import os
import requests
import json
from collections import Counter
import random
import time
import re
import datetime
# --- PHOENIX SETUP ---
try:
    from opentelemetry.instrumentation.requests import RequestsInstrumentor
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    
    tracer_provider = TracerProvider()
    otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:6006/v1/traces")
    tracer_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
    trace.set_tracer_provider(tracer_provider)
    tracer = trace.get_tracer(__name__)
    
    # Instrument requests to capture LLM calls
    RequestsInstrumentor().instrument()
    
    def trace_span(name):
        return tracer.start_as_current_span(name)
except ImportError:
    print("Warning: phoenix or opentelemetry not installed. Tracing disabled.")
    import contextlib
    @contextlib.contextmanager
    def trace_span(name):
        yield


def load_keys():
    keys = []
    groq_key = None
    env_path = 'd:\\NoteBookLLM_Br\\.env'
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("OPENROUTER_API_KEY"):
                    keys.append(line.strip().split('=', 1)[1])
                elif line.startswith("GROQ_API_KEY"):
                    groq_key = line.strip().split('=', 1)[1]
    return keys, groq_key

OPENROUTER_KEYS, GROQ_API_KEY = load_keys()
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"

# --- CONFIGURATION: ROLE-BASED COUNCIL (v3.0 - R21 Compliant) ---
def check_r21_compliance():
    """Verify that a log entry exists for today before proceeding (R21)."""
    today = datetime.date.today().strftime("%Y_%m_%d")
    log_path = f"d:\\NoteBookLLM_Br\\3-resources\\wiki\\logs\\log_{today}.md"
    if not os.path.exists(log_path):
        print("CRITICAL: Rule R21 violation. No daily log found.")
        return False
    return True

COUNCIL_MEMBERS = {
    "local/qwen2.5:3b": {
        "role": "Logician",
        "weight": 1.0,
        "focus": "Technical accuracy, schema validation, and logical consistency."
    },
    "local/hermes3:3b": {
        "role": "Generalist",
        "weight": 0.8,
        "focus": "Content clarity, pedagogical value, and general readability."
    },
    "local/qwen3:4b": {
        "role": "Dissenter",
        "weight": 1.2,
        "focus": "Finding contradictions, questioning source reliability, and identifying knowledge gaps. Be skeptical."
    }
}

LOCAL_ELDERS = list(COUNCIL_MEMBERS.keys())

# Cloud Judge remains the Supreme Authority
JUDGE_MODEL = "openrouter/nvidia/nemotron-3-super-120b-a12b:free"

def robust_json_parse(text: str):
    """Advanced JSON extraction with fuzzy decision mapping."""
    
    VALID_DECISIONS = {"SUPERSEDES A", "SUPERSEDES B", "MERGE", "REJECT BOTH", "KEEP BOTH"}
    
    def normalize_decision(d_text):
        if not d_text: return None
        d_text = str(d_text).upper()
        if "SUPERSEDE" in d_text and " B" in d_text: return "SUPERSEDES B"
        if "SUPERSEDE" in d_text and " A" in d_text: return "SUPERSEDES A"
        if "REJECT" in d_text: return "REJECT BOTH"
        if "KEEP" in d_text: return "KEEP BOTH"
        if "MERGE" in d_text: return "MERGE"
        # Exact match check
        for v in VALID_DECISIONS:
            if v in d_text: return v
        return None

    def try_parse(s):
        try:
            s = re.sub(r',\s*([\]\}])', r'\1', s)
            return json.loads(s)
        except: return None

    # 1. Extraction Phase
    blocks = re.findall(r'(\[.*\]|\{.*\})', text, re.DOTALL)
    blocks.sort(key=len, reverse=True)
    
    for b in blocks:
        parsed = try_parse(b)
        if parsed:
            a, r, raw_d = "", "", ""
            if isinstance(parsed, list) and len(parsed) >= 3:
                a, r, raw_d = str(parsed[0]), str(parsed[1]), str(parsed[2])
            elif isinstance(parsed, list) and len(parsed) > 0 and isinstance(parsed[0], dict):
                d = parsed[0]
                a, r, raw_d = d.get("assessment", ""), d.get("conflict_type", ""), d.get("decision", d.get("DECISION", ""))
            elif isinstance(parsed, dict):
                a, r, raw_d = parsed.get("assessment", ""), parsed.get("reason", parsed.get("conflict_type", "")), parsed.get("decision", "")
            
            final_d = normalize_decision(raw_d)
            if final_d: return a, r, final_d

    # 2. Regex Fallback Phase
    decision_match = re.search(r'(?:\*{0,2})DECISION(?:\*{0,2}):?\s*(\[?[\w\s]+\]?)', text, re.IGNORECASE)
    if decision_match:
        candidate = decision_match.group(1).strip('[] *\n')
        return "Bóc tách thủ công", "Regex fallback", normalize_decision(candidate)

    return None, None, None

def call_model(model_path: str, prompt: str, retries: int = 2) -> str:
    provider, model_id = model_path.split("/", 1)
    headers = {"Content-Type": "application/json"}
    
    if provider == "local":
        data = {
            "model": model_id, 
            "messages": [{"role": "user", "content": prompt}],
            "options": {"num_ctx": 8192, "temperature": 0.1, "num_predict": 2048}
        }
        try:
            response = requests.post(OLLAMA_URL, headers=headers, json=data, timeout=300)
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e: return f"Error: {e}"
        
    elif provider == "openrouter":
        for attempt in range(retries + 1):
            key = random.choice(OPENROUTER_KEYS)
            headers["Authorization"] = f"Bearer {key}"
            try:
                response = requests.post(OPENROUTER_URL, headers=headers, json={"model": model_id, "messages": [{"role": "user", "content": prompt}]}, timeout=60)
                if response.status_code == 200: return response.json()["choices"][0]["message"]["content"]
                time.sleep(5)
            except: continue
        return "Error: OpenRouter Failed"
    return "Error: Unknown provider"

@trace_span("Wiki-Council-Deliberation")
def run_council(case_description: str, atom_a_content: str, atom_b_content: str, supporting_context: list = None):
    """Run a Role-Based Council with Weighted Voting."""
    
    local_context_text = ""
    cloud_context_text = ""
    if supporting_context:
        local_context_text = "\nSUPPORTING CONTEXT:\n"
        cloud_context_text = "\nSUPPORTING CONTEXT (Full Evidence):\n"
        for ctx in supporting_context:
            summary = ctx.get('summary') or ctx.get('content', '')[:300] + "..."
            local_context_text += f"- {ctx['title']}: {summary}\n"
            cloud_context_text += f"### {ctx['title']}\n{ctx.get('content', 'No content')}\n\n"

    results = {}
    local_deliberations = []
    weighted_votes = Counter()
    total_valid_weight = 0

    print("\n--- STAGE 1: ROLE-BASED DELIBERATION ---")
    for model_path, config in COUNCIL_MEMBERS.items():
        print(f"[*] Triệu tập {config['role']} ({model_path})...")
        
        role_prompt = f"""You are the {config['role']} of the Wiki Council. 
Your specific focus is: {config['focus']}

### PROTOCOL:
1. Compare ATOM A vs ATOM B.
2. Evaluate based on source authority, technical depth, and recency.
3. {config['role'].upper()} SPECIAL INSTRUCTION: Ensure you address your specific focus area in the assessment.

Context: {case_description}
{local_context_text}

ATOM A:
{atom_a_content}

ATOM B:
{atom_b_content}

### OUTPUT FORMAT (STRICT JSON ONLY):
{{
  "assessment": "<your role-specific assessment>",
  "conflict_type": "<contradiction | complement | overlap>",
  "decision": "<DECISION>"
}}
DECISION: [SUPERSEDES A, SUPERSEDES B, MERGE, REJECT BOTH, KEEP BOTH].

IMPORTANT: 
- No preamble. No text outside JSON. 
- Ensure all quotes inside strings are escaped.
- Example BAD: "assessment": "Model "A" is better"
- Example GOOD: "assessment": "Model A is stronger because..."
"""
        # Hotfix: Kill thinking mode for Qwen3 to prevent parse failure
        final_prompt = role_prompt
        if "qwen3" in model_path:
            final_prompt = "/no_think\n" + role_prompt

        res = call_model(model_path, final_prompt)
        results[model_path] = res
        assessment, conflict_type, decision = robust_json_parse(res)
        
        if decision:
            # Explicitly use weight from config
            weight = config.get('weight', 1.0)
            weighted_votes[decision] += weight
            total_valid_weight += weight
            
            local_deliberations.append({
                "model": model_path,
                "role": config['role'],
                "decision": decision,
                "weight": weight,
                "assessment": assessment
            })
            print(f"  [+] {config['role']} voted: {decision} (Weight: {weight})")
        else:
            print(f"  [!] {config['role']} failed to provide valid output.")

    # --- STAGE 2: WEIGHTED CONSENSUS ---
    print("\n--- STAGE 2: WEIGHTED CONSENSUS ---")
    final_decision = None
    if local_deliberations:
        most_weighted, weight_sum = weighted_votes.most_common(1)[0]
        # Consensus threshold: > 50% of the total valid weight
        if weight_sum > total_valid_weight / 2:
            final_decision = most_weighted
            print(f"  [+] ĐẠT ĐỒNG THUẬN CÓ TRỌNG SỐ: {final_decision} ({weight_sum:.1f}/{total_valid_weight:.1f})")
    
    # --- STAGE 3: CHAIRMAN SYNTHESIS ---
    if not final_decision:
        print("\n--- STAGE 3: CHAIRMAN SYNTHESIS (CLOUD) ---")
        delibs_text = ""
        for d in local_deliberations:
            delibs_text += f"- {d['role']} ({d['model']}): Voted {d['decision']}. Assessment: {d['assessment']}\n"

        chairman_prompt = f"""You are the Supreme Judge. Resolve the conflict using local deliberations and full evidence.
Case: {case_description}
{cloud_context_text}

LOCAL DELIBERATIONS:
{delibs_text if delibs_text else "None."}

ATOM A: {atom_a_content}
ATOM B: {atom_b_content}

OUTPUT JSON ARRAY ONLY: ["<final assessment>", "<justification>", "<DECISION>"]
"""
        try:
            res = call_model(JUDGE_MODEL, chairman_prompt)
            _, _, final_decision = robust_json_parse(res)
            print(f"[*] PHÁN QUYẾT TỐI CAO: {final_decision}")
        except:
            final_decision = "REJECT BOTH"

    return {"final_decision": final_decision, "deliberations": local_deliberations, "raw_responses": results}

if __name__ == "__main__":
    print("Council Engine (Weighted Trio v2.5) ready.")

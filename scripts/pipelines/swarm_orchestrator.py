import sys
import os
import argparse
import json
from typing import List, Optional

# Add root directory to sys.path to import libs
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from libs.core.llm_client import (
    call_profiler,
    call_designer,
    call_pedagogical_engineer,
    call_evaluator,
    call_creative,
    call_auditor
)

def orchestrate():
    parser = argparse.ArgumentParser(description="Swarm Orchestrator - Execute Pedagogical Agents via 9Router")
    parser.add_argument("--role", required=True, choices=["profiler", "designer", "engineer", "evaluator", "creative", "auditor"], help="Agent role to invoke")
    parser.add_argument("--prompt", required=True, help="Task description for the agent")
    parser.add_argument("--context_files", nargs="*", help="List of files to include as context")
    parser.add_argument("--output", help="Optional file path to save the output")
    parser.add_argument("--model", help="Override default model for the agent role")
    parser.add_argument("--max_tokens", type=int, help="Override default max tokens")
    parser.add_argument("--temp", type=float, help="Override default temperature")
    
    args = parser.parse_args()
    
    # 1. Prepare messages with context
    messages = []
    
    if args.context_files:
        context_content = "--- CONTEXT DATA ---\n"
        for file_path in args.context_files:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    context_content += f"\n[FILE: {os.path.basename(file_path)}]\n{f.read()}\n"
            else:
                print(f"Warning: Context file {file_path} not found.")
        
        messages.append({"role": "user", "content": context_content})
    
    messages.append({"role": "user", "content": f"TASK:\n{args.prompt}"})
    
    print(f"[*] Calling Swarm Agent: @{args.role} via 9Router...")
    
    # 2. Invoke appropriate agent wrapper
    try:
        if args.role == "profiler":
            content, model = call_profiler(messages, model=args.model, max_tokens=args.max_tokens)
        elif args.role == "designer":
            content, model = call_designer(messages, model=args.model, max_tokens=args.max_tokens)
        elif args.role == "engineer":
            # Pass temperature only if it's supported by the wrapper (currently added to pedagogical_agent)
            content, model = call_pedagogical_engineer(messages, model=args.model, max_tokens=args.max_tokens)
        elif args.role == "evaluator":
            content, model = call_evaluator(messages, model=args.model, max_tokens=args.max_tokens)
        elif args.role == "creative":
            content, model = call_creative(messages, model=args.model, max_tokens=args.max_tokens)
        elif args.role == "auditor":
            content, model = call_auditor(messages, model=args.model, max_tokens=args.max_tokens)
        else:
            raise ValueError(f"Unknown role: {args.role}")
        
        print(f"[OK] Agent: @{args.role} | Model: {model}")
        
        # 3. Handle Output
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[+] Output saved to: {args.output}")
        else:
            print("\n--- AGENT RESPONSE ---\n")
            print(content)
            print("\n----------------------\n")
            
    except Exception as e:
        print(f"[ERROR] Swarm execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    orchestrate()

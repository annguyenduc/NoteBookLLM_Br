import os
from dotenv import load_dotenv

load_dotenv()

KEYS = [
    "OPENROUTER_API_KEY",
    "GROQ_API_KEY",
    "TOGETHERAI_API_KEY",
    "HUGGINGFACE_API_KEY"
]

print("--- Environment Check ---")
for k in KEYS:
    v = os.getenv(k)
    if v:
        # Check for common mistakes
        if v.startswith(("your_", "sk-", "gsk-", "pk-")):
            status = "FOUND"
            # Mask the middle
            masked = v[:5] + "..." + v[-4:] if len(v) > 10 else "***"
            print(f"{k}: {status} ({masked})")
        else:
            print(f"{k}: FOUND (Format: {v[:3]}...)")
            
        if v != v.strip():
            print(f"  WARNING: {k} has leading/trailing whitespace!")
        if v.startswith(("'", '"')) and v.endswith(("'", '"')):
            print(f"  WARNING: {k} might be quoted improperly in .env")
    else:
        print(f"{k}: NOT FOUND")

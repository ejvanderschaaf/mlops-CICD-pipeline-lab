import json
import os
import sys
from datetime import datetime, timezone

# Read accuracy from metrics file
with open("artifacts/metrics.txt", "r") as f:
    accuracy = float(f.read().strip())

# Accept commit SHA as a command-line argument
commit_sha = sys.argv[1] if len(sys.argv) > 1 else "unknown"

# Build model card
model_card = {
    "model": "LogisticRegression",
    "dataset": "Iris",
    "accuracy": accuracy,
    "commit_sha": commit_sha,
    "packaged_at": datetime.now(timezone.utc).isoformat(),
}

os.makedirs("artifacts", exist_ok=True)
with open("artifacts/model_card.json", "w") as f:
    json.dump(model_card, f, indent=2)

print(f"Model card written to artifacts/model_card.json")
print(json.dumps(model_card, indent=2))

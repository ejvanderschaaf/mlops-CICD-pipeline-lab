import sys

THRESHOLD = 0.80

with open("artifacts/metrics.txt", "r") as f:
    accuracy = float(f.read().strip())

print(f"Accuracy: {accuracy:.4f} | Threshold: {THRESHOLD}")

if accuracy < THRESHOLD:
    print("FAILED: Model accuracy is below the required threshold.")
    sys.exit(1)  # Non-zero exit code will fail the CI pipeline
else:
    print("PASSED: Model meets the performance threshold.")
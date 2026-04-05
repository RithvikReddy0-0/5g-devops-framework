import matplotlib.pyplot as plt
from collections import defaultdict
import re

log_file = "results/traffic_logs.txt"

counts = defaultdict(int)

with open(log_file, "r") as f:
    for line in f:
        if "VIDEO" in line:
            counts["video"] += 1
        elif "FILE" in line:
            counts["file"] += 1
        elif "WEB" in line:
            counts["web"] += 1

labels = list(counts.keys())
values = list(counts.values())

plt.figure()
plt.bar(labels, values)

plt.xlabel("Traffic Type")
plt.ylabel("Number of Requests")
plt.title("5G Network Slice Traffic Distribution")

plt.savefig("results/traffic_distribution.png")
plt.show()

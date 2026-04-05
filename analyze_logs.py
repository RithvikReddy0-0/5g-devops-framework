import re
import matplotlib.pyplot as plt
from collections import defaultdict

log_file = "run_logs.txt"

time_counts = defaultdict(lambda: {"video":0, "web":0, "file":0})

with open(log_file, "r") as f:
    for line in f:
        match = re.search(r"\[(.*?)\].*SERVER \| (VIDEO|WEB|FILE)", line)
        if match:
            time = match.group(1)[-8:]  # extract HH:MM:SS
            traffic = match.group(2).lower()
            time_counts[time][traffic] += 1

times = sorted(time_counts.keys())
video = [time_counts[t]["video"] for t in times]
web = [time_counts[t]["web"] for t in times]
file = [time_counts[t]["file"] for t in times]

plt.figure()
plt.plot(times, video, label="Video Traffic")
plt.plot(times, web, label="Web Traffic")
plt.plot(times, file, label="File Traffic")

plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Number of Requests")
plt.title("Traffic Distribution Over Time")
plt.legend()

plt.tight_layout()
plt.savefig("traffic_graph.png")
plt.show()

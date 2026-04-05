import matplotlib.pyplot as plt
from collections import defaultdict
import re

log_file = "traffic_logs.txt"

# structure: {time: {type: count}}
data = defaultdict(lambda: {"video": 0, "file": 0, "web": 0})

with open(log_file, "r") as f:
    for line in f:
        # extract time (HH:MM:SS)
        match = re.search(r"\[(.*?)\]", line)
        if not match:
            continue

        timestamp = match.group(1).split(" ")[1]  # only time

        if "VIDEO" in line:
            data[timestamp]["video"] += 1
        elif "FILE" in line:
            data[timestamp]["file"] += 1
        elif "WEB" in line:
            data[timestamp]["web"] += 1

# sort timestamps
times = sorted(data.keys())

video_counts = [data[t]["video"] for t in times]
file_counts = [data[t]["file"] for t in times]
web_counts = [data[t]["web"] for t in times]

plt.figure()

plt.plot(times, video_counts, label="Video")
plt.plot(times, file_counts, label="File")
plt.plot(times, web_counts, label="Web")

plt.xlabel("Time")
plt.ylabel("Requests per second")
plt.title("5G Traffic Over Time")
plt.legend()

plt.xticks(rotation=45)

plt.savefig("traffic_time_series.png")
plt.show()

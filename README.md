# 🚀 5G DevOps Framework with Kubernetes, Prometheus & Grafana

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

A complete simulation framework for **5G network traffic generation, monitoring, and DevOps automation** using Kubernetes.
This project demonstrates how modern telecom systems can be **observed, scaled, and optimized in real time**.

---

## 📌 Project Overview

This project simulates a **5G network environment** with multiple User Equipment (UE) types generating traffic.
The system is deployed using **Kubernetes**, monitored using **Prometheus**, and visualized using **Grafana**.

The goal is to replicate real-world **network slicing, traffic behavior, and observability** in a cloud-native setup.

---

## 🧠 Key Concepts Demonstrated

- 5G Traffic Simulation (Video, Web, File transfers)
- Kubernetes-based Microservices Deployment
- Real-time Metrics Collection via Prometheus
- Visualization & Monitoring with Grafana Dashboards
- DevOps Automation using Makefile
- Scalable Architecture with multiple UE pods

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│           UE Pods (Kubernetes)          │
│  📺 Video UE  🌐 Web UE  📁 File UE    │
└────────────────┬────────────────────────┘
                 │ HTTP Requests
                 ▼
┌─────────────────────────────────────────┐
│        Traffic Server (Flask API)       │
│         Exposes /metrics endpoint       │
└──────────┬──────────────────────────────┘
           │ Scrapes /metrics
           ▼
┌─────────────────────────────────────────┐
│           Prometheus                    │
│     Time-series metrics storage         │
└──────────┬──────────────────────────────┘
           │ Data source
           ▼
┌─────────────────────────────────────────┐
│              Grafana                    │
│     Real-time dashboards & alerts       │
└─────────────────────────────────────────┘
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| **Kubernetes** | Container orchestration |
| **Docker** | Containerization |
| **Python (Flask)** | Traffic server & metrics endpoint |
| **Prometheus** | Metrics scraping & storage |
| **Grafana** | Monitoring dashboards |
| **Makefile** | DevOps automation |
| **WSL (Linux)** | Development environment |

---

## 📂 Project Structure

```
5g-devops-framework/
│
├── core/               # Core traffic server logic
├── ues/                # User Equipment simulators
├── k8s/                # Kubernetes manifests
├── monitoring/         # Prometheus & Grafana configs
├── optimization/       # Analysis and improvements
├── logs/               # Generated logs
├── results/            # Output results & graphs
├── Makefile            # Automation commands
├── docker-compose.yml  # Local testing setup
└── analyze_logs.py     # Log analysis script
```

---

## 🚀 How to Run

### 1. Setup Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Start Kubernetes System

```bash
make start
```

### 3. Verify Running Pods

```bash
make pods
```

### 4. Check Services

```bash
make svc
```

### 5. View Logs

```bash
make logs
```

### 6. Open Prometheus

```bash
make prometheus
```

Navigate to: `http://localhost:9090`

### 7. Open Grafana

```bash
make grafana
```

Navigate to: `http://localhost:3000`

### 8. Stop the System

```bash
make stop
```

---

## 🔍 What's Happening Internally

### 🔹 UE Simulation

Multiple pods simulate different 5G traffic profiles:

| UE Type | Traffic Pattern | Use Case |
|---|---|---|
| 📺 Video UE | High bandwidth, sustained | Streaming |
| 🌐 Web UE | Moderate, request-response | Browsing |
| 📁 File UE | Bursty, large payloads | Downloads |

Each UE continuously sends requests to the traffic server, mimicking real network load.

### 🔹 Traffic Server

- Built with **Flask**
- Handles and classifies incoming UE requests
- Exposes a `/metrics` endpoint in Prometheus format

### 🔹 Prometheus

- Scrapes `/metrics` on a configured interval
- Stores time-series data for querying via PromQL

### 🔹 Grafana

Visualizes key metrics including:
- Request rate per UE type
- Traffic distribution across pods
- System performance over time

---

## 📈 Sample Output

- Real-time traffic logs per UE pod
- Prometheus metrics at `/metrics`
- Grafana dashboards with live graphs
- Traffic distribution plots from `analyze_logs.py`

---

## ⚠️ Challenges & Solutions

| Challenge | Solution |
|---|---|
| `ErrImageNeverPull` in Kubernetes | Fixed image builds; configured local Docker registry correctly |
| Git authentication errors | Switched to SSH key authentication |
| Merge conflicts | Resolved using `git rebase` and branch hygiene |
| Prometheus config issues | Debugged scrape targets; verified endpoint accessibility |
| Pod-to-pod communication failures | Corrected Kubernetes service endpoints and DNS resolution |

---

## 💡 Key Learnings

- Real-world DevOps workflows in a cloud-native environment
- Kubernetes debugging techniques (`kubectl logs`, `describe`, `exec`)
- Monitoring and observability for distributed systems
- Managing Git conflicts in collaborative/production scenarios

---

## 🔥 Future Improvements

- [ ] Network slicing implementation per UE type
- [ ] AI-based traffic optimization and anomaly detection
- [ ] Auto-scaling policies based on live traffic load
- [ ] Integration with a real 5G core (Open5GS / OAI)

---

## 👨‍💻 Author

**Rithvik Reddy**
Computer Science Student | DevOps & Cloud-Native Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub — it helps others discover it!

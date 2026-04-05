# 5G DevOps Framework (Free5GC + UERANSIM)

## Overview
This project implements a DevOps-based framework to deploy, test, and validate a cloud-native 5G-Advanced network stack in a repeatable and automated manner.

The deployment uses:
- Free5GC as the 5G Core Network
- UERANSIM as simulated gNB and UE
- Docker Compose for automation and reproducibility
- KPI testing using ping and iperf3

---

## Objectives
- Deploy Free5GC 5G Core using Docker Compose
- Deploy simulated gNB and UE using UERANSIM
- Perform UE registration and PDU session establishment
- Validate end-to-end internet connectivity
- Perform KPI tests such as latency and throughput

---

## Project Structure

5g-devops-framework/
│── core/free5gc/free5gc-compose/
│── ran/UERANSIM/
│── results/kpi_tests/
│── docs/screenshots/
│── scripts/
│── README.md


---

## Deployment Steps

### 1. Start 5G Core (Free5GC)
```bash
cd core/free5gc/free5gc-compose
docker compose up -d
```
Check status:
```bash
docker compose ps
```

### 2.Run UERANSIM gNB + UE
Inside UERANSIM container:
```bash
docker exec -it ueransim bash
./nr-ue -c config/uecfg.yaml
```
---

## KPI Testing 

### Ping test (Google DNS)
```bash
docker exec ueransim bash -c "ping -c 20 8.8.8.8"
```

### Ping test (google.com)
```
docker exec ueransim bash -c "ping -c 3 google.com"
```
### Throughput test (iperf3)
```
docker exec ueransim bash -c "iperf3 -c 172.20.4.156 -t 20"
```

---

## Results

- All KPI results are stored under:

- results/kpi_tests/

- Including:

- ping logs

- iperf3 throughput logs

- docker compose status output

- UE IP output

- Free5GC + UERANSIM container logs

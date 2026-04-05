# ===============================
# 5G DevOps Framework Automation
# ===============================

.PHONY: build deploy start stop clean logs pods svc restart

# 🔨 Build Docker image
build:
	docker build -t traffic-server:latest ./ues

# 🚀 Deploy to Kubernetes
deploy:
	kubectl apply -f k8s/manifests/

# 🔥 Start full system
start: build deploy
	@echo "System started 🚀"

# 🛑 Stop everything
stop:
	kubectl delete -f k8s/manifests/
	@echo "System stopped 🛑"

# 💀 Clean Docker system (dangerous)
clean:
	docker system prune -a -f
	@echo "Docker cleaned 💀"

# 📊 View pods
pods:
	kubectl get pods

# 🌐 View services
svc:
	kubectl get svc

# 📜 Logs (server)
logs:
	kubectl logs -l app=traffic-server -f

# 🔁 Restart server
restart:
	kubectl delete pod -l app=traffic-server
	@echo "Server restarting 🔁"

# 🔗 Port forward Prometheus
prometheus:
	kubectl port-forward svc/prometheus-service 9090:9090

# 🔗 Port forward server
server:
	kubectl port-forward svc/traffic-server-service 5000:5000

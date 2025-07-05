# 📦 ML Pipeline (Kubernetes + Helm + CI/CD)

This project demonstrates a simple **Data Science and Engineering Pipeline** using:
- 🐳 Docker
- ☸️ Kubernetes
- 🎛️ Helm
- 🔁 GitHub Actions (CI/CD)

---

## 📁 Project Structure

```
.
├── data-pipeline/
│   ├── etl.py
│   └── Dockerfile
├── model-trainer/
│   ├── train.py
│   └── Dockerfile
├── model-api/
│   ├── app.py
│   └── Dockerfile
├── k8s-helm/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       └── *.yaml
└── .github/
    └── workflows/
        └── ci-cd.yml
```

---

## ⚙️ How It Works

1. **ETL** fetches and stores Iris dataset → `/data`
2. **Trainer** reads `/data`, trains a model, saves it → `/models`
3. **API** loads model from `/models` and serves predictions via Flask

---

## 🚀 Running It

### 1. Start Kubernetes (locally using Minikube)
```bash
minikube start
```

### 2. Deploy using Helm
```bash
helm install ml-pipeline ./k8s-helm
```

### 3. Access API
```bash
minikube service model-api
```

Test prediction:
```bash
curl -X POST http://<MODEL_API_URL>/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

---

## 🔁 GitHub Actions (CI/CD)

- Builds Docker images for each stage
- Pushes them to **GitHub Container Registry (GHCR)**
- Deploys/updates app via Helm automatically

No Terraform required — 100% K8s native.

---

## 📦 Persistent Storage

- `/data` shared via `shared-data-pvc`
- `/models` shared via `model-pvc`

---

## 🔒 Secrets

To securely push to GHCR, GitHub Actions uses:
```yaml
secrets:
  GITHUB_TOKEN: default secret provided by GitHub
```

---

## 🧹 Cleanup
```bash
helm uninstall ml-pipeline
minikube stop
```

---

## 📌 Requirements

- Docker
- Minikube (or other K8s distro)
- Helm
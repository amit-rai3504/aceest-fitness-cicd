# 🧩 ACEest Fitness & Gym — CI/CD Pipeline

This repository implements a complete **CI/CD pipeline** for the ACEest Fitness Flask web application using **Jenkins**, **SonarQube**, **Docker**, and **Kubernetes**.

---

## 📦 Project Overview

| Component | Description |
|------------|-------------|
| **App Framework** | Flask (Python 3.11) |
| **Testing** | Pytest + Coverage |
| **CI/CD Orchestrator** | Jenkins |
| **Code Quality** | SonarQube Community Edition |
| **Containerization** | Docker |
| **Deployment Strategies** | Blue/Green, Canary, Rolling, Shadow, and A/B (Kubernetes manifests) |

---

## ⚙️ Jenkins Pipeline Stages

1. **Checkout**  
   Clones the latest code from the `main` branch.

2. **Setup Python**  
   Creates a virtual environment and installs dependencies from `requirements.txt`.

3. **Unit Tests**  
   Runs all pytest tests, exports `pytest.xml` and `coverage.xml` for reporting.

4. **SonarQube Analysis**  
   Uses the official `sonarsource/sonar-scanner-cli` image (via Docker) to analyze code and push metrics to SonarQube.

5. **Docker Build**  
   Builds the application image using `Dockerfile`.

6. **Container Verification**  
   Spins up a temporary container, verifies the `/health` endpoint, and cleans up automatically.

---

## ✅ Folder structure for screenshots

docs/
├── jenkins_console_logs.png
├── jenkins_succesful_build.png
├── jenkins_test.png
└── sonarqube.png
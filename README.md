# ACEest Fitness & Gym — CI/CD

This repo contains a minimal Flask web app wired for CI/CD with Jenkins, pytest,
SonarQube, Docker, and Kubernetes (blue/green, canary, shadow, A/B, rolling).

## Local quickstart
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m flask --app app run -p 5000
curl http://localhost:5000/health

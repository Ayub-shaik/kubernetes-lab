from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# -----------------------------
# Metrics Tracking
# -----------------------------
REQUEST_COUNT = 0


@app.before_request
def count_requests():
    global REQUEST_COUNT
    REQUEST_COUNT += 1


# -----------------------------
# DB Config (future-ready)
# -----------------------------
DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "companydb")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


# -----------------------------
# Core APIs
# -----------------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "backend-api"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": "v2"
    })


@app.route("/api/jobs")
def jobs():
    return jsonify({
        "jobs": [
            {"id": 1, "name": "devops-engineer"},
            {"id": 2, "name": "platform-engineer"},
            {"id": 3, "name": "sre-engineer"}
        ],
        "status": "success"
    })


@app.route("/api/cluster-health")
def cluster_health():
    return jsonify({
        "backend": "running",
        "frontend": "running",
        "postgres": "running",
        "ci_cd": "active",
        "gitops": "argo-enabled",
        "cluster": "k3s-ready"
    })


@app.route("/api/metrics")
def metrics():
    return jsonify({
        "requests": REQUEST_COUNT,
        "service": "backend-api",
        "status": "ok"
    })


# Optional root (safe response)
@app.route("/")
def root():
    return jsonify({
        "service": "backend-api",
        "status": "running"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
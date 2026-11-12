from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "devops-service",
        "status": "running"
    })


@app.route("/health")
def health():
    version = os.environ.get("APP_VERSION", "v1.0.0")
    return jsonify({
        "status": "healthy",
        "service": "devops-service",
        "version": version
    })


@app.route("/version")
def version():
    v = os.environ.get("APP_VERSION", "v1.0.0")
    return jsonify({"version": v})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

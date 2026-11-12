
from flask import Flask, jsonify
import os
import time
app = Flask(__name__)
START_TIME = time.monotonic()
APP_VERSION = os.environ.get("APP_VERSION", "v1.1.0")
@app.route("/")
def home():
    return jsonify({
        "service": "devops-service",
        "status": "running"
    })



@app.route("/health")
def health():
    uptime_seconds = int(time.monotonic() - START_TIME)

    return jsonify(
        service="devops-service",
        status="healthy",
        version=APP_VERSION,
        uptime_seconds=uptime_seconds
    ), 200


@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

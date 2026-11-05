
import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Team Service Information</title>
    </head>
    <body>
        <h1>Team Service Information</h1>
        <h2>Welcome to Our DevOps Web Service</h2>

        <p><strong>Service:</strong> Team Information Service</p>
        <p><strong>Description:</strong> A sample web service for our DevOps project.</p>
        <p><strong>Contact:</strong> team@example.com</p>
        <p><strong>Operating Hours:</strong> Monday - Friday, 9 AM - 5 PM</p>
        <p><strong>Application Version:</strong> {{ version }}</p>

        <a href="/health">Check Service Health</a>
    </body>
    </html>
    """, version=APP_VERSION)

@app.route("/health")
def health():
    return jsonify(status="healthy", version=APP_VERSION), 200

@app.route("/version")
def version():
    return jsonify(version=APP_VERSION), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

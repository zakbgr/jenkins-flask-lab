import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "local")
    return f"<h1>Jenkins CI/CD Lab</h1><p>Version: {version}</p>"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

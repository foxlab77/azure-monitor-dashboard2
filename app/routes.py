from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Azure Monitor Dashboard Running 🚀"

@main.route("/health")
def health():
    return jsonify({"status": "ok"})
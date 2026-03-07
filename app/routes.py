from flask import Blueprint, render_template, jsonify
from .query_client import query_logs
from .log_client import send_log

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "Azure Monitor Dashboard Started 🚀"


@main.route("/generate-log")
def generate_log():
    send_log("Hello from Flask app")
    return {"status": "log sent"}


@main.route("/dashboard")
def dashboard():

    logs = query_logs()

    return render_template(
        "dashboard.html",
        logs=logs,
        timestamps=timestamps,
        counts=counts
    )


@main.route("/logs")
def logs():

    return jsonify(query_logs())
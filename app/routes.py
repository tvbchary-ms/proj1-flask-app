from flask import Blueprint, current_app
import socket
import datetime

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return f"""
    <h1>🚀 DevOps Flask App</h1>
    <p><b>Version:</b> {current_app.config['VERSION']}</p>
    <p><b>Environment:</b> {current_app.config['ENVIRONMENT']}</p>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Time:</b> {datetime.datetime.now()}</p>
    <br>
    <h4>Designed and Deployed by TV Bhaskarachary （丁陽）, Tamkang University </h4>
    """

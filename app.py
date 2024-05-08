import os

from flask import Flask, jsonify, request, abort
import requests

settings = {
    "APP": os.environ.get("APP", "myapp"),
    "ALLOWED_APPS": os.environ.get("ALLOWED_APPS", "app1,app2").split(","),
}

app = Flask(settings["APP"])


@app.route("/")
def hello():
    return jsonify({"app": settings["APP"]})


@app.route("/reach")
def reach():
    dest_app = request.args.get("app")
    if dest_app in settings["ALLOWED_APPS"]:
        url = f"http://{dest_app}"
        resp = requests.get(url).json()
        return jsonify({"app": settings["APP"], "reached": resp["app"]})
    else:
        abort(404)

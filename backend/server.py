from flask import Flask, request

from .Handler import Handler

app = Flask(__name__)

db = {}

@app.route("/", methods=["GET", "POST"])
def server():
    if request.method == "GET":
        return {"jsonrpc": "2.0", "result": "OK"}
    handler = Handler(db)
    return handler.handleRequest(request.json)


@app.errorhandler(404)
def not_found(error):
    return "404", 404

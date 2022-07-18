from unittest import result
from flask import Flask, jsonify


app = Flask(__name__)

aws_key = "AKIAIOSFODNN7EXAMPLE"

@app.route("/", methods=["GET"])
def first():
    result = "Hello World"
    return (result)

@app.route("/version", methods=["GET"])
def version():
    result = "1.0.0"
    return (result)

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="127.0.0.1")
   
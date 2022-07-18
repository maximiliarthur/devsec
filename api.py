from unittest import result
from flask import Flask, jsonify


app = Flask(__name__)



@app.route("/", methods=["GET"])
def first():
    result = "Hello World"
    return (result)

@app.route("/version", methods=["GET"])
def version():
    result = "1.0.0"
    return (result)

if __name__ == "__main__":
    app.run(debug=False, port=8080, host="127.0.0.1")
   
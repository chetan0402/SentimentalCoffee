from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("manager_index.html")


@app.route("/api/getDB")
def giveDB():
    return "not done yet"


if __name__ == "__main__":
    app.run()

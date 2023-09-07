from flask import Flask, render_template
import sqlite3
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("manager_index.html")


@app.route("/api/getDB")
def giveDB():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    result = cur.execute("""
    SELECT * FROM "main"."data"
    """).fetchall()
    return_dict = {}
    for element in result:
        return_dict[element[0]] = [element[1], element[2], element[3], element[4]]
    cur.close()
    con.close()
    return json.dumps(return_dict)


if __name__ == "__main__":
    app.run(port=8080)

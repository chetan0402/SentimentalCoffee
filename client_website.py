from flask import Flask, render_template, request, jsonify
import uuid
import sqlite3
from transformers import pipeline
from threading import Thread

sentiment_pipline = pipeline("sentiment-analysis")
app = Flask(__name__)


def dataProcessThread(unique_id, review):
    result = sentiment_pipline([review])
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(
        """
        UPDATE "main"."data" SET "type"=?,processed=1 WHERE "uuid"=?
        """, (result[0]["label"], unique_id)
    )
    cur.close()
    con.commit()
    con.close()


@app.route("/")
def index():
    return render_template("client_index.html")


@app.route("/api/add")
def add_review():
    name = request.args.get("name")
    review = request.args.get("review")

    con = sqlite3.connect("data.db")
    cur = con.cursor()
    unique_id = str(uuid.uuid4()).replace("-", "")
    cur.execute("""
    INSERT INTO "main"."data"("uuid","name","review","type","processed") VALUES (?,?,?,NULL,0);
    """, (unique_id, name, review))
    cur.close()
    con.commit()
    con.close()
    Thread(target=dataProcessThread, args=(unique_id, review)).start()
    return jsonify({
        "status": "OK"
    })


if __name__ == "__main__":
    app.run()

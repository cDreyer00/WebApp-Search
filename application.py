from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("database", check_same_thread=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    print(query)
    results = db.execute("SELECT * FROM books WHERE title LIKE ?", ["%" + query + "%"])
    return render_template("search.html", results=results)
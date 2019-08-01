#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/teams/")
def bad_teams():
   return render_template("badteam.html")

if __name__ == "__main__":
   app.run(port=5006)

from flask import Flask, render_template, request

app = Flask("where")

@app.route("/")
def initial():
	return render_template("index.html")

app.run()
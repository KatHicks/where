from flask import Flask, render_template, request

app = Flask("where")

@app.route("/")
def initial():
	return render_template("index.html")

@app.route("/form")
def basic_form():
	return render_template("form.html")

def search():
	form_data = request.form







	return render_template("result.html")

app.run()
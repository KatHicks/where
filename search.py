from flask import Flask, render_template, request

app = Flask("where")

#loads home page at parent root
@app.route("/")
def initial():
	return render_template("index.html")

#then loads form page after linking through to form root with home page enter button
@app.route("/form")
def basic_form():
	return render_template("form.html")

#then loads results page after clicking submit on the form and uses form data in its return
@app.route("/result", methods=['post'])
def query():
	form_data = request.form

	return render_template("result.html")

#image api query
#city_img = "https://source.unsplash.com/category/buildings/?" + "london"
#note to render into html page need to be arguments of a new function and added into render_template

app.run(debug=True)
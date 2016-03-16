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
def getty(city):
	endpoint = "https://api.gettyimages.com/v3/search/images"
	payload = {"phrase": city, "rating": "pg", "api_key": "dc6zaTOxFJmzC"}
	response = requests.get(endpoint, params=payload)

	data = response.json()

	result = data['data'][0]['images']['fixed_height']['url']

	return result

#running the app
app.run(debug=True)
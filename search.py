from flask import Flask, render_template, request
import requests, csv, unicodecsv, os, sys, operator

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

def selector():
	form_data = request.form

	filtered_list = []
	input_file = None

	month = request.form['month']
	weather = request.form['weather']
	average_flight = request.form['budget_flights']

	if weather == 'hot':
		min_temp = 25
		max_temp = sys.maxint
	elif(weather == 'warm'):
		min_temp = 20
		max_temp = 25
	elif(weather == 'mild'):
		min_temp = 5
		max_temp = 20
	elif(weather == 'cold'):
		min_temp = -273
		max_temp = 5
	else:
		print "uh oh wrong temperature input"

	if average_flight == 'cheap':
		min_flight = 0
		max_flight = 100
	elif(average_flight == 'midrange'):
		min_flight = 100
		max_flight = 350
	elif(average_flight == 'expensive'):
		min_flight = 350
		max_flight = sys.maxint
	else:
		print "uh oh wrong budget input"

	with open("cities-data.csv") as csvfile:
	 	input_file = csv.DictReader(csvfile)
	 	for row in input_file:
	 		input_month = month
	 		row_month = row['Month']
	 		average_temp = float(row['Avg_Min_Temp_C'])
	 		average_flight = float(row['Avg_Min_Flight_Price_GBP'])

	 		if row_month == input_month and average_temp > min_temp and average_temp < max_temp and average_flight < max_flight and average_flight > min_flight:
	 		 	filtered_list.append(row)

	 	filtered_list.sort(key=operator.itemgetter('Avg_Min_Flight_Price_GBP'))

	destinations = filtered_list[0:3]

	print destinations

	#example result for destinations: 
	#[{'Avg_Min_Flight_Price_GBP': '405', 'City': 'Shanghai', 'Month': 'June', 'Avg_Min_Temp_C': '21.7', 'Country': 'China'}, 
	#{'Avg_Min_Flight_Price_GBP': '429', 'City': 'Kolkata', 'Month': 'June', 'Avg_Min_Temp_C': '20.1', 'Country': 'India'}, 
	#{'Avg_Min_Flight_Price_GBP': '433', 'City': 'Ho Chi Minh City', 'Month': 'June', 'Avg_Min_Temp_C': '24.5', 'Country': 'Vietnam'}]

	return render_template("result.html")

#image api query
#city_img = "https://source.unsplash.com/category/buildings/?" + "london"
#note to render into html page need to be arguments of a new function and added into render_template

app.run(debug=True)
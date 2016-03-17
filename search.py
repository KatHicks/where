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
		print "Uh oh, wrong temperature input!"

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
		print "Uh oh, wrong budget input!"

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

	#example result for destinations: 
	#[{'Avg_Min_Flight_Price_GBP': '405', 'City': 'Shanghai', 'Month': 'June', 'Avg_Min_Temp_C': '21.7', 'Country': 'China'}, 
	#{'Avg_Min_Flight_Price_GBP': '429', 'City': 'Kolkata', 'Month': 'June', 'Avg_Min_Temp_C': '20.1', 'Country': 'India'}, 
	#{'Avg_Min_Flight_Price_GBP': '433', 'City': 'Ho Chi Minh City', 'Month': 'June', 'Avg_Min_Temp_C': '24.5', 'Country': 'Vietnam'}]

	#---END OF SELECTOR SECTION AND START OF RENDERING SECTION---#

	if len(destinations)==3:
		result_one = destinations[0]
		result_two = destinations[1]
		result_three = destinations[2]

		#declaring variables to pass into the render template
		city_one = result_one['City']
		country_one = result_one['Country']
		city_img_one = "https://source.unsplash.com/category/buildings/?" + city_one
		month_one = result_one['Month']
		price_one = result_one['Avg_Min_Flight_Price_GBP']
		temp_one = result_one['Avg_Min_Temp_C']

		city_two = result_two['City']
		country_two = result_two['Country']
		city_img_two = "https://source.unsplash.com/category/buildings/?" + city_two
		month_two = result_two['Month']
		price_two = result_two['Avg_Min_Flight_Price_GBP']
		temp_two = result_two['Avg_Min_Temp_C']

		city_three = result_three['City']
		country_three = result_three['Country']
		city_img_three = "https://source.unsplash.com/category/buildings/?" + city_three
		month_three = result_three['Month']
		price_three = result_three['Avg_Min_Flight_Price_GBP']
		temp_three = result_three['Avg_Min_Temp_C']

		return render_template("result.html", 
			city1=city_one, country1=country_one, url1=city_img_one, month1=month_one, price1=price_one, temp1=temp_one,
			city2=city_two, country2=country_two, url2=city_img_two, month2=month_two, price2=price_two, temp2=temp_two,
			city3=city_three, country3=country_three, url3=city_img_three, month3=month_three, price3=price_three, temp3=temp_three)

	elif len(destinations)==2:

		result_one = destinations[0]
		result_two = destinations[1]

		#declaring variables to pass into the render template
		city_one = result_one['City']
		country_one = result_one['Country']
		city_img_one = "https://source.unsplash.com/category/buildings/?" + city_one
		month_one = result_one['Month']
		price_one = result_one['Avg_Min_Flight_Price_GBP']
		temp_one = result_one['Avg_Min_Temp_C']

		city_two = result_two['City']
		country_two = result_two['Country']
		city_img_two = "https://source.unsplash.com/category/buildings/?" + city_two
		month_two = result_two['Month']
		price_two = result_two['Avg_Min_Flight_Price_GBP']
		temp_two = result_two['Avg_Min_Temp_C']

		return render_template("result.html", 
			city1=city_one, country1=country_one, url1=city_img_one, month1=month_one, price1=price_one, temp1=temp_one,
			city2=city_two, country2=country_two, url2=city_img_two, month2=month_two, price2=price_two, temp2=temp_two)

	elif len(destinations)==1:
		result_one = destinations[0]

		#declaring variables to pass into the render template
		city_one = result_one['City']
		country_one = result_one['Country']
		city_img_one = "https://source.unsplash.com/category/buildings/?" + city_one
		month_one = result_one['Month']
		price_one = result_one['Avg_Min_Flight_Price_GBP']
		temp_one = result_one['Avg_Min_Temp_C']

		return render_template("result.html", 
			city1=city_one, country1=country_one, url1=city_img_one, month1=month_one, price1=price_one, temp1=temp_one)

	else:
		return render_template("result.html")

app.run(debug=True)
import requests, csv, unicodecsv, os, sys, operator

#list of dictionaries in the format:
#{'Avg_Min_Flight_Price_GBP': '492', 'City': 'Washington D.C.', 'Month': 'September', 'Avg_Min_Temp_C': '17.2', 'Country': 'United States of America'}

#note on setting min and max values: set defaults in the function - if arg exists then use given otherwise default -sys.maxint - 1


filtered_list = []
input_file = None


month = 'August' # = request.form['month']
weather = 'hot' #= (request.form['month'])
average_flight = 'cheap' #=flights_price = request.form['budget_flights'])

#weather selector
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

#flight selector
if average_flight == 'cheap':
	min_flight = 0
	max_flight = 100
elif(weather == 'midrange'):
	min_flight = 100
	max_flight = 350
elif(weather == 'expensive'):
	min_flight = 350
	max_flight = sys.maxint
else:
	print "uh oh wrong budget input"


#def selector(month, weather, price):
with open("cities-data.csv") as csvfile:
	input_file = csv.DictReader(csvfile)
	for row in input_file:
		input_month = month
		row_month = row['Month']
		average_temp = float(row['Avg_Min_Temp_C'])
#		min_temp = -273
#		max_temp = sys.maxint
		average_flight = float(row['Avg_Min_Flight_Price_GBP'])
		min_flight = 0
		max_flight = sys.maxint

		if row_month == input_month and average_temp > min_temp and average_temp < max_temp and average_flight < max_flight and average_flight > min_flight:
		 	filtered_list.append(row)

filtered_list.sort(key=operator.itemgetter('Avg_Min_Flight_Price_GBP'))

print filtered_list[0:3]

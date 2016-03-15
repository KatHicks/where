import requests, csv, unicodecsv


with open('city_weather.csv') as m:
	for row in m:
		print row
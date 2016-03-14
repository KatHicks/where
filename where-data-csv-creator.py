import requests, csv, unicodecsv
		
headers = ['city', 'month', 'avg_min_temperature']
with open('city_weather.csv', mode='w') as csvfile:
		writer = unicodecsv.DictWriter(csvfile, headers)

def write_csv(city):	
	weather_endpoint = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
	payload = {"key": "5d1f90a4fc1d448980f202203161003", "q": city, "format": "json","mca": "yes" }

	response = requests.get(weather_endpoint, params=payload)
	data = response.json()

	month_index = 0

	while month_index <= 11:
		month = data['data']['ClimateAverages'][0]['month'][month_index]['name']
		avg_min_temperature = data['data']['ClimateAverages'][0]['month'][month_index]['avgMinTemp']

		with open('city_weather.csv', mode='a') as csvfile:
			writer = unicodecsv.DictWriter(csvfile, headers)
			writer.writerow({'city': city, 'month': month, 'avg_min_temperature': avg_min_temperature})

		month_index = month_index + 1
	

cities = []

with open('top-100-cities.csv') as f:
	reader = csv.reader(f)
	cities = list(reader)

#cities = ["Paris", "London", "New York", "Hong Kong", "Singapore", "Bangkok", "Macau", "Kuala Lumpur", "Shenzhen", "Antalya", "Paris", "Istanbul", "Rome", "Dubai"]

for city in cities:
	write_csv(city)


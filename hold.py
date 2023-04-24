print(response.json()['location']['name'])

#  tomorrow.io API
url = "https://api.tomorrow.io/v4/weather/forecast?location=newyork&apikey=1xKR2c5vCp2WQO6ci3o6FljhPuTkB2GP"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)


# OWM 
"api.openweathermap.org/data/2.5/weather?id=524901&appid=YOUR_API_KEY"
api_key_owm = "814573ba0a3f07c527d7b784fee3eff0"

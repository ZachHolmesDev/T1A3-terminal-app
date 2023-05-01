#  tomorrow.io API
def get_current_weather_tmrio(selected_city):
    selected_city = requests.get(f"https://api.tomorrow.io/v4/weather/forecast?location={selected_city}&apikey=1xKR2c5vCp2WQO6ci3o6FljhPuTkB2GP")
# OWM 
"api.openweathermap.org/data/2.5/weather?id=524901&appid=YOUR_API_KEY"
api_key_owm = "814573ba0a3f07c527d7b784fee3eff0"

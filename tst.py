import requests
# import os 

api_key_wapi_caleb = "3328658fef7c4737a1635629232204"

# Ui functions
# --------------------------
def print_ui(selected_city, current_weather_response, option):
    # os.system('cls' if os.name == 'nt' else 'clear')
    print_menu(selected_city)
    if option == '1':
        print_current_weather(current_weather_response)

def print_menu(selected_city,):
    print("================================================")
    print("---Welcome to T1A3 Weather CLI---")
    print("[s] Select City ")
    print("[1] Get current weather  for Selected City ")
    print("[2] Display forecast     for Selected City ")
    print("[3] **Get Historical Data")
    print("[4] **Export something???")
    print("[q] Quit")
    print(f"Selected City: ", {selected_city})
    print("================================================")

    
def print_current_weather(current_weather_response):
    print("Current weather for:   ",current_weather_response.json()['location']['name'],)
    print('last_updated          =', current_weather_response.json()['current']['last_updated'])
    print('localtime             =', current_weather_response.json()['location']['localtime'])
    print('current condition     =',current_weather_response.json()['current']['condition']['text'])
    print('')
    print('Temps')
    print('temp c                =' , current_weather_response.json()['current']['temp_c'])
    print('feelslike c           =' , current_weather_response.json()['current']['feelslike_c'])
    print('')
    print('Precipitation')
    print('precip mm             =' , current_weather_response.json()['current']['precip_mm'])
    print('humidity              =' , current_weather_response.json()['current']['humidity'])
    print('cloud                 =' , current_weather_response.json()['current']['cloud'])
    print('pressure_mb           =' , current_weather_response.json()['current']['pressure_mb'])
    print('')
    print('Visability')
    print('vis km                =' , current_weather_response.json()['current']['vis_km'])
    print('')
    print('Wind')
    print('wind kph              =' , current_weather_response.json()['current']['wind_kph'])
    print('wind dir              =' , current_weather_response.json()['current']['wind_dir'])
    print('wind degree           =' , current_weather_response.json()['current']['wind_degree'])
    print('gust kph              =' , current_weather_response.json()['current']['gust_kph'])
    # print('' , current_weather_response.json()['current'][''])
    # print('' , current_weather_response.json()['current'][''])
    # print('' , current_weather_response.json()['current'][''])
    print("-----------------------------------------------")
    
    
# menu functions
# --------------------------
def menu():
    selected_city = "Brisbane"
    current_weather_response = None
    forecast_response = None 
    option = None 

    # info = None
    print_ui(selected_city, current_weather_response, option)
    
    if selected_city == None:
        print("No City selected")
        selected_city = input("Give City Name: ")
        print("")
        print("")
    if selected_city == "q":
         return
     
    while True:
        print_ui(selected_city, current_weather_response, option)
        option = input("Enter otion number here: ")
        print("")
        print("")
        match option:
            case "s":
                selected_city = input("Give New City Name: ")
                if selected_city == "q":
                    break
                current_weather_response = None 
                forecast_response = None 
                continue
            case '1':
                current_weather_response = get_current_weather_wapi(selected_city)
                write_response(current_weather_response)
                continue
            case '2':
                forecast_response = get_forecast_wapi(selected_city)
                write_response(forecast_response)
                continue
            case "q":
                break
            # case 3:
            
    print('thanks for using T1A3 Weather CLI')
    print('PROGRAM EXIT')
    
# get functions
# ------------------------------
def get_current_weather_wapi(selected_city):
    current_weather_response = requests.get(f"http://api.weatherapi.com/v1/current.json?q={selected_city}&key={api_key_wapi_caleb}")
    return current_weather_response

def get_forecast_wapi(selected_city):
    forecast_response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?q={selected_city}&key={api_key_wapi_caleb}")
    return forecast_response

# def get_current_weather_tmrio(selected_city):
#     selected_city = requests.get(f"https://api.tomorrow.io/v4/weather/forecast?location={selected_city}&apikey=1xKR2c5vCp2WQO6ci3o6FljhPuTkB2GP")

def write_response(response):
    file = open('rqsts.json', 'a')
    file.write(response.text)
    file.close()

menu()
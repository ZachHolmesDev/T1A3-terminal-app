import requests

def holder_ui():
    print("---Welcome to the the dvd surround sound test---")
    print("[0] Select City ")
    print("[1] Get current weather ")
    print("[2] **Display forecast")
    print("[3] **Get Historical Data")
    print("[4] **Export something???")
    print("[5] ")
    print(f"Selected City: ", {selected_city})
    
def ui_selector(num):
    match num:
        case 0:
            selected_city = input("Give City Name: ")
        case 1:
            get_current_weather_wapi
        case 2:
            
        case 3:
        

def get_current_weather_wapi():
    loc = input("Give City Name: ")
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?q={loc}&key={api_key_wapi_caleb}")
    # file = open('rqsts.json', 'a')
    # file.write(response.text)
    # file.close()
    print(response.json()['location']['name'])
    print(response.json()['current']['condition']['text'])
    print('temp_c =' , response.json()['current']['temp_c'])
    print('feelslike_c =' , response.json()['current']['feelslike_c'])

# def get_current_weather_tmrio():
#     loc = input("Give City Name: ")
#     response = requests.get(f"https://api.tomorrow.io/v4/weather/forecast?location={loc}&apikey=1xKR2c5vCp2WQO6ci3o6FljhPuTkB2GP")
#     # file = open('rqsts.json', 'a')
#     # file.write(response.text)
#     # file.close()
#     print(response.json()['location']['name'])
#     print(response.json()['current']['condition']['text'])
#     print('temp_c =' , response.json()['current']['temp_c'])
#     print('feelslike_c =' , response.json()['current']['feelslike_c'])
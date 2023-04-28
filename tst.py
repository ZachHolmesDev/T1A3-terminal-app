import requests

api_key_wapi_caleb = "3328658fef7c4737a1635629232204"
# Ui and menu functions
# --------------------------
def print_ui(selected_city, current_weather_response):
    print_menu(selected_city)
    if current_weather_response != None:
        print_current_weather(current_weather_response)

def print_menu(selected_city,):
    print("================================================")
    print("---Welcome to the the dvd surround sound test---")
    print("[0] Select City ")
    print("[1] Get current weather for Selected City ")
    print("[2] **Display forecast")
    print("[3] **Get Historical Data")
    print("[4] **Export something???")
    print("[q] Quit")
    print(f"Selected City: ", {selected_city})
    print("================================================")

    
def print_current_weather(current_weather_response):
    print("---",current_weather_response.json()['location']['name'],"--------------------------")
    print(current_weather_response.json()['current']['condition']['text'])
    print('temp_c =' , current_weather_response.json()['current']['temp_c'])
    print('feelslike_c =' , current_weather_response.json()['current']['feelslike_c'])
    print("-----------------------------------------------")
    
    

def menu():
    selected_city = None
    current_weather_response = None
    # info = None
    print_ui(selected_city, current_weather_response)
    
    if selected_city == None:
        print("No City selected")
        selected_city = input("Give City Name: ")
    if selected_city == "q":
         return
     
    while True:
        print_ui(selected_city, current_weather_response)
        num = input("Enter otion number here: ")
        match num:
            case "0":
                selected_city = input("Give New City Name: ")
                if selected_city == "q":
                    break
                current_weather_response = None
                continue
            case '1':
                current_weather_response = get_current_weather_wapi(selected_city)
                # print_current_weather(response)
                continue
            case "q":
                break
            
            
        # case 3:

# get functions
# ------------------------------
def get_current_weather_wapi(selected_city):
    current_weather_response = requests.get(f"http://api.weatherapi.com/v1/current.json?q={selected_city}&key={api_key_wapi_caleb}")
    # file = open('rqsts.json', 'a')
    # file.write(response.text)
    # file.close()
    return current_weather_response
    # print(response.json()['location']['name'])
    # print(response.json()['current']['condition']['text'])
    # print('temp_c =' , response.json()['current']['temp_c'])
    # print('feelslike_c =' , response.json()['current']['feelslike_c'])

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

menu()
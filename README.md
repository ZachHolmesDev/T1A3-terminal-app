# T1A3-terminal-app Zach Holmes

- [T1A3-terminal-app Zach Holmes](#t1a3-terminal-app-zach-holmes)
  - [Source Control Repository](#source-control-repository)
- [Description and Fetures](#description-and-fetures)
  - [Introduction](#introduction)
  - [Features](#features)
    - [1. Display weather information:](#1-display-weather-information)
    - [2. Export weather data](#2-export-weather-data)
    - [3. Select a new city](#3-select-a-new-city)
- [Implementation Plan](#implementation-plan)
    - [Trello board](#trello-board)
    - [Trello card](#trello-card)
- [Code Style](#code-style)

## Source Control Repository

Access the source control repository at [zholmes430/t1a3-terminal-app](https://github.com/zholmes430/t1a3-terminal-app).

# Description and Fetures

## Introduction

This project is a command-line interface (CLI) application that provides users with weather data, such as current weather, forecasts, and historical weather data. The program is written in Python and uses the [WeatherAPI.com](https://www.weatherapi.com/) service to fetch weather data.

The application has several functions to handle various tasks, such as fetching weather data, displaying the user interface, and exporting data. It utilizes the requests library to make API calls, and the os, json, and datetime libraries for other functionality.

The documentation i used for the WeatherAPI.com service can be found at [www.weatherapi.com/docs/](https://www.weatherapi.com/docs/).

note the api is limited to the free version as you can see in the image below:

![api limit](/README-images/wapi-price.png)

## Features

Here are the three main features of the application, along with the description of how they demonstrate the understanding of variables, loops, conditional control structures, and error handling:

  ### 1. Display weather information:

This feature allows the user to display various weather information for a selected city, including current weather, a forecast for the current day, and a 7-day weather history. The information is retrieved using API calls to the Weather API.

- Variables: Throughout the code, variables are used to store user input, API responses, and other data needed for processing. For example, the selected_city variable holds the city chosen by the user, and the current_weather_response variable holds the API response for the current weather.

- Loops: The print_history function uses a loop to iterate through the historical weather data and print it to the console. The loop iterates through the list of days in the response and extracts relevant information for each day.

- Conditional control structures: The main function uses a match statement, which is similar to a switch statement, to determine which action to perform based on the user's input. The case statements within the match statement handle the different actions the user can take.

- Error handling: The check_loc_valid function checks if the city entered by the user is valid by making an API call and handling the error response if it's not valid. If the city is invalid or there's a connection error, the function prints the appropriate error message and prompts the user to try again by pressing enter. It returns a tuple containing a boolean value (True if the city is valid, False otherwise) and an error message. The select_new_city function uses the check_loc_valid function and iterates until a valid city is entered or the user inputs "q" to quit.

### 2. Export weather data

The application allows the user to export the full weather data from the API in JSON format, with options to export the 24-hour forecast, 7-day history, or current weather data for the selected city.

- Variables: The export_response function uses variables such as selected_city, call_type, and export to store the data needed for exporting the JSON file.

- Conditional control structures: The function uses an if statement to determine which API call to make based on the call_type argument.

- Error handling: The function calls the get_ functions that will handle any errors that may occur during the API call in a simmilar way to the check_loc_valid function.

### 3. Select a new city

The user can change the selected city at any time to display and export weather data for a different city.

- Variables: The select_new_city function uses the new_city and city_is_valid variables to store user input and check if the city is valid.

- Loops: The function uses a while loop to repeatedly ask the user for a new city until a valid city is entered or the user quits.

- Conditional control structures: The if statement in the select_new_city function checks if the user input is valid or if the user wants to quit.

- Error handling: The check_loc_valid function checks if the city is valid and handles any errors that may occur during the API call.

# Implementation Plan

In this project, I used Trello as my project management platform to keep track of the main features and their respective tasks. Trello's card system allowed me to create a card for each feature and include checklists within the cards to ensure that all tasks are organized and easy to follow. Here's an outline of my implementation plan:

**1. Display current weather conditions, forecast, and historical data**  
    Checklist of tasks:
  - Design a clear and user-friendly output format
  - Create a function to parse and display current weather conditions
  - Create a function to parse and display weather forecast data
  - Create a function to parse and display historical weather data
  - Test each function to ensure correct data display

**2. Fetch weather data based on user's location or a specified city**   
   Checklist of tasks:
  - Register for an API key and research the API documentation
  - Install the requests package
  - Implement a function to fetch weather data using the API and user's
  - location or specified city
  - Test the function to ensure accurate weather data retrieval

**3. Export historical and/or predicted data to a file**  
    Checklist of tasks:
  - Determine the file format for export (e.g., CSV, JSON)
  - Implement a function to export the data to the chosen file format
  - Add a command-line option to trigger the export feature
  - Test the export functionality with different data sets
  - Document the export feature in the user guide

I've provided screenshots of the Trello board and a card, illustrating how the implementation plan was organized and tracked using Trello.

### Trello board
![trello board](/README-images/trello1.png)
### Trello card
![trello board](/README-images/trello2.png)


# Code Style

This project roughly adheres to the [PEP 8 style guide](https://peps.python.org/pep-0008/), which is the recommended style guide for Python code. 

Here are the main aspects of the code that follow the pep8 style 

- Indentation: The code uses 4 spaces per indentation level, which is consistent with PEP 8 recommendations.

- Naming conventions: Function and variable names are in lowercase with words separated by underscores, following the PEP 8 naming convention for functions and variables. For example: `check_loc_valid, selected_city, `and` error_msg.`

- Comments: The code includes descriptive comments and docstrings, which help explain the purpose and functionality of the code. This makes the code more readable and easier to understand.

Some aspects of the code that do not follow the pep8 style such as the blocks of print statements in the `print_ui()` functions. 

This is because the print statements are used to display information to the user, and it is more readable and to have all of the code for each print statment on one line.


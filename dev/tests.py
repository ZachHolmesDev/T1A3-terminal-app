from T1A3_Weather_CLI import get_current_weather_wapi, check_loc_valid


def test_get_current_weather_wapi():
    # Test case 1: Check if the function returns a valid response for a known city
    city1 = "New York"
    response1 = get_current_weather_wapi(city1)
    assert response1.status_code == 200, f"Failed to get current weather data for {city1}"

    # Test case 2: Check if the function returns the correct error for an unknown city
    city2 = "UnknownCity"
    response2 = get_current_weather_wapi(city2)
    assert "error" in response2.json(), f"Failed to return an error for an unknown city {city2}"

def test_check_loc_valid():
    # Test case 1: Check if the function returns True for a valid city
    city1 = "Los Angeles"
    result1 = check_loc_valid(city1)
    assert result1 == True, f"Failed to validate the city {city1} as valid"

    # Test case 2: Check if the function returns False for an invalid city
    city2 = "sdfgsdgs"
    result2 = check_loc_valid(city2)
    assert result2 == False, f"Failed to validate the city {city2} as invalid"

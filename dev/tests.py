from T1A3_Weather_CLI import get_current_weather_wapi, check_loc_valid, api_key_wapi_caleb


def test_get_current_weather_wapi():
    city = "New York"
    response = get_current_weather_wapi(city)
    assert response.status_code == 200, f"Failed to get the current weather for {city}"
    assert response.json()['location']['name'] == city, f"Invalid city name in the response"
    print(f"Test passed for get_current_weather_wapi() with city: {city}")

def test_check_loc_valid():
    valid_city = "London"
    invalid_city = "NotACity"
    
    assert check_loc_valid(valid_city) is True, f"Failed to validate city: {valid_city}"
    assert check_loc_valid(invalid_city) is False, f"Failed to invalidate city: {invalid_city}"
    print(f"Test passed for check_loc_valid() with cities: {valid_city} and {invalid_city}")

if __name__ == "__main__":
    test_get_current_weather_wapi()
    test_check_loc_valid()


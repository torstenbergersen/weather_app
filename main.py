import requests
import json

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('cod') == 404:
            print("City not found.")
            return
        
        file_name = f"{city}_weather.json"

        with open(file_name, 'w') as file:
            json.dump(data, file)
        
        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

api_key = '50958e31edcbbe4e49f8a733f4c117e8'
city = input("Enter city name: ")
weather = get_weather(api_key, city)

if weather.get('cod') != 200:
    print("Failed to get the weather data")
else:
    temperature = weather['main']['temp']
    description = weather['weather'][0]['description']
    print(f"Weather in {city}: {temperature} °C, {description}")
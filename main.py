import requests
import json

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    file_name = f"{city}_weather.json"

    with open(file_name, 'w') as file:
        json.dump(data, file)

api_key = '50958e31edcbbe4e49f8a733f4c117e8'
city = input("Enter city name: ")
weather = get_weather(api_key, city)


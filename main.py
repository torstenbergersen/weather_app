import requests
import json
import tkinter as tk
from tkinter import messagebox
from config import PRIVATE_API_KEY

def get_weather_gui(api_key, city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        weather = response.json()
        if weather.get('cod') != 200:
            messagebox.showerror("Error", "Failed to get the weather data.")
            return
        if weather.get('cod') == 404:
            messagebox.showerror("Error", "City not found.")
            return
        temperature = weather['main']['temp']
        description = weather['weather'][0]['description']
        weather_str = f"Weather in {city}: {temperature} °C, {description}"
        messagebox.showinfo("Weather", weather_str)
        file_name = f"{city}_weather.json"

        with open(file_name, 'w') as file:
            json.dump(weather, file)

    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("Error", f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        messagebox.showerror("Error", f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        messagebox.showerror("Error", f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        messagebox.showerror("Error", f"An error occurred: {req_err}")

api_key = PRIVATE_API_KEY

root = tk.Tk()
root.title("Weather App")

frame = tk.Frame(root)
frame.pack(padx=10,pady=10)

city_entry = tk.Entry(frame)
city_entry.pack(side=tk.LEFT, padx=(0, 10))
city_entry.insert(0, "Enter City")

get_weather_btn = tk.Button(frame, text="Get Weather", command=lambda: get_weather_gui(api_key, city_entry.get()))
get_weather_btn.pack(side=tk.LEFT)

root.mainloop()
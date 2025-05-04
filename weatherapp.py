import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "6a548b062158c655f488c867754c3045"

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }

        return weather
    except requests.exceptions.HTTPError as errh:
        messagebox.showerror("HTTP Error", str(errh))
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error", str(err))
    return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather = get_weather(city)
    if weather:
        result_label.config(
            text=f"City: {weather['city']}\n"
                 f"Temperature: {weather['temperature']} °C\n"
                 f"Weather: {weather['description'].title()}\n"
                 f"Humidity: {weather['humidity']}%\n"
                 f"Wind Speed: {weather['wind']} m/s"
        )

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")
root.resizable(False, False)

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack()

tk.Button(root, text="Get Weather", command=show_weather, font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
result_label.pack(pady=10)

root.mainloop()

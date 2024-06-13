import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city_name = city_entry.get()
    api_key = "ae39896132916a2be3997476fd304935"  # 여기에 OpenWeatherMap API 키를 입력하세요.
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    # API 요청
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = weather['description']
        
        weather_info = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {weather_description}"
        messagebox.showinfo("Weather Information", weather_info)
    else:
        error_message = response.json().get('message', 'City not found')
        messagebox.showerror("Error", f"Error: {error_message}. Please enter the city name correctly or try adding a country code (e.g., 'Seoul, KR').")

# GUI 설정
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name (e.g., 'Seoul' or 'Seoul, KR'):")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

root.mainloop()
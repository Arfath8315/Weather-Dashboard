import requests
import pandas as pd
import matplotlib.pyplot as plt
from forecast_plot import plot_forecast

API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_forecast(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['cod'] != "200":
        print("City not found.")
        return

    forecasts = data['list']
    df = pd.DataFrame([{
        'Date': item['dt_txt'],
        'Temperature': item['main']['temp'],
        'Humidity': item['main']['humidity'],
        'Weather': item['weather'][0]['main']
    } for item in forecasts])

    print(df[['Date', 'Temperature', 'Humidity', 'Weather']].head(10))  # Show sample
    plot_forecast(df)

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_forecast(city)

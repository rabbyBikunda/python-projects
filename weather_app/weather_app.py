import requests
import json
import time

API_KEY = ''
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    """Function to fetch weather data for a given city"""
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] != 200:
            print(f"Error fetching weather data for {city}. Error Code: {data['cod']}")
            return

        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        sunrise = time.strftime('%H:%M:%S', time.gmtime(data['sys']['sunrise'] - 3600))  # UTC to local time
        sunset = time.strftime('%H:%M:%S', time.gmtime(data['sys']['sunset'] - 3600))  # UTC to local time

        print(f"Weather Information for {city_name}, {country}:\n")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Weather: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")

    except Exception as e:
        print(f"Error occurred: {e}")

def get_forecast(city):
    """Function to display 5-day forecast for a given city"""
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] != '200':
            print(f"Error fetching forecast data for {city}. Error Code: {data['cod']}")
            return

        print(f"\n5-Day Weather Forecast for {city}:\n")
        for forecast in data['list'][::8]: 
            date_time = forecast['dt_txt']
            temperature = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            wind_speed = forecast['wind']['speed']
            print(f"{date_time}: {temperature}°C, {description.capitalize()}, Wind Speed: {wind_speed} m/s")

    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    """Main function to interact with the user"""
    print("Welcome to the Real-Time Weather App!\n")
    
    city = input("Enter the city name: ").strip()

    get_weather_data(city)

    show_forecast = input("\nWould you like to see a 5-day weather forecast? (y/n): ").strip().lower()
    if show_forecast == 'y':
        get_forecast(city)

if __name__ == "__main__":
    main()

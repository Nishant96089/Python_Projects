import requests

# Your API key from OpenWeatherMap
API_KEY = 'ec2000e25fc7a522e6e384e2fe39696e'

def get_weather(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

city_name = 'patna'  # Example city name
weather = get_weather(city_name)
if weather:
    print(f"Weather in {city_name}:")
    print(f"Description: {weather['description']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
else:
    print("Weather information not available. Please check your location.")

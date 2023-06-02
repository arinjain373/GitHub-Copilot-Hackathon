API_KEY = "688b11af9488862d495e4a6b60ff338a"
URL = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'

#write a code using URL and API_KEY to get the weather data of the input city
import requests
import json

city = input("Enter city name: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

response = requests.get(url)
data = response.json()

#write code to print the weather data into a beautiful format
print(f"City: {data['name']}")
print(f"Country: {data['sys']['country']}")
print(f"Temperature: {data['main']['temp']} Kelvin")
print(f"Feels like: {data['main']['feels_like']} Kelvin")
print(f"Max Temperature: {data['main']['temp_max']} Kelvin")
print(f"Min Temperature: {data['main']['temp_min']} Kelvin")
print(f"Humidity: {data['main']['humidity']} %")
print(f"Wind Speed: {data['wind']['speed']} m/s")
print(f"Wind Direction: {data['wind']['deg']} Degrees")
print(f"Cloudiness: {data['clouds']['all']} %")
print(f"Sunrise: {data['sys']['sunrise']} UTC")
print(f"Sunset: {data['sys']['sunset']} UTC")
print(f"Timezone: {data['timezone']} seconds")
print(f"Description: {data['weather'][0]['description']}")

import requests

API_KEY = "cb932c6248b5fe673aa76727cf7e7db2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"Looks like {weather} today")
    temperature = round((data['main']['temp'] - 273.15) + 32, 2)
    print(f"It is {temperature} degrees fahrenheit today")
    wind = round(data['wind']['speed']*2.23694, 2)
    print(f"Winds are gusting at {wind} mph")
    
else:
    print("An error occured. ")

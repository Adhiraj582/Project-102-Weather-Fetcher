import requests

API_KEY = "c71549f5c21f0a9ed4525031b4203b6d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: \n")
print('')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("The Weather is:", weather)
    print("The Temperature is:", temperature, "celsius.")
else:
    print("An error occurred.")

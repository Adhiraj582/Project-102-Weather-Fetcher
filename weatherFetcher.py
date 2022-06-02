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
    if(weather == 'sunny'):
        print('Its a great wearther outside!')
    elif(temperature < 10):
        print("It's too cold outside!")
    elif(temperature > 40):
        print("You probably shouldn't go out.")
    else:
        print("It's fine to go outside.")
        print('')
else:
    print("An error occurred.")

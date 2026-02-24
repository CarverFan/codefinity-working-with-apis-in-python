import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.85,
    "longitude": 2.35,
    "hourly": "temperature_2m"
}

def print_first_five_paris_temperatures():
    # Your implementation goes here
    response = requests.get(url, params=params)
    data = response.json()
    temps = data["hourly"]["temperature_2m"][:5]
    for t in temps:
        print(t)

print_first_five_paris_temperatures()

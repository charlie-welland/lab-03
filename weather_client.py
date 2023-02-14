import requests
from typing import Dict

# connect to a "real" API

URL = "https://api.openweathermap.org/data/2.5/weather"

#My custom API Key
API_KEY = "80fa30ff9b83897dd52f50522cea4350"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    main()

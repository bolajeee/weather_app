from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather(city = None):
    try:
        request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv('API_KEY')}&q={city}&units=metric"
    except KeyError:
        print("API key not found")
        return None
    
    get_curr_weather = requests.get(request_url).json()
    
    return get_curr_weather

if __name__ == "__main__":
    print(f"*****\nGet current weather data\n*****")

    input_city = input("Enter city name: ")

    if not bool(input_city.strip()):
        input_city = "London"
    
    weather_data = get_weather(input_city)

    pprint(f"\n{weather_data}\n")    
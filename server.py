from flask import Flask, request, render_template, redirect, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_weather(city):
    try:
        api_key = os.getenv("API_KEY")
        request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={api_key}&q={city}&units=metric"
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return redirect(url_for('index'))  
    # Redirect to home if no city is provided

    weather_data = get_weather(city)
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
from flask import Flask, request, render_template, redirect, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Get the API key from environment variable
API_KEY = os.getenv('OPENWEATHER_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
                return render_template('index.html', weather_data=weather_data)
            else:
                error_message = "City not found or API request failed."
                return render_template('index.html', error_message=error_message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
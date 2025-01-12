from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            api_key = 'your_api_key'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()
                return render_template('index.html', weather_data=weather_data)
            else:
                error_message = "City not found or API request failed."
                return render_template('index.html', error_message=error_message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

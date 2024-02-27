import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = os.environ.get('API_KEY')
RESERVAMOS_API_URL = os.environ.get('RESERVAMOS_API_URL')

"""
Args:
    city (str): Name of the city.

Returns:
    list: List of dictionaries containing weather data for the next 5 days,
          or None if the city is not found.
"""
def get_weather_data(city):
    response = requests.get(f'{RESERVAMOS_API_URL}?q={city}')
    data = response.json()

    if not data or data[0]['result_type'] != 'city':
        return None

    lat = data[0]['lat']
    lon = data[0]['long']

    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'

    response = requests.get(url)
    data = response.json()
    forecast = []
    for day in data['list']:
        forecast.append({
            'date': day['dt_txt'],
            'max_temp': day['main']['temp_max'],
            'min_temp': day['main']['temp_min'],
            'weather': day['weather'][0]['main']
        })

    return forecast

"""
Args:
    city (str): Name of the city.

Returns:
    JSON: JSON response containing the city name and its weather forecast,
           or a JSON error message with a 404 status code if city not found.
"""
@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    forecast = get_weather_data(city)
    if not forecast:
        return jsonify({'error': 'City not found'}), 404

    return jsonify({'city': city, 'forecast': forecast})


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests
import time

app = Flask(__name__)

API_KEY = "                     "

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', '')
    if not city:
        return jsonify({'error': 'Please enter a city name'}), 400

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        resp = requests.get(url, timeout=5)
        json_data = resp.json()

        if json_data.get('cod') != 200:
            return jsonify({'error': json_data.get('message', 'City not found')}), 404

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description'].title()
        icon = json_data['weather'][0]['icon']
        temp = round(json_data['main']['temp'] - 273.15, 1)
        feels_like = round(json_data['main']['feels_like'] - 273.15, 1)
        min_temp = round(json_data['main']['temp_min'] - 273.15, 1)
        max_temp = round(json_data['main']['temp_max'] - 273.15, 1)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        country = json_data['sys']['country']
        sunrise = time.strftime("%I:%M %p", time.gmtime(json_data['sys']['sunrise'] - 219800))
        sunset = time.strftime("%I:%M %p", time.gmtime(json_data['sys']['sunset'] - 219800))

        return jsonify({
            'city': city.title(),
            'country': country,
            'condition': condition,
            'description': description,
            'icon': icon,
            'temp': temp,
            'feels_like': feels_like,
            'min_temp': min_temp,
            'max_temp': max_temp,
            'pressure': pressure,
            'humidity': humidity,
            'wind': wind,
            'sunrise': sunrise,
            'sunset': sunset
        })
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out. Try again.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

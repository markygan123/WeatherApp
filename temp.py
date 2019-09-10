from flask import Flask, render_template, request
import datetime
import requests

app = Flask(__name__)

r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=30.242149&lon=-93.250710&appid=a8f7204f074ec2cb1dd88a845a06f881')
json_object = r.json()
current_weather_data = r.text

@app.route('/')
def index():
    now = datetime.datetime.now()
    current_date = now.strftime('%A %x')
    current_time = now.strftime('%I:%M:%S %p')
    access_weather = json_object['weather'][0]

    temp_k = float(json_object['main']['temp'])
    temp_f = round((temp_k - 273.15) * 1.8 + 32)
    temp_min_k = float(json_object['main']['temp_min'])
    temp_min_f = round((temp_min_k - 273.15) * 1.8 + 32)
    temp_max_k = float(json_object['main']['temp_max'])
    temp_max_f = round((temp_max_k - 273.15) * 1.8 + 32)
    humidity = json_object['main']['humidity']
    clouds = access_weather['description']
    current_weather = access_weather['main']

    heat_index = round(-42.379 + 2.04901523*(temp_f) + 10.14333127*(humidity) - .22475541*(temp_f)*(humidity) - .00683783*(temp_f)*(temp_f) - .05481717*(humidity)*(humidity) + .00122874*(temp_f)*(temp_f)*(humidity) + .00085282*(temp_f)*(humidity)*(humidity) - .00000199*(temp_f)*(temp_f)*(humidity)*(humidity))

    return render_template('index.html', date=current_date, time=current_time,temp=temp_f, min_temp=temp_min_f, max_temp=temp_max_f, humid=humidity, cloud=clouds, weather=current_weather, heat=heat_index, cwd=current_weather_data)

if __name__ == "__main__":
    app.run(debug=True)

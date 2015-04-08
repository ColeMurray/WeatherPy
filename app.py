#!venv/bin/python
from flask import Flask,render_template
from getWeather import getWeatherFromFile
app = Flask(__name__)
weather_data = getWeatherFromFile("SF.JSON")

for key,value in weather_data.iteritems():
    print value[0]
    print value[1]

@app.route('/')
def index():
    return render_template("index.html",weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)


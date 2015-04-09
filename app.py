#!venv/bin/python
from flask import Flask,render_template, request, redirect, url_for
from getWeather import getWeather_pub
app = Flask(__name__)
#weather_data = getWeatherFromFile("SF.JSON")

weather_data = getWeather_pub('Riverside')
for key,value in weather_data.iteritems():
    print value[0]
    print value[1]

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        query = request.form['city']
        global weather_data
        weather_data = getWeather_pub(query)
        return render_template("index.html",weather_data=weather_data, cityName=query)

    return render_template ("index.html", weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)


import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)
stations = pd.read_csv('data_small/stations.txt', skiprows=17, sep=',')[['STAID', 'STANAME']]


@app.route('/')
def home():
    return render_template('index.html', data=stations.to_html(index=False))


@app.route('/api/v1/<int:station>/<date>')
def get_weather(station, date):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        'station': station,
        'date': date,
        'temperature': temperature
    }


@app.route('/api/v1/<int:station>')
def get_station_data(station):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    data = df.to_dict(orient='records')
    return data


@app.route('/api/v1/yearly/<int:station>/<int:year>')
def get_temp_by_year(station, year):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    df['year'] = df['    DATE'].dt.year
    return df.loc[df['year'] == year].to_dict(orient='records')


if __name__ == '__main__':
    app.run(debug=True, port=8080)

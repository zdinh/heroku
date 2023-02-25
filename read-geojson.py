from flask import Flask
import geopandas as gpd

app = Flask(__name__)
@app.route('/')

def hello_world():
    print('hello')
    test=gpd.read_file('https://raw.githubusercontent.com/zdinh/heroku/main/palm_grid.geojson')
    return print('hello again', test.shape)
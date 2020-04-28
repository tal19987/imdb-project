from flask import Flask,request
from flask_cors import CORS
from functions.imdb_api import api_json
from multiprocessing import Pool
import json

app = Flask(__name__)
CORS(app)
data = {
    'movies': []
}
json_data = json.dumps(data)

@app.route('/')
def movies():
    movies = request.args.get('movie').split(',')
    p = Pool(processes=10)
    data["movies"] = p.map(api_json,movies)
    p.close()
    return data

if __name__ == '__main__':
    app.run(port=8080)
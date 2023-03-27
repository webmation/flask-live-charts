import json
from time import time
from random import random
from flask import Flask, render_template, make_response, request
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    # Create a PHP array and echo it as JSON
    res = requests.get('http://125.141.107.23:8080/api/getObsData?obsID=OBS-0001')
    #res = requests.get('http://192.168.0.100:8080/api/getObsData?obsID=OBS-0001')
    #res = requests.get('http://192.168.0.138:8080/api/jsondata')
    json_Object = json.loads(res.text)
    print(f'Get Request Response : {res.text}')

    jsonArray = json_Object.get("obs_data")
    
    a = int(jsonArray[0]['DATETIME'])
    b = float(jsonArray[0]['DATA'])
    print(f'Get Request Response : {a} : {b}')

    data = [((int(jsonArray[0]['DATETIME']) + 0) * 1000 , float(jsonArray[0]['DATA'])),
            ((int(jsonArray[1]['DATETIME']) + 0) * 1000 , float(jsonArray[1]['DATA'])),
            ((int(jsonArray[2]['DATETIME']) + 0) * 1000 , float(jsonArray[2]['DATA'])),
            ((int(jsonArray[3]['DATETIME']) + 0) * 1000 , float(jsonArray[3]['DATA'])) ]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

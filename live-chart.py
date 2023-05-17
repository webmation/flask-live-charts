import json
from time import time
from random import random
from flask import Flask, render_template, make_response, request
import requests


app = Flask(__name__)


@app.route('/')
def obs():
    #return render_template('index.html', data='test')
    return render_template('index2.html', data='test')

@app.route('/obs02')
def obs2():
    return render_template('index2.html', data='test')

@app.route('/obs03')
def obs3():
    return render_template('index3.html', data='test')

@app.route('/obs04')
def obs4():
    return render_template('index4.html', data='test')

@app.route('/obs-0001')
def live_data():
    res = requests.get('http://125.141.107.23:8080/api/getObsData?obsID=OBS-0001')
    json_Object = json.loads(res.text)
    print(f'Get Request Response : {res.text}')

    jsonArray = json_Object.get("obs_data")
    a = int(jsonArray[0]['DATETIME'])
    b = float(jsonArray[0]['DATA'])
    print(f'Get obs-0001 Request Response : {a} : {b}')

    data = [((int(jsonArray[0]['DATETIME']) + 0) * 1000 , float(jsonArray[0]['DATA'])),
            ((int(jsonArray[1]['DATETIME']) + 0) * 1000 , float(jsonArray[1]['DATA'])),
            ((int(jsonArray[2]['DATETIME']) + 0) * 1000 , float(jsonArray[2]['DATA'])),
            ((int(jsonArray[3]['DATETIME']) + 0) * 1000 , float(jsonArray[3]['DATA'])),
            ((int(jsonArray[4]['DATETIME']) + 0) * 1000 , float(jsonArray[4]['DATA'])),
            ((int(jsonArray[5]['DATETIME']) + 0) * 1000 , float(jsonArray[5]['DATA'])),
            ((int(jsonArray[6]['DATETIME']) + 0) * 1000 , float(jsonArray[6]['DATA'])) ]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/obs-0002')
def live_data2():
    res = requests.get('http://125.141.107.23:8080/api/getObsData?obsID=OBS-0002')
    json_Object = json.loads(res.text)
    print(f'Get Request Response : {res.text}')

    jsonArray = json_Object.get("obs_data")
    a = int(jsonArray[0]['DATETIME'])
    b = float(jsonArray[0]['DATA'])
    print(f'Get obs-0002 Request Response : {a} : {b}')

    data = [((int(jsonArray[0]['DATETIME']) + 0) * 1000 , float(jsonArray[0]['DATA'])),
            ((int(jsonArray[1]['DATETIME']) + 0) * 1000 , float(jsonArray[1]['DATA'])),
            ((int(jsonArray[2]['DATETIME']) + 0) * 1000 , float(jsonArray[2]['DATA'])),
            ((int(jsonArray[3]['DATETIME']) + 0) * 1000 , float(jsonArray[3]['DATA'])),
            ((int(jsonArray[4]['DATETIME']) + 0) * 1000 , float(jsonArray[4]['DATA'])),
            ((int(jsonArray[5]['DATETIME']) + 0) * 1000 , float(jsonArray[5]['DATA'])),
            ((int(jsonArray[6]['DATETIME']) + 0) * 1000 , float(jsonArray[6]['DATA'])),
            ((int(jsonArray[7]['DATETIME']) + 0) * 1000 , float(jsonArray[7]['DATA'])) ]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/obs-0003')
def live_data3():
    res = requests.get('http://125.141.107.23:8080/api/getObsData?obsID=OBS-0003')
    json_Object = json.loads(res.text)
    print(f'Get Request Response : {res.text}')

    jsonArray = json_Object.get("obs_data")
    a = int(jsonArray[0]['DATETIME'])
    b = float(jsonArray[0]['DATA'])
    print(f'Get obs-0003 Request Response : {a} : {b}')

    data = [((int(jsonArray[0]['DATETIME']) + 0) * 1000 , float(jsonArray[0]['DATA'])),
            ((int(jsonArray[1]['DATETIME']) + 0) * 1000 , float(jsonArray[1]['DATA'])),
            ((int(jsonArray[2]['DATETIME']) + 0) * 1000 , float(jsonArray[2]['DATA'])),
            ((int(jsonArray[3]['DATETIME']) + 0) * 1000 , float(jsonArray[3]['DATA'])),
            ((int(jsonArray[4]['DATETIME']) + 0) * 1000 , float(jsonArray[4]['DATA'])),
            ((int(jsonArray[5]['DATETIME']) + 0) * 1000 , float(jsonArray[5]['DATA'])),
            ((int(jsonArray[6]['DATETIME']) + 0) * 1000 , float(jsonArray[6]['DATA'])) ]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

@app.route('/obs-0004')
def live_data4():
    res = requests.get('http://125.141.107.23:8080/api/getObsData?obsID=OBS-0004')
    json_Object = json.loads(res.text)
    print(f'Get Request Response : {res.text}')

    jsonArray = json_Object.get("obs_data")
    a = int(jsonArray[0]['DATETIME'])
    b = float(jsonArray[0]['DATA'])
    print(f'Get obs-0002 Request Response : {a} : {b}')

    data = [((int(jsonArray[0]['DATETIME']) + 0) * 1000 , float(jsonArray[0]['DATA'])),
            ((int(jsonArray[1]['DATETIME']) + 0) * 1000 , float(jsonArray[1]['DATA'])),
            ((int(jsonArray[2]['DATETIME']) + 0) * 1000 , float(jsonArray[2]['DATA'])),
            ((int(jsonArray[3]['DATETIME']) + 0) * 1000 , float(jsonArray[3]['DATA'])),
            ((int(jsonArray[4]['DATETIME']) + 0) * 1000 , float(jsonArray[4]['DATA'])),
            ((int(jsonArray[5]['DATETIME']) + 0) * 1000 , float(jsonArray[5]['DATA'])),
            ((int(jsonArray[6]['DATETIME']) + 0) * 1000 , float(jsonArray[6]['DATA'])),
            ((int(jsonArray[7]['DATETIME']) + 0) * 1000 , float(jsonArray[7]['DATA'])) ]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

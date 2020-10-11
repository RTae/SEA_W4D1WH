from flask import Flask, request
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
CORS(app)

@app.route('/')
def helloworld():
    return "Helloword"

@app.route('/area', methods = ['GET'] )
@cross_origin()
def area():
    w = float(request.values['w'])
    h = float(request.values['h'])
    return str(w*h)

@app.route('/bmi', methods = ['GET'] )
@cross_origin()
def bmi():
    weight = float(request.values['weight'])
    height = float(request.values['height'])
    height = height/100
    bmi  = str(round(weight/(height**2), 3))
    return 'Your BMI is ' + bmi + ' kg/m^2'
'''
@app.route('/iris', methods = ['GET'] )
@cross_origin()
def prediction_model_iris():
    req = request.values['param']
    target = prediction_model(req)
    return target
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request
from flask_cors import CORS
from modelo import *

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def get_cita():
    return "esto es un get *****"

@app.route('/submit', methods=['POST'])
def new_cita():
    data= request.get_json()
    print ('**newcita', data)
    post_cita(data)
    return "Formular trimis cu succes"

app.run(debug=True)
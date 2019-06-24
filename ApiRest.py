import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/getalert', methods=['GET'])
def getALert():
    data = request.data.roomCode

    
    
    return 'True' 

@app.route('/example', methods=['POST'])
def example():
    print(request.data)

app.run(host='0.0.0.0',port=80)


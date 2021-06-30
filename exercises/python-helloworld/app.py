import logging
from flask import Flask
from flask import json

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='app.log', encoding='utf-8', level=logging.DEBUG)
@app.route("/")
def hello():
    logging.debug("home endpoint was reached")
    return "Hello World!"

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response
if __name__ == "__main__":
    app.run(host='0.0.0.0')

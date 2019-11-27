import flask
from flask import request, Response
import os
import json

app = flask.Flask(__name__)


@app.route('/', methods=["POST"])
def index():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    token = str(data['challenge'])
    return Response(token, mimetype='text/plane')


@app.route('/get')
def get():
    return "Hello, this is get!"


port = os.getenv('VCAP_APP_PORT', '8000')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)

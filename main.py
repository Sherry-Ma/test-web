from flask import Flask, jsonify, make_response
import datetime

app = Flask(__name__)

@app.route('/')
def example():
    # here to change headers
    response_text = 'Hello, World!'
    response = make_response(response_text, 200)
    response.headers['Content-Length'] = len(response_text.encode('utf-8'))
    response.headers['Cache-Control'] = 'max-age=360000'
    return response


if __name__ == '__main__':
    app.run()

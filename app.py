from datetime import datetime

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return f'Hello World! {datetime.now()} version 17.02.2025 v2  sdasdas '

@app.route('/a1')
def a1():
    return f'a1 route now {datetime.now()} version 17.02.2025'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

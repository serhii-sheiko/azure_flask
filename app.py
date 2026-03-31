from datetime import datetime

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return f'Hello World! {datetime.now()} version -> 31.03.2026 3'

@app.route('/a1')
def a1():
    print("a1")
    return f'a1 route now {datetime.now()} version 31.03.2026'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

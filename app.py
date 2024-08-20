from datetime import datetime

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return f'!909890 Hello World! {datetime.now()} version 21.03.2024'

@app.route('/a1')
def a1():
    return f'a1 route now {datetime.now()} version 20.08.2024'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

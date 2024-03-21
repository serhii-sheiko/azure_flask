from datetime import datetime

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return f'Hello World! {datetime.now()} version 21.03.2024'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

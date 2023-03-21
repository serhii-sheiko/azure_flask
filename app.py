from datetime import datetime

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return f'Hello World! {datetime.now()}'

if __name__ == '__main__':
    app.run()

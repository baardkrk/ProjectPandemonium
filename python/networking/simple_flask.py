import time
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    time.sleep(2)
    return 'hello, world'


@app.route('/exception')
def return_exception():
    time.sleep(1)
    return '', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)


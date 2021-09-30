from flask import Flask
from datetime import datetime
import time 

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def time():
    time = datetime.now(time.timezone("US/Eastern"))
    return time.strftime("%Y : %M : %H : %S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)

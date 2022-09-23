# web.py

from flask import Flask, request
from ping3 import ping

app = Flask(__name__)

@app.route('/')
def pingback():
    ip_addr = request.remote_addr
    latency = ping(ip_addr, unit='ms') 

    return '<h1> Your ping is: ' + "{:.3f}".format(latency) + 'ms!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    
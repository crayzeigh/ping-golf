# web.py

from flask import Flask, request
from ping3 import ping
import pandas as pd

app = Flask(__name__)

def get_score():
    ip_addr = request.remote_addr
    latency = ping(ip_addr, unit='ms') 
    score = str(round(latency ,3))
    return score

def get_agent():
    agent = str(request.user_agent)
    return agent

@app.route('/', methods = ['POST'])
def pingback():
    score = get_score()
    agent = get_agent()
    entry = score + "," + agent + "\n"
    
    with open("scoreboard.csv", "a") as f:
        f.write(entry)

    return agent + ", is " + score + "ms from the target."
    
@app.route('/', methods = ['GET'])
def app_test():
    score = get_score()
    agent = get_agent()
    
    return "<h1>Your Ping is: " + score + "ms</h1>\n\n<h3>User agent: \n" + agent + "</h3>\n"
    
@app.route('/scoreboard')
def scoreboard():
    columns = ["ping","agent"]
    df = pd.read_csv("scoreboard.csv",usecols=columns)

    df = df.sort_values("ping")
    scoreboard = df.to_html(columns=columns)

    return scoreboard

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

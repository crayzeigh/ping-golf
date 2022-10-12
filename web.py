# web.py

from flask import Flask, request, render_template
from ping3 import ping
import pandas.io.sql as psql
import psycopg2
import os

app = Flask(__name__)
con = psycopg2.connect(os.environ["DATABASE_URL"])

def get_score():
    ip_addr = request.remote_addr
    latency = ping(ip_addr, unit='ms') 
    agent = str(request.user_agent)

    if not latency:
        score = "XX"
    else:
        score = round(latency ,3)

    return score, agent

@app.route('/', methods = ['POST'])
def pingback():
    score, agent = get_score()
    
    try:
        with con.cursor() as cur:
            cur.execute(f"INSERT INTO scoreboard (score,name) VALUES ({score},'{agent}');")
            con.commit()
        status = "Entry completed successfully"
    except:
        print ("Error on INSERT!")
        status = "Error updating database"

    return f"{status}.\n{agent} is {score}ms away.\n"
    
@app.route('/', methods = ['GET'])
def app_test():
    score, agent = get_score()

    return f"<h1>Your Ping is: {score}ms</h1>\n\n<h3>User agent: \n{agent}</h3>\n"
    
@app.route('/scoreboard')
def scoreboard():
    sql = "SELECT * FROM scoreboard;"
    scores_df = psql.read_sql_query(sql, con)
    scores_df.sort_values(by=['score'], ascending=[True], inplace=True)
    scores_df.rename(columns={'score':'Ping in ms', 'name':'Name'}, inplace=True)
    scoreboard = scores_df.to_html(index=False)

    return render_template('scoreboard.html', scoreboard=scoreboard)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

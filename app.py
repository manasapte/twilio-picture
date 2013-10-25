from flask import Flask, render_template, request, Response, session, abort, jsonify
import json
import redis

app = Flask(__name__)
app.config['DEBUG'] = True

r = redis.StrictRedis(host='localhost',port=6379,db=0)

@app.route('/twipic')
def index():
    id = r.incr('sessionid')
    return render_template('picture.html',id=id) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)

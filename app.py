from flask import Flask, render_template, request, Response, session, abort, jsonify
from twilio.rest import TwilioRestClient
import json
import redis

app = Flask(__name__)
app.config['DEBUG'] = True

r = redis.StrictRedis(host='localhost',port=6379,db=0)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC2dd3b641addfcbf5e5cc2af60a03fb73"
auth_token  = "041d85969d3e7df0ba2046ea977a825e"
client = TwilioRestClient(account_sid, auth_token)

@app.route('/twipic')
def index():
    return render_template('picture.html') 

@app.route('/text',methods=['POST'])
def text():
  id = r.incr('sessionid')
  ph = request.form.get('phone')  
  r.set(ph,id)
  sms = client.sms.messages.create(body="Enter the following code on the site:"+str(id),
    to="+16786444097",
    from_="+19252320999")  
  

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)

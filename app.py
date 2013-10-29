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

@app.route('/send',methods=['POST'])
def send():
  img = request.form.get('base64img')
  ph = request.form.get('phone')
  print "request phone: "+ph
  code = request.form.get('code')
  print "request code: "+code
  print "from redis: "+r.get(ph)
  if r.get(ph) == code:
    fh = open("/static/"+str(ph)+".png", "wb")
    fh.write(imgData.decode('base64'))
    fh.close()
    #send MMS
    return json.dumps({'success':True}) 
  return json.dumps({'success':False}) 

@app.route('/text',methods=['POST'])
def text():
  id = r.incr('sessionid')
  print "form: "+str(request.form)
  ph = request.form.get('phone')  
  r.set(ph,id)
  sms = client.sms.messages.create(body="Enter the following code on the site:"+str(id),
    to=ph,
    from_="+19252320999")
  return json.dumps({'phone':ph}) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)

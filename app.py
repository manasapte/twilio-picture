from flask import Flask, render_template, request, Response, session, abort, jsonify
from socketio_namespaces import PlayersNamespace
from socketio import socketio_manage
import json
import redis

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/tetris')
def index():
    return render_template('tetris.html') 

@app.route('/game',methods=['GET'])
def game():
  print('hello called')
  return Response(render_template('login.xml',mimetype='text/xml'))



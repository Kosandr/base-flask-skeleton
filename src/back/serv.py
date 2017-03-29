from flask import Flask, session, redirect, url_for, escape, request, render_template, send_from_directory
#from flask_session import Session

import user_agents, json
import os.path, sqlite3
#from user_acc.atomicid import ObjId
#from user_acc import Perm, UserPermissions

app = Flask(__name__, template_folder='../templates')

def mobile(func):
   def func_wrapper(*args, **kwargs):
      agent_str = request.headers.get('User-Agent')
      agent_parsed = user_agents.parse(agent_str)
      is_mobile = agent_parsed.is_mobile
      return func(is_mobile=agent_parsed.is_mobile, *args, **kwargs)
   return func_wrapper

def read_config():
   with open('conf.json', 'r') as f:
      conf_str = f.read()
      json_conf = json.loads(conf_str)
      return json_conf

conf = read_config()

app.secret_key = conf['SECRET_KEY']
#SESSION_TYPE = 'redis'
#app.config['SESSION_TYPE'] = SESSION_TYPE
#Session(app)

APP_ROOT = conf['APP_ROOT']
DOMAIN = conf['DOMAIN']
STATIC_NGINX = conf['STATIC_NGINX']

def get_conf():
   return {
      'root_path' : APP_ROOT,
      'static_path' : STATIC_NGINX
   }

@app.route(APP_ROOT, strict_slashes=False)
@app.route(APP_ROOT + 'index', strict_slashes=False)
@app.route(APP_ROOT + 'index.html', strict_slashes=False)
@mobile
def index(is_mobile):
   #print(is_mobile)
   return render_template('index.html', conf=get_conf())

@app.route('/<path:path>')
def catch_all(path):
   return render_template('sorry.html')






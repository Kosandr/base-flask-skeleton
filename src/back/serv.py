from flask import Flask, session, redirect, url_for, escape, request, render_template, send_from_directory
#from flask_session import Session

import user_agents, json
import os.path, sqlite3
#from user_acc.atomicid import ObjId
#from user_acc import Perm, UserPermissions

import helpers
from helpers import mobile, is_mobile_agent, read_config



app = Flask(__name__, template_folder='../templates')

conf = read_config()

app.secret_key = conf['SECRET_KEY']
#SESSION_TYPE = 'redis'
#app.config['SESSION_TYPE'] = SESSION_TYPE
#Session(app)

APP_ROOT = conf['APP_ROOT']
DOMAIN = conf['DOMAIN']
STATIC_NGINX = conf['STATIC_NGINX']
SITE_NAME = conf['SITE_NAME']

def get_conf():
   from utiltools import shellutils

   need_flush_cache = True
   cache_flush_str = ''
   if need_flush_cache:
      random = shellutils.rand_str(3)
      cache_flush_str = '?x=' + random

   site_root_path = DOMAIN + APP_ROOT

   return {
      'root_path' : site_root_path,
      'static_path' : STATIC_NGINX,
      'random' : shellutils.rand_str(3),
      'cache_flush' : cache_flush_str,
      'is_mobile' : is_mobile_agent(),
      'site_name' : SITE_NAME,
      'active_page' : activePage
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






import json, user_agents
from flask import request

def is_mobile_agent():
   agent_str = request.headers.get('User-Agent')
   agent_parsed = user_agents.parse(agent_str)
   return agent_parsed.is_mobile

def mobile(func):
   def func_wrapper(*args, **kwargs):
      return func(is_mobile=is_mobile_agent(), *args, **kwargs)
   return func_wrapper

def read_config():
   with open('conf.json', 'r') as f:
      conf_str = f.read()
      json_conf = json.loads(conf_str)
   return json_conf


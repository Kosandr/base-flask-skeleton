#!/bin/bash

apt install nginx-extras

pip3 install gunicorn Flask
pip3 install user_agents


mkdir -p /sec/{nginx_confs,logs}

#!/bin/bash

pid_dir='tmp/pids'
mkdir -p $pid_dir

num_workers=2
ip=127.0.0.1
port=4829

#cd src/back;
gunicorn --pythonpath src/back serv:app --workers=$num_workers -b $ip:$port &

latest=$!
echo $latest > $pid_dir/guni.pid
echo "starting guni proc: $latest"

####

pywatch ./src/sass scss ./watchers/watchsass.py -d &
latest=$!
echo $latest > $pid_dir/sasswatch.pid

pywatch ./src/jsx jsx "./watchers/watchjsx.py %s" -p &
latest=$!
echo $latest > $pid_dir/jsxwatch.pid


#./watchers/pywatch.py ./src/back "py|html" "kill -HUP $latest" -d
pywatch ./src/back "py|html" "kill -HUP `cat $pid_dir/guni.pid`" -d &
pywatch ./src/templates "py|html" "kill -HUP `cat $pid_dir/guni.pid`" -d

kill -9 `cat $pid_dir/jsxwatch.pid` `cat $pid_dir/sasswatch.pid`



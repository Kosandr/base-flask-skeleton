#!/bin/bash

#~/orgs/Kosandr/base-flask-skeleton/run.sh /sec/sites/<flask-project>/ 5016
#./run.sh . port


loc=$1

pid_dir="$loc/tmp/pids"
mkdir -p $pid_dir

num_workers=2
ip=127.0.0.1
#port=4829
port=$2

#cd src/back;
gunicorn -k flask_sockets.worker --pythonpath $loc/src/back serv:app --workers=$num_workers -b $ip:$port &

latest=$!
echo $latest > $pid_dir/guni.pid
echo "starting guni proc: $latest"

####

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "KK: $DIR"

#pywatch $loc/src/sass scss $loc/watchers/watchsass.py -d &
pywatch $loc/src/sass scss $DIR/watchers/watchsass.py -d &
latest=$!
echo $latest > $pid_dir/sasswatch.pid

#pywatch $loc/src/jsx jsx "$loc/watchers/watchjsx.py %s" -p &
pywatch $loc/src/jsx jsx "$DIR/watchers/watchjsx.py %s" -p &
latest=$!
echo $latest > $pid_dir/jsxwatch.pid


#./watchers/pywatch.py ./src/back "py|html" "kill -HUP $latest" -d
pywatch $loc/src/back "py|html" "kill -HUP `cat $pid_dir/guni.pid`" -d &
pywatch $loc/src/templates "py|html" "kill -HUP `cat $pid_dir/guni.pid`" -d

echo 'exiting'
kill -9 `cat $pid_dir/jsxwatch.pid` `cat $pid_dir/sasswatch.pid` `cat $pid_dir/guni.pid`




SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

echo $DIR
$DIR/kill_curr_dir.sh $1


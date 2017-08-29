#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR
echo "pull-and-run.sh: $DIR"

git pull origin master
./run.sh

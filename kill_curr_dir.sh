#!/bin/bash


#using pts/46, but can use this instead:
#ps ax | grep $$ | awk '{ print $2 }'
#http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x721.html


###latest working: sudo kill -9 `ps -e | grep guni | grep "pts/46" | awk '{ print $1 }' | tr '\n' ' '`

#kill pywatch
#ps -e | grep pywatch | grep "pts/46" | awk '{ print $1 }' | tr '\n' ' '



kill `lsof . | grep pywatch | awk '{ print $2}' | tr '\n' ' ' `
kill `lsof . | grep gunicorn | awk '{ print $2}' | tr '\n' ' ' `

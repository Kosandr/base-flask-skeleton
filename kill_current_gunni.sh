#!/bin/bash


#using pts/46, but can use this instead:
#ps ax | grep $$ | awk '{ print $2 }'
#http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x721.html


sudo kill -9 `ps -e | grep guni | grep "pts/46" | awk '{ print $1 }' | tr '\n' ' '`

#kill pywatch
#ps -e | grep pywatch | grep "pts/46" | awk '{ print $1 }' | tr '\n' ' '

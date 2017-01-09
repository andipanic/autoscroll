#!/bin/bash

#
# Starts autoscroll.py or stops it if another autoscroll process
#   is currently running.
# 

SCROLL=$(ps aux | grep [au]toscroll.py | awk {'print $2'})

if [[ $SCROLL ]]; then
    kill -9 $SCROLL
else
    autoscroll.py
fi

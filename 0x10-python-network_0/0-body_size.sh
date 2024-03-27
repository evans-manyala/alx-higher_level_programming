#!/bin/bash

curl -sI "$1" | grep -i Content-Length | awk '{print "The response size for",$1,"is:",$2,"bytes"}' || echo "Error: Could not retrieve response size for the URL."

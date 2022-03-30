#!/bin/bash

app_name=emanon

# Clear the port before beginning
sh ./clearport.sh

# Delete previous Docker image if any
docker stop $app_name
docker rm $app_name

# Build Docker image
docker build -t $app_name .

# Run Docker image
docker run --name $app_name $appname
#!/bin/sh

[ ! -n "$1" ] && echo "You must specify an install directory." && exit

#copy cgi scripts to install dir
#TODO: put surveys.py somewhere else
sudo cp submit survey surveys.py $1

#TODO: setup script for creating survey tables

#make survey data dir
sudo mkdir -p /etc/sws/surveys

#make application data dir
sudo mkdir -p /usr/share/sws

#make survey sql database
sudo mysql -e "CREATE DATABASE sws;"

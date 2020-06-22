#!/bin/sh

[ ! -n "$1" ] && echo "You must specify an install directory." && exit

#make install dir
sudo mkdir -p $1
sudo mkdir -p $1/cgi

#copy cgi scripts to install dir
#TODO: put surveys.py somewhere else
sudo cp -r sws.css cgi/ fonts/ $1

#TODO: setup script for creating survey tables

#make survey data dir
sudo mkdir -p /etc/sws/surveys

#make application data dir
sudo mkdir -p /usr/share/sws

#copy files to app data dir
sudo cp -r html/ /usr/share/sws

#make survey sql database
sudo mysql -e "CREATE DATABASE sws;"

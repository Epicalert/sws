#!/bin/sh

[ ! -n "$1" ] && echo "You must specify an install directory." && exit

sudo cp submit survey surveys.py $1

#TODO: setup script for creating survey tables

sudo mysql -e "CREATE DATABASE sws;"

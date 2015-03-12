#!/bin/bash

cd /root/starl

nohup python manage.py runserver 0.0.0.0:80 &>> log.txt &

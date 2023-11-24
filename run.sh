#! /bin/bash

sudo docker build --tag trello-django .
sudo docker run --publish 8000:8000 trello-django
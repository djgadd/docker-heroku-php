#!/bin/bash

gem install foreman
useradd -m heroku
chown -R heroku /app/.heroku

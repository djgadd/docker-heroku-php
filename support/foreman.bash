#!/bin/bash

export HOME=/app

# Load in the environment
. /etc/profile

# Run foreman
foreman start --root /var/www

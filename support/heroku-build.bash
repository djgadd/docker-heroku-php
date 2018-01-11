#!/bin/bash

chmod +x /app/support/heroku.bash
chmod +x /app/support/foreman.bash
mkdir -p /tmp/buildpack/php /tmp/build_cache /tmp/env
python /app/support/strip-composer-packages.py /app/composer.lock /app/composer.json
curl https://codon-buildpacks.s3.amazonaws.com/buildpacks/heroku/php.tgz | tar --warning=none -xz -C /tmp/buildpack/php
STACK=heroku-16 /tmp/buildpack/php/bin/compile /app /tmp/build_cache /tmp/env

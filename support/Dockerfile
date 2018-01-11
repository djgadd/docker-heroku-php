# See https://github.com/heroku/stack-images/issues/56

FROM heroku/heroku:16-build as heroku-build
COPY . /app
WORKDIR /app
RUN chmod +x /app/support/heroku-build.bash
RUN /app/support/heroku-build.bash
# RUN chmod +x /app/support/docker.init.sh
# RUN mkdir -p /tmp/buildpack/php /tmp/build_cache /tmp/env
# RUN curl https://codon-buildpacks.s3.amazonaws.com/buildpacks/heroku/php.tgz | tar --warning=none -xz -C /tmp/buildpack/php
# RUN STACK=heroku-16 /tmp/buildpack/php/bin/compile /app /tmp/build_cache /tmp/env

FROM heroku/heroku:16
COPY --from=heroku-build /app /app
COPY --from=heroku-build /app/.profile.d /etc/profile.d
RUN /app/support/heroku.bash
ENV HOME /app
USER heroku
SHELL ["/bin/bash", "-l"]
EXPOSE 5000
VOLUME /var/www
ENTRYPOINT ["/app/support/foreman.bash"]

# Install foreman so we can run our Procfile
# RUN gem install foreman
#
# # Create a Heroku user and set it as the user to login as
# RUN useradd -m heroku
# RUN chown -R heroku /app/.heroku
# ENV HOME /app
# USER heroku
#
# # Set our sell to log us in
# SHELL ["/bin/bash", "-l"]
#
# # Expose our ports and volume
# EXPOSE 5000
# VOLUME /app/www
#
# # Boot things up
# ENTRYPOINT ["/app/support/docker.init.sh"]

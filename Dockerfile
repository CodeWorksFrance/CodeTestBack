# Source image
FROM python:3.8-slim-buster

# Copy the requirement dependencies to install
COPY ./requirements.txt /app/requirements.txt

# Define a working directory
WORKDIR /app

# Install production dependencies.
RUN set -ex; \
    pip install -r requirements.txt; \
    pip install gunicorn

# Copy the app.py file to the container
COPY ./ /app

# Launch app
ENTRYPOINT ["strawberry", "server", "app"]

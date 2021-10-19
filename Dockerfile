# Get image from docker hub
FROM tiangolo/meinheld-gunicorn-flask:python3.9

# If you need to install any apt package you can do it here e.g:
# RUN apt-get update && apt-get install -y pandoc

# Copy the requirements file into the container.
# The requirements file is a list of all pip packages we need.
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
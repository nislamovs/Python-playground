# set base image (host OS)
FROM python:2.7.17

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

EXPOSE 5000

VOLUME /dev/ttyUSB0:/dev/ttyUSB0

# command to run on container start
#CMD [ "python", "./uart_example.py" ]./
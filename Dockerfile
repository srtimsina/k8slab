# set base image
FROM frolvlad/alpine-python3:latest

# set the working directory in the container
WORKDIR /opt

# copy the dependencies file to the working directory
COPY scripts/ .

# install dependencies
RUN python -m pip install -r requirements.txt
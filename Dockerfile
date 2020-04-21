# Getting base image as Ubuntu
FROM ubuntu:14.04


# author name
MAINTAINER siddharth pal <siddharthasinghbisen96@gmail.com>


# setup ubuntu by updating and the install software-properties-common which lets us add PPA (Personal Package Archive)rep
RUN apt-get update && apt-get install -y \
    software-properties-common 


# now to install python
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    python3-pip


# create a directory in the container
WORKDIR /energyconsumption


# to copy all the files from the current directory to container
COPY . /energyconsumption

COPY stable-requirements.txt /energyconsumption/stable-requirements.txt

RUN pip3 install setuptools-39.1.0 -U
# Now Install all the dependencies from requirements.txt
RUN pip3 install -r stable-requirements.txt


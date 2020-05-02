# Getting base image as alpine
FROM alpine:latest


# author name
MAINTAINER siddharth pal <siddharthasinghbisen96@gmail.com>

# To add python to container
FROM python:3.7

# To copy the requirements.txt file from local directory to tmp directory in container
COPY requirements.txt /tmp

# to create temp as working directory
WORKDIR /tmp

# To add all the files from local directory to tmp
COPY . /tmp

# To install all dependencies from requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


# To open port at 5000

EXPOSE 5000

ENTRYPOINT ["python"]
# To run main.py file

CMD ["main.py"]

FROM ubuntu:latest

WORKDIR /usr/app/src

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
#install all packages in requirements.txt
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
#copy the whole project
COPY . .


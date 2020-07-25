FROM python:3

RUN apt-get update

# install python-library
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

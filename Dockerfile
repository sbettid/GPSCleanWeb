FROM ubuntu:22.04

WORKDIR /app

ENV PYTHON_VERSION=3.9

COPY . .

RUN apt update -y && apt install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa

RUN ln -fs //usr/share/zoneinfo/Europe/Rome /etc/localtime && apt install -y python3.9-distutils python3.9 python3-pip

RUN python3.9 -m pip install -r requirements.txt --extra-index-url https://google-coral.github.io/py-repo/

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

EXPOSE 8000
FROM registry.access.redhat.com/ubi9/ubi:9.3

WORKDIR /app

ENV PYTHON_VERSION=3.9

COPY . .

RUN dnf install -y python3.9 python3-pip

RUN python3.9 -m pip install -r requirements.txt --extra-index-url https://google-coral.github.io/py-repo/

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

EXPOSE 8000
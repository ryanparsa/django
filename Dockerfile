FROM python:3.12-buster
EXPOSE 8000

COPY requirements-prod.txt .
RUN python3 -m pip install --no-cache-dir --requirement requirements.prod.txt && rm -rfv requirements.prod.txt

WORKDIR /opt/app
ADD src $WORKDIR

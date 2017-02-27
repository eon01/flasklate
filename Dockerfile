FROM python:3.4
ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD app.conf /app
ADD . /app
WORKDIR /
ENTRYPOINT python app.py

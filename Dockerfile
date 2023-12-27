FROM python:3.11

RUN pip install --upgrade pip

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT ["python", "main.py"]

FROM python:3.11

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .
CMD ["python3", "app.py"]


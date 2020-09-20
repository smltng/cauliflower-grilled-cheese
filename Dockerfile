FROM python:3.7.3-slim

COPY . /app
WORKDIR /app
ADD . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

RUN chmod +x ./entry_point.sh
ENTRYPOINT ["sh", "entry_point.sh"]

FROM ubuntu:22.04
RUN apt update
RUN apt install python3-pip -y

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "--config", "gunicorn_config.py", "src:create_app()"]
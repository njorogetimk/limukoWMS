FROM ubuntu:22.04
RUN apt update
RUN apt install python3-pip -y

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV SQLALCHEMY_DATABASE_URI 'postgresql://postgres:postgres@postgres/limuko'
ENV SECRET_KEY '123456789'

CMD ["gunicorn", "--config", "gunicorn_config.py", "src:create_app()"]
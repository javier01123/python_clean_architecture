FROM python:3.8.3
LABEL Javier Andrade

ENV PYTHONUNBUFFERED 1

# RUN apk add --update --no-cache postgresql-client
# RUN apk add --update --no-cache --virtual .tmp-install \
#     postgresql-dev gcc linux-headers python3-dev musl-dev
# RUN apk del .tmp-install

# RUN pip install psycopg2-binary

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# RUN mkdir /app
# WORKDIR /app
# COPY . /app
COPY . .

# RUN adduser -d myuser
# USER myuser
FROM ubuntu:16.04d

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /myMoviesApp/requirements.txt

WORKDIR /myMoviesApp

RUN pip install -r requirements.txt

COPY . /myMoviesApp

ENTRYPOINT [ "python" ]

CMD [ "myMoviesApp.py" ]
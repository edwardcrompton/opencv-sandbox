FROM jjanzic/docker-python3-opencv

RUN pip install imutils
RUN pip install --upgrade pip

RUN mkdir /app
VOLUME /app
WORKDIR /app

ENTRYPOINT ["python"]


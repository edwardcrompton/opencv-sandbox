FROM jjanzic/docker-python3-opencv

ADD images /resources

RUN pip install imutils
RUN pip install --upgrade pip

CMD ["python"]


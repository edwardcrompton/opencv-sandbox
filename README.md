# OpenCV and Python

#### Start commands

docker build -t opencv .
docker run -i -t opencv

#### To run a script in the current folder

docker run -v `pwd`:/app -i -t opencv /app/opencv_tutorial_01.py


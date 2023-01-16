FROM balenalib/raspberrypi3-python

# Install GPIO. This wont install on non-linux OS so we install in the Docker Image.
RUN sudo apt update
RUN sudo apt install gcc libc6-dev && python3 -m pip install RPi.GPIO

# Install the wheel
COPY dist/*.whl /
RUN python3 -m pip install *.whl

CMD sump
HEALTHCHECK CMD ps -ef | grep sump | grep -v grep
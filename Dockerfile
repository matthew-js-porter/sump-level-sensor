FROM raspbian/stretch

RUN sudo apt update
RUN sudo apt upgrade -y
RUN sudo apt install python3 -y
RUN sudo apt install python3-venv python3-pip -y

COPY dist/*.whl /
RUN python3 -m pip install --upgrade --ignore-installed pip setuptools wheel requests pyxdg
RUN python3 -m pip install *.whl
RUN useradd -ms /bin/bash pi
RUN mkdir -p /home/pi
USER pi
CMD sump
HEALTHCHECK CMD ps -ef | grep sump | grep -v grep
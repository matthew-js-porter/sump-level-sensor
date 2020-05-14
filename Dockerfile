FROM raspbian/stretch

RUN sudo apt update
RUN sudo apt upgrade -y
RUN sudo apt install python3 -y
RUN sudo apt install python3-venv python3-pip -y

COPY dist/*.whl /
RUN python3 -m pip install --user --upgrade pip setuptools wheel requests
RUN python3 -m pip install *.whl
CMD sump
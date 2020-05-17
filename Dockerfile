FROM raspbian/stretch

# Update and upgrade packages
RUN sudo apt update
RUN sudo apt upgrade -y

# Install python and pip
RUN sudo apt install python3 -y
RUN sudo apt install python3-venv python3-pip -y

# Remove vulnerable pacakges
RUN apt remove python3-xdg -y
RUN apt remove python3-crypto -y

# Update pip, and requets which pip will need to download packages
RUN python3 -m pip install --upgrade --ignore-installed pip requests

# Install packages needed to install the wheel.
RUN python3 -m pip install --upgrade --ignore-installed setuptools wheel

# Install GPIO. This wont install on non-linux OS so we install in the Docker Image.

RUN python3 -m pip install RPi.GPIO

# Install the wheel
COPY dist/*.whl /
RUN python3 -m pip install *.whl

CMD sump
HEALTHCHECK CMD ps -ef | grep sump | grep -v grep
FROM raspbian/stretch

RUN sudo apt update
RUN sudo apt install python3 -y
RUN sudo apt install python3-venv python3-pip -y

COPY dist/* /
RUN tar -xzf *.tar.gz
RUN mkdir -p sump && cp -r sump-level-sensor*/* sump
WORKDIR sump
ENV PYTHONPATH=sump
RUN pwd
RUN ls
RUN python3 -m pip install -r sump_level_sensor.egg-info/requires.txt
CMD python3 ./sump/sump.py
CMD python3 ./sump/sump.py
# Sump Level Sensor
A tool that uses a raspberry pi to tell if the water levels are higher than they should be.

## build
```bash
python setup.py sdist
docker build . -t sump:latest
```

## run
```bash
docker run -v ${HOME}/.aws:/root/.aws sump:latest
```

## tests
```bash
python setup.py test
```
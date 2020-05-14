# Sump Level Sensor
A tool that uses a raspberry pi to tell if the water levels are higher than they should be.

## build
```bash
python setup.py bdist_wheel
docker build . -t matthewjsporter/sump-level-sensor:latest
```

## Deploy
```bash
docker push matthewjsporter/sump-level-sensor:latest
```

watchtower will automatically deploy to raspberry pi.

The initial deployment can be ran with this command.

```bash
docker run --privileged -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION --name sump --restart=always matthewjsporter/sump-level-sensor:latest
```

watch tower can be deployed with this command.

```bash
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock --restart=always v2tec/watchtower:armhf-latest
```


## run
```bash
docker run -v ${HOME}/.aws:/home/pi/.aws matthewjsporter/sump-level-sensor:latest
```

## tests
```bash
python setup.py test
```

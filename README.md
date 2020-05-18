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
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock --restart=always v2tec/watchtower:armhf-latest -i 30
```


## run
```bash
docker run -v ${HOME}/.aws:/root/.aws matthewjsporter/sump-level-sensor:latest mocksump
```

## tests
```bash
python setup.py test
```


## scanning

### anchore image scanning.
```bash
curl -s https://ci-tools.anchore.io/inline_scan-v0.6.0 | bash -s -- -t 1200 -f -d Dockerfile matthewjsporter/sump-level-sensor:latest

```

### snyk image scanning
```bash
snyk monitor --file=sump_level_sensor.egg-info/requires.txt --package-manager=pip
```


## Cloudformation
```bash
aws cloudformation update-stack --stack-name sump-level-sensor --template-body file://aws/cloudformation.yml --parameters  ParameterKey=EmailParameter,ParameterValue=<email> ParameterKey=SMSParameter,ParameterValue=<phone>
```
node {
    stage('checkout') {
        checkout scm
    }

    stage('build') {
        sh "whoami"
    }

    stage('test') {
        sh "python3 setup.py test"
    }

    stage('package') {
        sh "sudo -S python3 setup.py sdist"
    }

    stage('build container') {
        sh "sudo -S docker build . -t sump:latest"
    }

    stage('run container') {
        sh "sudo -S docker run --privileged -v ${HOME}/.aws:/root/.aws sump:latest"
    }
}
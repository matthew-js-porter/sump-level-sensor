node {
    stage('checkout') {
        checkout scm
    }

    stage('build') {
        sh "python3 setup.py build"
    }

    stage('test') {
        sh "python3 setup.py test"
    }

    stage('package') {
        sh "python3 setup.py sdist"
    }

    stage('build container') {
        sh "sudo docker build . -t sump:latest"
    }

    stage('run container') {
        sh "sudo docker run --privileged -v ${HOME}/.aws:/root/.aws sump:latest"
    }
}
node {
    stage('checkout') {
        checkout scm
    }

    stage('test') {
        sh "python3 setup.py test"
    }

    stage('package') {
        sh "python setup.py sdist"
    }

    stage('build container') {
        sh "docker build . -t sump:latest"
    }

    stage('run container') {
        sh "docker run -v ${HOME}/.aws:/root/.aws sump:latest"
    }
}
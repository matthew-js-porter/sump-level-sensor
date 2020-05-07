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
        sh "python setup.py sdist"
    }

    stage('build container') {
        sh "sudo docker build . -t sump:latest"
    }

    stage('run container') {
        sh "sudo docker run -v ${HOME}/.aws:/root/.aws sump:latest"
    }
}
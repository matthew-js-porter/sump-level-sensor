node {
    stage('checkout') {
        checkout scm
    }

    stage('build') {
        sh """
            #!/bin/bash
            python3 -m venv venv
            . ./venv/bin/activate
            pip install --upgrade pip setuptools wheel requests
            pip install .
        """
    }

    stage('test') {
        sh "python setup.py test"
    }

    stage('package') {
        sh "python setup.py sdist bdist_wheel"
    }

    stage('build container') {
        sh "sudo docker build . -t sump:latest"
    }

    stage('run container') {
        withCredentials([usernamePassword(credentialsId: 'AWS_CREDENTIALS', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
            sh "sudo docker stop sump || { :; }"
            sh "sudo docker rm sump || { :; }"
            sh "sudo docker run --privileged -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=us-east-1 --name sump --restart=always sump:latest &"
        }
    }
}
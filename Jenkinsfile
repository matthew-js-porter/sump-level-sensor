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
        sh "sudo python3 setup.py sdist"
    }

    stage('build container') {
        sh "sudo docker build . -t sump:latest"
    }

    stage('run container') {
        withCredentials([usernamePassword(credentialsId: 'AWS_CREDENTIALS', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
            sh "sudo docker run --privileged -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=us-east-1 sump:latest"
        }
    }
}
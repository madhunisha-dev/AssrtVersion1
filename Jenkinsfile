
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t madhunisha23/asset-system:v1 .'
            }
        }

        stage('Test Container') {
            steps {
                bat 'docker image inspect madhunisha23/asset-system:v1'
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                bat 'where docker'
                bat 'docker --version'
                bat 'docker info'
                }
            }

        stage('Test Container') {
            steps {
                bat 'docker image inspect madhunisha23/asset-system:v1'
            }
        }
    }
}

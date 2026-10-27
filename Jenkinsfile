
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
                bat 'set "PATH=C:\\Users\\madhu\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;%PATH%" && where docker && docker --version && docker info'
                }
            }

        stage('Test Container') {
            steps {
                bat 'docker image inspect madhunisha23/asset-system:v1'
            }
        }
    }
}

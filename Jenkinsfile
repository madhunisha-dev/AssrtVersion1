
pipeline {
    agent any

    environment {
        PATH = "C:\\Users\\madhu\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
        DOCKER_IMAGE = "madhunisha23/asset-system"
        VERSION = "v1"
    }

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

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE%:%VERSION% .'
            }
        }

        stage('Test Docker Image') {
            steps {
                bat 'docker image inspect %DOCKER_IMAGE%:%VERSION%'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '@echo off & echo %DOCKER_PASS%| docker login -u "%DOCKER_USER%" --password-stdin'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'docker push %DOCKER_IMAGE%:%VERSION%'
            }
        }
    }

    post {
        success {
            echo 'Asset System v1 pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }

        always {
            bat 'docker logout'
        }
    }
}

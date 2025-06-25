pipeline {
    agent any

    environment {
        IMAGE_NAME = "discount-app"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yogeshagre/first-order-discount-ml.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build(IMAGE_NAME)
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d -p 8000:8000 ${IMAGE_NAME}"
                }
            }
        }
    }
}

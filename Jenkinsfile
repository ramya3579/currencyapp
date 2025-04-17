pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-currency-converter"
        CONTAINER_NAME = "flask-currency-container"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/ramya3579/currencyapp'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Remove Old Container') {
            steps {
                script {
                    sh "docker rm -f $CONTAINER_NAME || true"
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME"
                }
            }
        }
    }

    post {
        success {
            echo '🚀 Deployed successfully on port 5000!'
        }
        failure {
            echo '❌ Deployment failed. Please check logs.'
        }
    }
}

pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/VigneshKK1007/devops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t kkvignesh/devops-app .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push kkvignesh/devops-app'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop devops-app || true
                docker rm devops-app || true

                docker run -d -p 5000:5000 \
                --name devops-app \
                kkvignesh/devops-app
                '''
            }
        }

    }
}

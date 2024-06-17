pipeline {
    agent any
    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Okemwag/Sharehub.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh './venv/bin/python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sshagent (credentials: ['your-ssh-credentials-id']) {
                    sh 'scp -r * Okemwa@102.133.146.44:/Dinease'
                    sh 'ssh Okemwa@102.133.146.44 "cd /Dinease && ./venv/bin/python manage.py migrate"'
                    sh 'ssh Okemwa@102.133.146.44 "sudo systemctl restart Dinease.service"'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}

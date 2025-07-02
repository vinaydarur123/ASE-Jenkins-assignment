pipeline {
    agent any

    environment {
        PATH = "C:\\Windows\\System32;${env.PATH}"
        PYTHONPATH = "."
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                pytest tests/
                '''
            }
        }

        stage('Done') {
            steps {
                echo '✅ Tests passed.'
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed.'
        }
    }
}

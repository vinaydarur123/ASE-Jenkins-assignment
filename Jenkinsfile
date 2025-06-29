pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat '''
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                set PYTHONPATH=.
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

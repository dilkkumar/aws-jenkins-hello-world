pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo '===== CHECKOUT ====='
                echo 'Getting source code from GitHub...'

                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '===== BUILD ====='
                echo 'Installing application dependencies...'

                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo '===== TEST ====='
                echo 'Testing Python application...'

                sh '''
                    ./venv/bin/python -m py_compile app.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo '===== DOCKER BUILD ====='
                echo 'Creating Docker image...'

                sh '''
                    docker build -t aws-jenkins-hello-world .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '===== DEPLOY ====='
                echo 'Stopping old container...'

                sh '''
                    docker stop aws-jenkins-hello-world || true
                    docker rm aws-jenkins-hello-world || true
                '''

                echo 'Starting new container...'

                sh '''
                    docker run -d \
                        --name aws-jenkins-hello-world \
                        -p 5000:5000 \
                        aws-jenkins-hello-world
                '''
            }
        }
    }

    post {

        success {
            echo '======================================'
            echo '       CI/CD PIPELINE SUCCESS'
            echo '======================================'
        }

        failure {
            echo '======================================'
            echo '       CI/CD PIPELINE FAILED'
            echo '======================================'
        }
    }
}

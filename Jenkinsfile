pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'team-management'
        DOCKER_TAG = "${BUILD_NUMBER}"
        GIT_URL = credentials('GIT_URL_SECRET')
        AWS_REGION = credentials('AWS_REGION')

        DB_CREDENTIALS = credentials('DB_CREDENTIALS')
        DB_HOST = credentials('DB_HOST')
        DB_PORT = credentials('DB_PORT')
        DB_NAME = credentials('DB_NAME')
        CONTAINER_NAME = 'team-management-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    echo "Stopping and removing any existing container with the same name..."
                    sh """
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    """

                    // Jenkins will automatically inject Username with password type Secret as two environment variables:
                    // `${DB_CREDENTIALS_USR}` represents username, `${DB_CREDENTIALS_PSW}` represents password

                    echo "Using DB credentials:"
                    echo "DB User: ${DB_CREDENTIALS_USR}"
                    echo "DB Host: ${DB_HOST}"
                    echo "DB Port: ${DB_PORT}"
                    echo "DB Name: ${DB_NAME}"

                    // Run new Docker container
                    echo "Running new Docker container..."
                    sh """
                        docker run -d \
                            --name ${CONTAINER_NAME} \
                            -p 8000:8000 \
                            -e DB_NAME=${DB_NAME} \
                            -e DB_USER=${DB_CREDENTIALS_USR} \
                            -e DB_PASSWORD=${DB_CREDENTIALS_PSW} \
                            -e DB_HOST=${DB_HOST} \
                            -e DB_PORT=${DB_PORT} \
                            ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    echo "Performing health check..."
                    sh """
                        sleep 10
                        curl -f http://localhost:8000/about/ || exit 1
                    """
                }
            }
        }
    }

    post {

        success {
            echo 'Build and local deployment successful!'
        }
        failure {
            echo 'Build or deployment failed!'
        }
    }
}
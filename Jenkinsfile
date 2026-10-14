
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        set +x
                        echo "$DOCKER_PASS" | docker login \
                          -u "$DOCKER_USER" --password-stdin
                        docker compose push
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy API') {
            steps {
                sh '''
                    docker compose up -d --force-recreate
                    sleep 5
                    docker compose ps
                    curl --fail --silent \
                      "http://localhost:5000/predict?x1=2&x2=3&x3=1"
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose logs --tail=50 || true'
        }
    }
}

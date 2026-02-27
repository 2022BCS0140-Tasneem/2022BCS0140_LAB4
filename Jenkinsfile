pipeline {
    agent any

    environment {
        IMAGE_NAME = "syedtasneemkousar/wine-quality:latest"
        CONTAINER_NAME = "wine_api_container"
        PORT = "8000"
    }

    stages {

        stage('Start') {
            steps {
                echo "CI/CD Pipeline Started"
                echo "Name: Syed Tasneem Kousar"
                echo "Roll No: 2022BCS0140"
            }
        }

        stage('Pull Docker Image') {
            steps {
                script {
                    sh "docker pull ${IMAGE_NAME}"
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh """
                    docker run -d -p ${PORT}:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                    """
                }
            }
        }

        stage('Wait for API') {
            steps {
                script {
                    timeout(time: 60, unit: 'SECONDS') {
                        waitUntil {
                            def status = sh(
                                script: "curl -s http://localhost:${PORT}/ || true",
                                returnStatus: true
                            )
                            return (status == 0)
                        }
                    }
                }
            }
        }

        stage('Valid Inference Test') {
            steps {
                script {
                    def response = sh(
                        script: """
                        curl -s -X POST http://localhost:${PORT}/predict \
                        -H "Content-Type: application/json" \
                        -d @test_data.json
                        """,
                        returnStdout: true
                    ).trim()

                    echo "Valid Response: ${response}"

                    // Validate response contains wine_quality
                    if (!response.contains("wine_quality")) {
                        error("❌ wine_quality field missing!")
                    }

                    // Validate numeric value
                    if (!(response =~ /[0-9]+/)) {
                        error("❌ wine_quality is not numeric!")
                    }
                }
            }
        }

        stage('Invalid Input Test') {
            steps {
                script {
                    def response = sh(
                        script: """
                        curl -s -X POST http://localhost:${PORT}/predict \
                        -H "Content-Type: application/json" \
                        -d @invalid_data.json
                        """,
                        returnStdout: true
                    ).trim()

                    echo "Invalid Response: ${response}"

                    // FastAPI usually returns "detail" for errors
                    if (!response.toLowerCase().contains("detail")) {
                        error("❌ Invalid input did not return proper error!")
                    }
                }
            }
        }

        stage('Stop Container') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                }
            }
        }

        stage('Complete') {
            steps {
                echo "Pipeline Finished Successfully"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline PASSED: Model is working correctly"
        }
        failure {
            echo "❌ Pipeline FAILED: Model validation failed"
        }
        always {
            sh "docker rm -f ${CONTAINER_NAME} || true"
        }
    }
}

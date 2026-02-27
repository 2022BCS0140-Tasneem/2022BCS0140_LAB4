pipeline {
    agent any

    stages {

        stage('Start') {
            steps {
                echo "CI/CD Pipeline Started"
                echo "Name: Syed Tasneem Kousar"
                echo "Roll No: 2022BCS0140"
            }
        }

        stage('Valid Inference Test') {
            steps {
                script {
                    def response = sh(
                        script: '''
                        curl -s -X POST http://host.docker.internal:8000/predict \
                        -H "Content-Type: application/json" \
                        -d @test_data.json
                        ''',
                        returnStdout: true
                    ).trim()

                    echo "Valid Response: ${response}"

                    if (!response.contains("wine_quality")) {
                        error("wine_quality missing!")
                    }
                }
            }
        }

        stage('Invalid Input Test') {
            steps {
                script {
                    def response = sh(
                        script: '''
                        curl -s -X POST http://host.docker.internal:8000/predict \
                        -H "Content-Type: application/json" \
                        -d @invalid_data.json
                        ''',
                        returnStdout: true
                    ).trim()

                    echo "Invalid Response: ${response}"

                    if (!response.toLowerCase().contains("detail")) {
                        error("Invalid input not handled properly!")
                    }
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
            echo "✅ Pipeline PASSED"
        }
        failure {
            echo "❌ Pipeline FAILED"
        }
    }
}

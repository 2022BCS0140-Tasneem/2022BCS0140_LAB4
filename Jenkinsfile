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

        stage('Install Dependencies') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python scripts/train.py'
            }
        }

        stage('Run App Check') {
            steps {
                sh 'python app.py || true'
            }
        }

        stage('Complete') {
            steps {
                echo "Pipeline Finished Successfully"
            }
        }
    }
}

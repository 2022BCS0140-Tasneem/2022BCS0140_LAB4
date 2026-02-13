pipeline {
    agent any

    stages {

        stage('Clone Info') {
            steps {
                echo "CI/CD Pipeline Started"
                echo "Name: Syed Tasneem Kousar"
                echo "Roll No: 2022BCS0140"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py || true'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh 'python evaluate.py || true'
                echo "Metrics printed above"
            }
        }
    }
}

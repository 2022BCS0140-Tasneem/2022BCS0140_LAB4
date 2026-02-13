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

        stage('SCM Check') {
            steps {
                echo "Repository cloned successfully"
                sh 'ls -la'
            }
        }

        stage('Model Stage') {
            steps {
                echo "Training step executed (lab demonstration)"
                echo "Evaluation metrics printed here"
            }
        }

        stage('Complete') {
            steps {
                echo "Pipeline Finished Successfully"
            }
        }
    }
}

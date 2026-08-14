pipeline{
    agent any
    stages{
        stage('Verify Python Env'){
            steps{
                sh 'python --version'
                sh 'ls la'
            }
        }
        stage('Test'){
            steps {
                sh 'python3 test_app.py'
            }
        }
    }
}
pipeline{
    agent any
    stages{
        stage('Verify Python Env'){
            steps{
                sh 'python3 --version'
                sh 'ls -la'
            }
        }
        stage('Test'){
            steps {
                sh 'python3 test_app.py'
            }
        }
    }
    post {
        success{
            echo 'Build Succeeded - tests passed'
        }
        failure{
            echo 'Build failed - checkl and run tests again'
        }
        always{
            echo "Pipeline finshed with status: ${currentBuild.result}"
        }
    }
}
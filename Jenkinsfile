pipeline{
    agent any
    environment{
        GREETING_EXPECTED = "Hello from Jenkins!"
    }
    stages{
        stage('Verify Python Env'){
            steps{
                sh 'python3 --version'
                sh 'ls -la'
            }
        }
        stage('Run Tests'){
            steps {
                sh 'echo "Expecting: $GREETING_EXPECTED"'
                sh 'python3 test_app.py'
            }
        }
    }
    post {
        success{
            echo 'Build Succeeded - tests passed'
        }
        failure{
            echo 'Build failed - check and run tests again'
        }
        always{
            echo "Pipeline finshed with status: ${currentBuild.result}"
        }
    }
}
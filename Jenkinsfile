pipeline{
    agent any
    parameters{
        booleanParam(name: 'SKIP_TESTS', defaultValue: false, description: 'Skip the test stage')
    }
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
            when {
                expression { params.SKIP_TESTS == false } 
            }
            steps {
                sh 'echo "Expecting: $GREETING_EXPECTED"'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
                sh './venv/bin/python test_app.py --junitxml=results.xml'
            }
            post {
                always{
                    junit 'results.xml'
                }
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
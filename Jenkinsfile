pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --alluredir=./allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'allure generate ./allure-results --clean -o ./allure-report'
            }
        }
    }
}

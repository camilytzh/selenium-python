pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                // Windows CMD
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest --alluredir=allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                bat 'allure generate allure-results -o allure-report --clean'
            }
        }
    }
}


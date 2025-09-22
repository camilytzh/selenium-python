pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                bat 'python -m venv venv'              
                bat 'venv\\Scripts\\activate && pip install --upgrade pip'
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
                bat 'venv\\Scripts\\activate && allure generate allure-results -o allure-report --clean'
            }
        }
    }
}



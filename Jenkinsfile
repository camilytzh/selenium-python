pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Creating virtual environment...'
                bat '"%PYTHON_EXE%" -m venv venv'

                echo 'Upgrading pip...'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'

                echo 'Installing requirements...'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                bat 'venv\\Scripts\\python.exe -m pytest --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                bat '"%ALLURE_EXE%" generate allure-results -o allure-report --clean'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}





pipeline {
    agent any

    environment {
        // Cambia esto a la ruta completa de tu python.exe
        PYTHON_EXE = 'C:\\Users\\Camily Torres\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
    }

    stages {
        stage('Setup environment') {
            steps {
                bat '"%PYTHON_EXE%" -m venv venv'

                bat '"%PYTHON_EXE%" -m venv\\Scripts\\python.exe -m pip install --upgrade pip'

                bat '"%PYTHON_EXE%" -m venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat 'venv\\Scripts\\python.exe -m allure generate allure-results -o allure-report --clean'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}




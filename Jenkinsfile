pipeline {
    agent any

    environment {
        PYTHON_EXE = 'C:\\Users\\Camily Torres\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
        ALLURE_EXE = 'C:\\Users\\Camily Torres\\Downloads\\allure-2.35.1\\bin\\allure.bat'
    }

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

        stage('Optional: Open Allure Report') {
            steps {
                echo 'You can serve the Allure report locally if needed...'
                // bat '"%ALLURE_EXE%" serve allure-results'   <- solo para pruebas locales
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}





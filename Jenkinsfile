pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('CheckDir') {
            steps {
                sh 'ls -la'
            }
        }
        stage('CheckDir') {
            steps {
                sh 'hostnamectl'
            }
        }
    }
}


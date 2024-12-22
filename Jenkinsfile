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
                sh 'pwd'
            }
        }
        stage('CheckHost') {
            steps {
                sh 'hostnamectl'
                sh 'cd javaproject'
		sh 'mvn clean package'
		sh 'tree'
            }
        }
    }
}


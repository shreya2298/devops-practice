pipeline {
    agent any

    stages {
        stage('CheckDir') {
            steps {
                sh 'ls -la'
                sh 'pwd'
            }
        }
        stage('CheckHost') {
            steps {
                sh 'hostnamectl'
                sh 'cd javaproject/HelloWorldProject'
                sh 'pwd'
                sh 'whoami'
                sh 'pwd'
                sh 'hostname'
		sh 'mvn -f javaproject/HelloWorldProject/pom.xml clean package'
		sh 'tree'
            }
        }
    }
}


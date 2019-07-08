node {
  checkout scm
}
pipeline {
  agent {
    docker {
      image 'python:2.7'
      args '-u root:root'
    }
  }
  environment {
    SQL_USER = 'None'
    SQL_PW = 'None'
    CLOUDSQL_HOST = 'None'
  }
  stages {
    stage('Test') {
      steps {
        sh 'pip install -r flask/requirements.txt && python flask/tests.py'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t notejam .'
      }
    }
    }
  }

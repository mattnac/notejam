node {
  checkout scm
}
pipeline {
  agent any
  environment {
    SQL_USER = 'None'
    SQL_PW = 'None'
    CLOUDSQL_HOST = 'None'
  }
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:2.7'
          args '-u root:root'
        }
      }
      steps {
        sh 'pip install -r flask/requirements.txt && python flask/tests.py'
      }
    }
    stage('Build') {
      agent {
        docker {
          image 'python:2.7'
          args '-u root:root'
        }
      }
      steps {
        sh 'docker build -t notejam .'
      }
    }
    }
  }
}

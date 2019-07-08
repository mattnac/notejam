node {
  checkout scm
}
pipeline {
  agent none
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
          args '--tmpfs /.config'
        }
      }
      steps {
        sh 'pip install -r flask/requirements.txt && python flask/tests.py'
      }
    }
  }
}

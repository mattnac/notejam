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
      steps {
        sh 'pip install -r flask/requirements.txt -t lib && python flask/tests.py'
      }
    }
  }
}

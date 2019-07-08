node {
  checkout scm
}
pipeline {
  agent {
    docker { image 'python2.7' }
  }
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
    stage('Build') {
      steps {

      }
    }
  }
}

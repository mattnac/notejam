node {
  checkout scm
}
pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'pip install -r flask/requirements.txt -t lib && python flask/tests.py'
      }
    }
  }
}

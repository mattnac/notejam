node {
  checkout scm
}
pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh '-c pip install -r flask/requirements -txt && python flask/tests.py'
      }
    }
  }
}

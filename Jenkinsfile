node {
  checkout scm
  def dockerImage
  stage('Clone repo') {
    checkout scm
  }
  stage('Build Image') {
    app = docker.build('notejam')
  }
  stage('Test') {
    app.inside {
      sh '-c /usr/local/bin/python tests.py'
    }
  }
}

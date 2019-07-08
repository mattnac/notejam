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
    withEnv(['CLOUDSQL_HOST=none', 'SQL_USER=none', 'SQL_PW=none']) {
      app.inside {
        sh '/usr/local/bin/python flask/tests.py'
      }
    }
  }
  stage('Push Image') {
    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
      app.push("${env.BUILD_NUMBER}")
      app.push("latest")
    }
  }
}

node {
  checkout scm
  def dockerImage
  stage('Clone repo') {
    checkout scm
  }
  stage('Build Image') {
    app = docker.build('mattiasdahlgren/notejam')
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
  stage('Authenticate k8s') {
    gcloud = docker.image('gcr.io/cloud-builders/gcloud')
    withCredentials([file(bookshelf-k8s-key, variable: 'GCE_ACCOUNT')]) {
      withEnv(['GOOGLE_APPLICATION_CREDENTIALS=$GCE_ACCOUNT']) {
        gcloud.inside('gcloud container clusters get-credentials demo-cluster --zone us-central1-a')
      }
    }
  }
}

node {
  checkout scm
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
    withCredentials([file(credentialsId: 'bookshelf-k8s-key', variable: 'GCE_ACCOUNT')]) {
      sh 'export GOOGLE_APPLICATION_CREDENTIALS=$GCE_ACCOUNT'
      sh 'gcloud container clusters get-credentials demo-cluster --zone us-central1-a'
    }
  }
  stage('Deploy service') {
    withCredentials([file(credentialsId: 'bookshelf-k8s-key', variable: 'GCE_ACCOUNT')]) {
      sh 'export GOOGLE_APPLICATION_CREDENTIALS=$GCE_ACCOUNT'
      sh 'kubectl -n notejam --record deployment.apps/notejam set image deployment.apps/notejam notejam=mattiasdahlgren/notejam:latest'
  }
  }
}

pipeline {
  // agent any
  agent { label 'ubuntu' } 
  stages {
    stage('Test Deploy') {
      steps([$class: 'BapSshPromotionPublisherPlugin']) {
        echo "deploying application to test environment"
        sshPublisher(
          continueOnError: false,
          failOnError: true,
          publishers: [
            sshPublisherDesc(
              configName: "test",
              verbose: true,
              transfers: [
                sshTransfer(execCommand: "sudo kill -9 `sudo lsof -t -i:5000`"),
                sshTransfer(execCommand: "pushd rest-flask-api && git reset --hard && git clean -fd && git pull && pipenv install && nohup pipenv run sh ./bootstrap.sh && popd")
              ]
            )
          ]
        )
      }
    }

    stage('Test Execution') {
      steps {
        sh 'cd tests'
        sh 'pipenv run pytest --alluredir=reports --base_url=http://34.135.218.254:5000'
      }
      // post {
      //   always {
      //     allure([
      //       includeProperties: false,
      //       properties: [],
      //       reportBuildPolicy: 'ALWAYS',
      //       results: [
      //         [path: 'reports']
      //       ]
      //     ])
      //   }
      // }
    }

    stage('Prod Deploy') {
      steps([$class: 'BapSshPromotionPublisherPlugin']) {
        echo "deploying application"
        sshPublisher(
          continueOnError: false,
          failOnError: true,
          publishers: [
            sshPublisherDesc(
              configName: "prod",
              verbose: true,
              transfers: [
                sshTransfer(execCommand: "sudo kill -9 `sudo lsof -t -i:5000`"),
                sshTransfer(execCommand: "pushd rest-flask-api && git reset --hard && git clean -fd && git pull && pipenv install && nohup pipenv run sh ./bootstrap.sh && popd")
              ]
            )
          ]
        )
      }
    }
  }

  post {
    always {
      echo 'The pipeline completed!'
    }
    success {
      echo "Flask Application Up and running!!"
    }
    failure {
      echo 'Build stage failed'
      error('Stopping early…')
    }
  }
}
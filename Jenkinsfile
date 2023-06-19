pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'echo "building the repo"'
            sh 'pipenv install'
            sh 'pipenv run sh ./bootstrap.sh &'
          }
        }
      }
    }
  
    stage('Test') {
      steps {
        sh 'cd tests'
        sh 'pipenv run pytest --alluredir=reports --base_url=http://localhost:5000'
      }
    }

    stage('Deploy') {
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
          echo "deploying application"
            sshPublisher(
                continueOnError: false, 
                failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "rest-api",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "git pull")
                        ]
                    )
                ]
            )
        }
    }
    
    // stage('Deploy')
    // {
    //   steps {
    //     echo "deploying the application "
    //   }
    // }
  }
  
  post {
        always {
            echo 'The pipeline completed'
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
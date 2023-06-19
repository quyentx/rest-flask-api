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
                          // sshTransfer(execCommand: "sudo kill -9 `sudo lsof -t -i:5000`"),
                          sshTransfer(execCommand: "pushd rest-flask-api && git pull && pipenv install && popd")
                        ]
                    )
                ]
            )
            // sshagent(credentials : ['quyentx_ste_at_34.136.158.210']) {
            // sh 'ssh -v quyentx_ste@104.154.92.222'
            // sh 'rm -rf rest-flask-api'
            // sh 'git clone git@github.com:quyentx/rest-flask-api.git'
            // sh 'cd rest-flask-api'
            // sh 'pipenv install'
            // sh 'pipenv run sh ./bootstrap.sh &'
            // }
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
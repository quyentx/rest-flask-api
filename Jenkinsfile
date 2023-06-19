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
            // sshPublisher(
            //     continueOnError: false, 
            //     failOnError: true,
            //     publishers: [
            //         sshPublisherDesc(
            //             configName: "rest-api",
            //             verbose: true,
            //             transfers: [
            //               sshTransfer(execCommand: "rm -rf rest-flask-api"),
            //               sshTransfer(execCommand: "git clone git@github.com:quyentx/rest-flask-api.git"),
            //               sshTransfer(execCommand: "pwd"),
            //               sshTransfer(execCommand: "ls -l"),
            //               // sshTransfer(execCommand: "pipenv install"),
            //               sshTransfer(execCommand: "pipenv run sh ./rest-flask-api/bootstrap.sh &")
            //             ]
            //         )
            //     ]
            // )
            // sshagent(credentials : ['quyentx_ste_at_34.136.158.210']) {
            // sh 'ssh -o StrictHostKeyChecking=no quyentx_ste@34.136.158.210 uptime'
            // sh 'ssh -v quyentx_ste@34.136.158.210'
            // sh 'rm -rf rest-flask-api'
            // sh 'git clone git@github.com:quyentx/rest-flask-api.git'
            // sh 'cd rest-flask-api'
            // sh 'pipenv install'
            // sh 'pipenv run sh ./bootstrap.sh &'
            // }
            def remote = [:]
            remote.name = "node-1"
            remote.host = "104.154.92.222"
            remote.allowAnyHosts = true

            node {
                withCredentials([sshUserPrivateKey(credentialsId: 'quyentx_ste_at_34.136.158.210', passphraseVariable: '', usernameVariable: 'quyentx_ste')]) {
                    remote.user = userName
                    stage("SSH Steps Rocks!") {
                        sshCommand remote: remote, command: 'rm -rf rest-flask-api'
                        sshCommand remote: remote, command: 'git clone git@github.com:quyentx/rest-flask-api.git'
                        sshCommand remote: remote, command: 'cd rest-flask-api'
                        sshCommand remote: remote, command: 'pipenv install'
                        sshCommand remote: remote, command: 'pipenv run sh ./rest-flask-api/bootstrap.sh &'
                    }
                }
            }
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
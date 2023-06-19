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
        sh 'pipenv run pytest alluredir=reports --base_url=http://localhost:5000'
        input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
      }
    }
  
    // stage('Deploy')
    // {
    //   steps {
    //     echo "deploying the application"
    //     sh "sudo nohup python3 app.py > log.txt 2>&1 &"
    //   }
    // }
  }
  
  post {
        always {
            echo 'The pipeline completed'
            junit allowEmptyResults: true, testResults:'**/reports'
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
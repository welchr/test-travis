pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip2 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest --pyargs nin --junitxml report.xml'
        junit 'report.xml'
      }
    }
  }
}

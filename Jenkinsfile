pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'virtualenv --no-site-packages testenv'
        sh 'source testenv/bin/activate'
        sh 'testenv/bin/pip install --no-cache-dir -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'testenv/bin/pytest --pyargs nin --junitxml report.xml'
        junit 'report.xml'
      }
    }
  }
}

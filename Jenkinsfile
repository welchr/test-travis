pipeline {
  agent any

  environment {
    PATH = "/home/linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
  }

  stages {
    stage('build') {
      steps {
        sh 'which python'
        sh 'echo $PATH'
        sh 'python2 -m virtualenv --no-site-packages testenv'
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
    stage('cleanup') {
      sh 'deactivate'
      sh 'rm -rf testenv'
      sh 'rm -f report.xml'
    }
  }
}

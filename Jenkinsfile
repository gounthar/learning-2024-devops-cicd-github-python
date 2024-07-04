
pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile add2vals.py calc.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}

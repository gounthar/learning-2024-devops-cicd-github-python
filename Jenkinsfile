pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile addvals.py calc.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        },
        stage('Unit Testing') {
            steps {
                sh 'python -m py_compile test_calc.py'
            }
        }
    }
}

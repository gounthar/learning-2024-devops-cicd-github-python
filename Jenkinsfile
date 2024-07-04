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

        stage('Unit Tests') {
            steps {
                unstash('compiled-results')
                sh 'pytest --junitxml=test-results.xml'
                archiveArtifacts(artifacts: 'test-results.xml', allowEmptyArchive: true)
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}

// check pipeline

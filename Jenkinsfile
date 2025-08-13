pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage("Cloning from Github...") {
            steps {
                script {
                    echo 'Cloning from Github...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[credentialsId: 'github-token-2', url: 'https://github.com/chinmay116/Hybrid-Anime-Recommendation.git']]
                    )
                }
            }
        }

        stage("Making a Virtual Environment...") {
            steps {
                sh """
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install dvc[gs]  # important: gs extra for Google Storage
                """
            }
        }

        stage('DVC Pull') {
            steps {
                withCredentials([file(credentialsId: 'gcp-anime-key', variable: 'GCP_KEY')]) {
                    script {
                        echo 'DVC Pull...'
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        
                        # Force DVC to use the key from Jenkins
                        export GOOGLE_APPLICATION_CREDENTIALS="${GCP_KEY}"
                        
                        # Make sure remote is correct and not broken
                        dvc remote modify myremote credentialpath "${GCP_KEY}" || true
                        
                        # Pull data from remote
                        dvc pull -v
                        '''
                    }
                }
            }
        }

    }
}

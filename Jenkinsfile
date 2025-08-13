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
                withCredentials([file(credentialsId: 'gcp-anime-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh """
                        echo "Using creds from: \$GOOGLE_APPLICATION_CREDENTIALS"
                        ls -l \$GOOGLE_APPLICATION_CREDENTIALS
                        . ${VENV_DIR}/bin/activate
                        export GOOGLE_APPLICATION_CREDENTIALS=\$GOOGLE_APPLICATION_CREDENTIALS
                        dvc pull -v
                    """
                }
            }
        }
    }
}

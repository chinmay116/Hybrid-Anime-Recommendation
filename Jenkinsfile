pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{

        stage("Cloning from Github..."){
            steps{
                script{
                    echo 'Cloning from Github...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'gcp-key-anime', url: 'https://github.com/chinmay116/Hybrid-Anime-Recommendation.git']])
                }
            }
        }
    }
}
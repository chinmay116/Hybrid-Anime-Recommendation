pipeline {
    agent any

    stages{
        stage("Cloning from Github..."){
            steps{
                script{
                    echo 'Cloning from Github...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token-2', url: 'https://github.com/chinmay116/Hybrid-Anime-Recommendation.git']])
                }
            }
        }
    }
}
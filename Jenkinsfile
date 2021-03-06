pipeline {
    agent any
    environment {
        registry = "tal19987/imdb-backend"
        registryCredential = "dockerhub-account"
        image = "${registry}:backend-${env.BUILD_ID}"
        google_project_id = "learned-battery-260616"
        kubernetes_cluster_name = "cluster-1"
        location = "us-central1-c"
        credentials_id = "My First Project"
    }
    stages {
        stage ("Build Docker Image") {
            steps {
                script {
                    customImg = docker.build(image, "./server")
                }
            }
        }
        stage ("Publish to Docker Registry")
        {
            steps {
                script {
                        docker.withRegistry('',registryCredential) {
                            customImg.push()
                            customImg.push('latest')
                    }
                }
            }
        }
        stage ("Deploy to Kubernetes") {
            steps {
                step ([
                    $class: 'KubernetesEngineBuilder',
                    projectId: env.google_project_id,
                    clusterName: env.kubernetes_cluster_name,
                    location: env.location,
                    manifestPattern: './server/backend-deployment.yaml',
                    credentialsId: env.credentials_id,
                    verifyDeployments: true
                ]) 
            }
        }
    }
    post {
        always {
            sh "docker rmi -f ${customImg.id}"
        }
    }
}
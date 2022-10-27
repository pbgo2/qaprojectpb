// node {
//     stages{
//     stage('Clone'){
//             sh "git clone https://github.com/deepanshuMeteor/examplerepo.git"
//     }
//    stage('Build Docker') {
//        // build the docker image from the source code using the BUILD_ID parameter in image name
//          sh "sudo docker build -t flask-app ."
//    }
//    stage("run docker container"){
//         sh "sudo docker run -p 8000:8000 --name flask-app -d flask-app "
//     }
// }




pipeline{
        agent any
        stages{
            stage('Clone'){
                sh "git clone https://github.com/pbgo2/qaprojectpb.git"
            }
            stage('Build Docker') {
            // build the docker image from the source code using the BUILD_ID parameter in image name
                sh "sudo docker build -t flask-app ."
            }
            stage("run docker container"){
                sh "sudo docker run -p 5000:5000 --name flask-app -d flask-app "
            }
        }
}
# Flask - Structure
_This project aims to demonstrate (in an easily digestable manner) how to structure a simple flask project with 
all the boilerplate and testing frameworks set up (with some examples!)_

The example also contains container definitions for a flask application. 

## Tests
- Run using: _python3 -m unittest discover_

## To Run in Docker
- docker-compose up -d --build_

## Publish to Github Container Repository - GHCR
Instructions here:
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry

1. Create security access token - https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
2. export CR_PAT=YOUR_TOKEN
3. echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

# Tag and publish images to Github packages
## Get images
docker images
## Get the image name to tag and tag with the repo
docker tag <TAG_ID> ghcr.io/<USER_NAME>/<IMAGE_NAME>:latest
docker push ghcr.io/<USER_NAME>/<IMAGE_NAME>:latest

https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry

## Kubernetes Deploy
# Create Flask Deployment
kubectl create -f ./kubernetes/flask-deployment.yml
# Create service
kubectl create -f ./kubernetes/flask-service.yml
# Create the ingress object:
kubectl apply -f ./kubernetes/minikube-ingress.yml

# Update hosts file to route requests from host defined, hello.world to Minikube instance
sudo echo "$(minikube ip) hello.structure" | sudo tee -a /etc/hosts
# ON MAC: Create tunnel
'docker port minikube | grep 22' to get the API_SERVER_SSH_PORT


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
# Create the volume 
kubectl apply -f ./kubernetes/persistent-volume.yml
# View details of volume
kubectl get pv

# Create the volume chain
kubectl apply -f ./kubernetes/persistent-volume-claim.yml

# Add Secrets object - secrets are based 64 obfuscated - echo -n "pleasechangeme" | base64 AND echo -n "sample" | base64

kubectl apply -f ./kubernetes/secret.yml

# Create the Postgres Deployment
kubectl create -f ./kubernetes/postgres-deployment.yml
# View deployments
kubectl get deployments
# Create Postgres service 
kubectl create -f ./kubernetes/postgres-service.yml
# Get Pod Names
kubectl get pods
# Create the database using the pod name
kubectl exec postgres-775dcb5b64-q58rq --stdin --tty -- createdb -U sample books
# Verify
kubectl exec postgres-775dcb5b64-q58rq --stdin --tty -- psql -U sample

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

# TODO: 
- Add prometheus 
- Add grafana 
- Create full deploy script (To kubernetes control plane) - (Compatible with EKS )

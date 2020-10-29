# Kubernetes lab on Minikube
## Project details
 Create a local kubernetes cluster. Create two separate namespaces ping and pong. Deploy a redis container on a pong namespace and a container with a simple python script to send ping request redis container.
 
## Prerequisites
- Mac OSX
- VirtualBox
- Minikube
- Docker

## Installing Minikube
To setup minikube kubernetes cluster, follow the official documentation at https://minikube.sigs.k8s.io/docs/start/

## Getting Started

Follow the below steps to run this project on a Minikube cluster.

1. Download Git:
    - For OSX -> https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
2. Clone this repository:
    - `git clone https://github.com/srtimsina/k8slab.git`
3. Enter the repo directory:
    - `cd k8slab`
4. Run `docker build -t sti.local/alpine-python:3.8 .`.
5. Run `kubectl apply -f .`.
6. Output should be something like:

```
namespace/ping created
namespace/pong created
deployment.apps/redis created
persistentvolumeclaim/redis-data created
service/redis created
deployment.apps/redis-client created
```

7. Get the list of namespaces

```
$ kubectl get ns -A
```

```
NAME                   STATUS   AGE
default                Active   147d
kube-node-lease        Active   147d
kube-public            Active   147d
kube-system            Active   147d
kubernetes-dashboard   Active   147d
ping                   Active   3m32s
pong                   Active   3m32s
```

8. Check the logs for ping response.

```
$ kubectl logs redis-client-75dffdb8b5-5dhxv
```

```
True
response from host "redis.pong.svc.cluster.local"
True
response from host "redis.pong.svc.cluster.local"
True
response from host "redis.pong.svc.cluster.local"
True
response from host "redis.pong.svc.cluster.local"
True
response from host "redis.pong.svc.cluster.local"
True
```
- To delete, run `kubectl delete -f .`.
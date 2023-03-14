# Dask cluster templates
These templates were used for Dask Helmcluster setup on a custom Kubernetes cluster. 

## Kubernetes setup
Follow the RKE2 [quick start guide][1]

## Ingress controller setup
The ingress option was preferred over NodePorts and port forwarding in order to manage TLS termination (https connections)independently of the deployment or service involved. Note that TLS termination steps are optional.

### 1. Create an nginx ingress controller deployment
Before setting any ingress rules for any of Dask or monitoring deployment, the ingress controller must be installed. The usual nginx controller repository contains several [guides][3] and alternatives. In this case, the "baremetal" option is chosen since this cluster is not related to any mainstream cloud vendor. 

```bash
#Installing the controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.6.4/deploy/static/provider/baremetal/deploy.yaml
```

Check that it [works][4].

### 2. Create a domain or subdomain
Main steps:
- Ensure you have a static IP address
- Obtain a free or paid domain/subdomain to assignto thet IP address
- Save the domain/subdomain name to use for subsequent ingress rule definitions. 


### 3. Self-signed TLS certificate and private key creation
Note: a self-signed certificate is not suitable for production. Only use for testing purposes. 

```bash
openssl req -new \
-x509 -sha256 -days 365 -nodes \
-key tls/private-key.key -out tls/certificate.crt \
-addext "subjectAltName=DNS:<your-domain-1>,DNS:<your-domain-2>"
```

### 4. Secret creation
This process must be repeated for every namespace that has a desired service endpoint. In this case, the Dask (default)and monitoring namespaces would have a corresponding secret created. 

```bash
kubectl create secret tls secret \
--key tls/private-key.key \
--cert tls/certificate.crt \
--namespace desired-namespace
```


## Dask cluster setup
Once the Kubernetes cluster is set, download the helm chart and install it as indicated by the [documentation][2]

```bash
#Install Dask charts
helm repo add dask https://helm.dask.org
helm repo update
helm install --version 2023.1.0 myrelease dask/dask
```

### 1. To prepare volumes for Jupyter notebook
This values.yaml configuration assumes the availability of persistence volumes for the dask-notebook pod. 
Follow the [volume template guide](./dask_volume_templates/README.md) to setup the volumes in advance.

### 2. Setting up NodePorts for external access. 
This repository contains two NodePort templates for accessing the [JupyterLab GUI](./nodeport_jupyter.yaml) and the [Dask dashboard](./nodeport_dask_ui.yaml). The alternative is to use port forwarding as described
in the Helm Chart documentation. 

An even better alternative is to use an [ingress](#ingress-controller-setup), as was used in this case.  

```bash
#Adding nodeport 
kubectl apply -f <nodeport_template.yaml>

#Port forwarding (alternative)
kubectl port-forward  \
--namespace svc/myrelease-dask-jupyter \
<external port>:80 &

#Port forwarding from any address (warning: exposes the port the specified IP address)
kubectl port-forward  \
--address <client IP address>
--namespace svc/myrelease-dask-jupyter \
<external port>:80 &


```

### 3. To use the present templates, provide them during the installation process
```bash
#Use the values.yaml template
helm repo add dask https://helm.dask.org
helm repo update

helm install \
--version 2023.1.0 \
--values values.yaml \
myrelease \
dask/dask

#For upgrading
helm upgrade \
--version 2023.1.0 \
--values values.yaml \
myrelease \
dask/dask
```


[1]: https://docs.rke2.io/install/quickstart
[2]: https://docs.dask.org/en/stable/deploying-kubernetes-helm.html
[3]: https://github.com/kubernetes/ingress-nginx/blob/main/docs/deploy/index.md#bare-metal-clusters
[4]: https://github.com/kubernetes/ingress-nginx/blob/main/docs/deploy/index.md#pre-flight-check
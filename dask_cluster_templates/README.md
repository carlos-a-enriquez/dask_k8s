# Dask cluster templates
These templates were used for Dask Helmcluster setup on a custom Kubernetes cluster. 

## Kubernetes setup
Follow the RKE2 [quick start guide][1]

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
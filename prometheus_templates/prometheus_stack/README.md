# Prometheus stack installation
As an alternative to the stand-alone Prometheus chart, a ["Prometheus stack"][1] helm chart provides graphana and Prometheus as a bundled pair. 

## Setting the PVs for Prometheus server
First, create the respective local folders and make them available. Then, create the resources 
on the cluster. 

```bash
#On the PV host machine
sudo mkdir -p /data/prometheus_server
sudo chown nobody:nogroup /data/prometheus_server
sudo chmod 777 /data/prometheus_server

#provisioning
kubectl apply -f ../prometheus_chart/storage-class.yaml #Reclaim policy is Retain
kubectl apply -f prom-pv-local.yaml
```

## Install the prometheus chart helm chart
Now that the PV resource is available, install the [chart][1].

```bash
#Install repository
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

#Reinstalling prometheus-stack
helm install prometheus-stack prometheus-community/kube-prometheus-stack \
--version 45.0.0 \
--namespace monitoring \
--values values.yaml &

#Uninstall
helm uninstall prometheus-stack --namespace monitoring
```

## Setting up ingress access
Check the following [guide](../../dask_cluster_templates/README.md#ingress-controller-setup) for the nginx ingress controller setup. If the TLS certificate and private key have already been created, make them available to the "monitoring" namespace by creating a secret as described within the same [guide](../../dask_cluster_templates/README.md#4-secret-creation). 



[1]: https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack
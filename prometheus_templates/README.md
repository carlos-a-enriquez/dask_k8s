# Prometheus setup
Setting up the promethesus helm chart for monitoring the Dask job scheduling and execution. 

# 1. Setting the PVs for Prometheus server and alertmonitor
First, create the respective local folders and make them available. Then, create the resources 
on the cluster. 

```bash
#On dask-instance 2
sudo mkdir -p /data/prometheus_alert
sudo chown nobody:nogroup /data/prometheus_alert
sudo chmod 777 /data/prometheus_alert

#On dask-instance 3
sudo mkdir -p /data/prometheus_server
sudo chown nobody:nogroup /data/prometheus_server
sudo chmod 777 /data/prometheus_server

#provisioning
kubectl apply -f storage-class.yaml #Reclaim policy is Retain
kubectl apply -f alert-pv-local.yaml
kubectl apply -f server-pv-local.yaml
```

# 2. Install the Prometheus Helm chart
Now that the resources are available, install the [chart][1]. 

```bash
#Pulling Helm Chart
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

#Creating the namespace
kubectl create namespace monitoring

#Installing Prometheus
#Version: https://artifacthub.io/packages/helm/prometheus-community/prometheus
helm install prometheus prometheus-community/prometheus \
--version 19.3.3 \
--namespace monitoring

#Checking status
kubectl get all --namespace=monitoring
```

[1]: https://artifacthub.io/packages/helm/prometheus-community/prometheus
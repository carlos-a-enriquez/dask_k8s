# Grafana helm chart
Setting up the helm chart.

# Setting up the custom volume resource

```bash
#Setting the PV mount (Node4)
sudo mkdir -p /data/grafana
sudo chown nobody:nogroup /data/grafana
sudo chmod 777 /data/grafana

#Setting the PV resource
kubectl create -f graf-pv-local.yaml
```

# Installing the helm chart

```bash
#Getting the repo
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

#Install grafana helm chart
helm install grafana grafana/grafana \
--version 6.50.7 \
--namespace monitoring \
--values values.yaml
```
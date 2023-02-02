# Dask_k8s

This repository will contain the files related to the deployment of Dask Helm charts on the OpenStack 
Kubernetes cluster. 

## Update 02/02/2023
Until yestarday, I had been working with the deployment and service yaml files that are part of the
Dask helm chart manifest. Remember that the manifest is "a YAML-encoded representation of the Kubernetes resources that were generated from this release's chart(s)."

However, from now on I will avoid that in order to concentrate on modifying the values.yaml file only. This way,
all that I need to modify my dask cluster is to run ```helm upgrade --values values.yaml --version 2023.1.0 myrelease dask/dask```. 

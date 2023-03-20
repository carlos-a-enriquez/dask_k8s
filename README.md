# Dask_k8s

This repository will contain the files related to the deployment of Dask Helm charts on the OpenStack 
Kubernetes cluster. 

## 1. Infrastructure setup

### Dask cluster setup.
Check [here](./dask_cluster_templates/README.md).

### Prometheus monitoring setup
Check [here](./prometheus_templates/prometheus_chart/README.md) for the Promethus stand-alone or [here](./prometheus_templates/prometheus_stack/README.md) for the Promethus stack (Graphana included). 


## 2. Custom Dask Docker images
The Dask base [image][1] and the dask-notebook [image][2] were modified to be able to run the ["SCENIC" protocol][3]. The corresponding Dockerfiles are accessible [here](./container_images/). 


## 3. Example notebooks
To test the execution of [pySCENIC][4], the mouse brain dataset and the PBMC dataset were used. The custom notebooks adapted from the ["SCENIC" protocol][3] repository can be found [here](./project/SCENIC%20Protocol%20-%20Case%20study%20-%20Mouse%20brain%20data%20set.ipynb) and [here](./PBMC_project/PBMC10k_SCENIC_custom-polished-version.ipynb). 


[1]: ghcr.io/dask/dask
[2]: ghcr.io/dask/dask-notebook
[3]: https://github.com/aertslab/SCENICprotocol
[4]: https://github.com/aertslab/pySCENIC
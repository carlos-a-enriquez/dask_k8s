# Dask volume templates
The Dask cluster [values file](../values.yaml) assumes that a persistent volume is avilable for binding.
This persistent volume (PV) must be provisioned before helm chart installation. The process describe herein 
assumes the provisioning of a "local" PV. 

## Procedure
1. Create the folder to be used as "local" mount point and make it accessible to Kubernetes.
2. Create the StorageClass
3. Create the Persistent Volume
4. Create the Persistent Volume Claim. 
5. Install/upgrade the helm cluster with the appropriate [value](../values.yaml) configuration. 

```bash
#Setting the folder (in node 2)
sudo mkdir -p /data
sudo chown nobody:nogroup /data
sudo chmod 777 /data

#Creating PV and Storage Class
kubectl apply -f storage-class.yaml #Order corrected later
kubectl apply -f persistent-volume.yaml


#Creating PV claim
kubectl apply -f dask-pv-claim.yaml

#Applying values change
helm upgrade \
--values values.yaml \
--version 2023.1.0 \
myrelease \
dask/dask
```
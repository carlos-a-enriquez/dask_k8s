# Dask NFS
The Dask cluster [PBMC values file](../PBMC_values.yaml) assumes that a persistent volume is avilable for binding.
This persistent volume (PV) must be provisioned before helm chart installation. The process describes how to set a VM as an NFS host such that it can be made available to the Kubernetes cluster for binding. 

The process is similar to that of the [local persistent volume](../dask_volume_templates/README.md).

## Procedure
1. Setup the NFS host.
2. Setup the NFS client.
3. Create the StorageClass
4. Create the Persistent Volume
5. Create the Persistent Volume Claim. 
6. Install/upgrade the helm cluster with the appropriate [value](../values.yaml) configuration. 

## NFS setup
In order to setup a VM instance as an NFS host, the machine must be accessible as a superuser.

### NFS host setup
Run the following commands on the NFS host. 

```bash
#Create the path to export
sudo apt install nfs-kernel-server
sudo mkdir -p /mnt/nfs/promdata
sudo chown nobody:nogroup /mnt/nfs/promdata
sudo chmod 777 /mnt/nfs/promdata

#Export the NFS path
cat << EOF >> /etc/exports
/mnt/nfs/promdata <Client IP address range>(rw,no_subtree_check,no_root_squash)
EOF

#Activating NFS access
sudo systemctl enable --now nfs-server
sudo exportfs -ar #check man exportfs for clarification
```

### NFS client setup
Run the following commands on the NFS clients. Even if access to the NFS server is done through Kubernetes, the NFS client program must be installed on the clients. 

```bash
#NFS installation on the clients
sudo apt install -y nfs-common
```

## Kubernetes persistent volume setup
Run the following commands using the YAML files contained within this path in order to make the NFS persistent volume accessible to the Dask deployment. After running this commands, the NFS PV should be available 

```bash
#Activating the storage class
kubectl apply -f nfs-storage-class.yaml

#Activating the PV
kubectl apply -f pv-dask-nfs.yaml

#Activating the PV claim
kubectl apply -f dask-nfs-pv-claim.yaml
```




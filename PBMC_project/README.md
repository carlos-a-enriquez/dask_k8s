# Input file recovery

Run the following code to obtain the input data. Check the SCENIC [protocol documentation](https://github.com/aertslab/SCENICprotocol/tree/master) and the [original SCENIC publication](https://www.nature.com/articles/s41596-020-0336-2) for further details.  

## Initial files

```bash

### Expression dataset
wget http://cf.10xgenomics.com/samples/cell-exp/3.0.0/pbmc_10k_v3/pbmc_10k_v3_filtered_feature_bc_matrix.tar.gz

### Transcription factors
wget https://raw.githubusercontent.com/aertslab/pySCENIC/master/resources/hs_hgnc_tfs.txt

### TF annotation database
wget https://resources.aertslab.org/cistarget/motif2tf/motifs-v9-nr.hgnc-m0.001-o0.0.tbl


```


## Genome ranking database retrieval
```bash
##################### Genome ranking database
mkdir -p -v /mnt/databases/PBMC #Jupyter notebook

wget -O /mnt/databases/PBMC/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather \
https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg38/refseq_r80/mc9nr/gene_based/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather

#Genome ranking checksum
wget -O /mnt/databases/PBMC/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather.sha1sum.txt \
https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg38/refseq_r80/mc9nr/gene_based/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather.sha1sum.txt

#Checksum check
cat /mnt/databases/PBMC/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather.sha1sum.txt 

#getting the checksum
sha1sum /mnt/databases/PBMC/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather 

```
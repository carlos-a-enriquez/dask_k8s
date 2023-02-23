import os

PROJECT = "/home/jovyan/work/dask_k8s/project"
DATA_FOLDER="/tmp"
RESOURCES_FOLDER="/resources"
#DATABASE_FOLDER = "/databases/"
DATABASE_FOLDER = PROJECT+"/databases/"
SCHEDULER="myrelease-dask-scheduler:8786"
#DATABASES_GLOB = "."+os.path.join(PROJECT, DATABASE_FOLDER, "mm9-*.mc9nr.genes_vs_motifs.rankings.feather")
DATABASES_GLOB = os.path.join(DATABASE_FOLDER, "mm9-*.mc9nr.genes_vs_motifs.rankings.feather")
MOTIF_ANNOTATIONS_FNAME = "."+os.path.join(PROJECT, RESOURCES_FOLDER, "motifs-v9-nr.mgi-m0.001-o0.0.tbl")
MM_TFS_FNAME = "."+os.path.join(PROJECT, RESOURCES_FOLDER, 'mm_mgi_tfs.txt')
SC_EXP_FNAME = "."+os.path.join(PROJECT, RESOURCES_FOLDER, "GSE60361_C1-3005-Expression.txt")
REGULONS_FNAME = os.path.join(PROJECT, DATA_FOLDER, "regulons.p")
MOTIFS_FNAME = os.path.join(PROJECT, DATA_FOLDER, "motifs.csv")
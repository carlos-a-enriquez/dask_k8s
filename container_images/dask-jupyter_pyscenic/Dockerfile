FROM ghcr.io/dask/dask-notebook
LABEL dataset=PBMC

RUN conda install -y conda==23.1.0
RUN conda install -y -c conda-forge matplotlib seaborn

RUN python -m pip install scanpy==1.9.3
RUN python -m pip install pyscenic==0.12.1
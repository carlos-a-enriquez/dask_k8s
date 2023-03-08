FROM ghcr.io/dask/dask:2023.1.0
LABEL dataset=PBMC

COPY dask_config.yaml /root/.config/dask/

RUN conda install -y conda==23.1.0 \
&& conda install -y -c conda-forge matplotlib seaborn \
&& conda clean -afy \
&& find /opt/conda/ -follow -type f -name '*.a' -delete \
&& find /opt/conda/ -follow -type f -name '*.pyc' -delete \
&& find /opt/conda/ -follow -type f -name '*.js.map' -delete 

RUN python -m pip install scanpy==1.9.3 pyscenic==0.12.0
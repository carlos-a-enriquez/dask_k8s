FROM ghcr.io/dask/dask:2023.1.0

COPY dask_config.yaml /root/.config/dask/

RUN conda install -y -c conda-forge matplotlib seaborn

RUN python -m pip install scanpy==1.9.3
RUN python -m pip install pyscenic==0.12.1
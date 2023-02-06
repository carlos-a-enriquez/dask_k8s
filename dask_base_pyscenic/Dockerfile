FROM ghcr.io/dask/dask:2023.1.0

RUN conda install -y numpy pandas matplotlib seaborn

RUN conda install -y anaconda cytoolz

RUN conda install -y seaborn scikit-learn statsmodels numba pytables

RUN conda install -y -c conda-forge python-igraph louvain

RUN conda install -y -c conda-forge multicore-tsne

RUN python -m pip install scanpy

RUN python -m pip install pyscenic
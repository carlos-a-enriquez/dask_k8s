FROM ghcr.io/dask/dask:2023.1.0

RUN conda install numpy pandas matplotlib seaborn

RUN conda install -c anaconda cytoolz

RUN conda install seaborn scikit-learn statsmodels numba pytables

RUN conda install -c conda-forge python-igraph louvain

RUN conda install -c conda-forge multicore-tsne

RUN python -m pip install scanpy

RUN python -m pip install pyscenic
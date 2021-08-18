FROM nvcr.io/nvidia/merlin/merlin-training:0.5.3

ENV LD_LIBRARY_PATH /usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/local/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64

WORKDIR /src

COPY dask-nvtabular-criteo-benchmark.py ./

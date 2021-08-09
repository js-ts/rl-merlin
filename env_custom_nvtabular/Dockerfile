FROM gcr.io/deeplearning-platform-release/base-cu110

WORKDIR /merlin

ENV LD_LIBRARY_PATH /usr/local/cuda/lib:/usr/local/cuda/lib64:/usr/local/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib:/usr/local/nvidia/lib64

RUN git clone https://github.com/NVIDIA/NVTabular.git
RUN conda env create -f=NVTabular/conda/environments/nvtabular_dev_cuda11.0.yml
RUN /opt/conda/envs/nvtabular_dev_11.0/bin/pip install -e NVTabular/.

COPY entrypoint.sh ./
COPY test_import.py ./
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
# Local Installation

conda install -c nvidia -c rapidsai -c numba -c conda-forge nvtabular cudatoolkit=11.2

### Install CRC for gcloud alpha storage

This can be installed as part of the docker image.  
pip install google-crc32c==1.1.2 --target /usr/lib/google-cloud-sdk/lib/third_party

### Docker simplification and execution testing

<!-- Start the container in interactive mode -->
docker run -it --rm --gpus all \
-v /home/renatoleite/workspace/data_sample:/training_data \
<container ID> /bin/bash

<!-- Run python benchmark -->
python dask-nvtabular-criteo-benchmark.py \
--data-path /training_data/ \
--out-path /output/ \
--devices "0"
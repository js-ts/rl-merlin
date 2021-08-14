# NVTabular benchmark setup

### Test 1 - Local execution on the Notebook with SSD PD

python dask-nvtabular-criteo-benchmark.py \
--data-path /home/jupyter/data \
--out-path /home/jupyter/bench-results \
--profile /home/jupyter/bench-results/report-notebook-ssd.html \
-d "0,1"

### Test 2 - Local execution on the Notebook with Google Storage

python dask-nvtabular-criteo-benchmark.py \
--data-path gs://workshop-datasets/criteo-parque/ \
--out-path gs://renatoleite-staging/bench-results/ \
--profile gs://renatoleite-staging/bench-results/report-notebook-gcs.html \
-d "0,1"

### Test 3 - Vertex AI traning job with FUSE storage mounted

python dask-nvtabular-criteo-benchmark.py \
--data-path /gcs/workshop-datasets/criteo-parque/ \
--out-path /gcs/renatoleite-staging/bench-results/ \
--profile /gcs/renatoleite-staging/bench-results/report-notebook-gcs.html \
-d "0,1"


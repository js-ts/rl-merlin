# NVTabular benchmark setup

### Test 1 - Local execution on the Notebook with SSD PD

python dask-nvtabular-criteo-benchmark.py \
--data-path /home/jupyter/data \
--out-path /home/renatoleite/merlin-on-gcp/bench-results \
--profile /home/renatoleite/merlin-on-gcp/bench-results/report-notebook-ssd.html \
--devices "0"
 <!-- Optional \
--part-mem-frac 0.01 \
--device-limit-frac 0.2 \
--device-pool-frac 0.2 -->

### Test 2 - Local execution on the Notebook with Google Storage

python dask-nvtabular-criteo-benchmark.py \
--data-path gs://workshop-datasets/criteo-parque/ \
--out-path gs://renatoleite-staging/bench-results/ \
--profile gs://renatoleite-staging/bench-results/report-notebook-gcs.html \
--devices "0"



```
docker build -t gcr.io/jk-mlops-dev/nvt-benchmark .
docker push gcr.io/jk-mlops-dev/nvt-benchmark 
```

## Local PD

```
docker run -it --rm --gpus all \
-v /mnt/disks/criteo:/data \
gcr.io/jk-mlops-dev/nvt-benchmark \
python dask-nvtabular-criteo-benchmark.py \
--data-path /data/criteo-benchmark-test \
--out-path /data/nvt_benchmark \
--devices "0,1" \
--device-limit-frac 0.8 \
--device-pool-frac 0.9 \
--num-io-threads 0 \
--part-mem-frac 0.125 \
--profile /data/output_benchmark/dask-report.html
```

## NFS

```
docker run -it --rm --gpus all \
-v /mnt/nfs:/data \
gcr.io/jk-mlops-dev/nvt-benchmark \
python dask-nvtabular-criteo-benchmark.py \
--data-path /data/criteo-benchmark-test \
--out-path /data/nvt_benchmark \
--devices "0,1" \
--device-limit-frac 0.8 \
--device-pool-frac 0.9 \
--num-io-threads 0 \
--part-mem-frac 0.125 \
--profile /data/output_benchmark/dask-report.html
```

## GCS

```
docker run -it --rm --gpus all \
-v /home/jupyter/src:/out \
gcr.io/jk-mlops-dev/nvt-benchmark \
python dask-nvtabular-criteo-benchmark.py \
--data-path gs://jk-vertex-us-central1/criteo-benchmark-test \
--out-path gs://jk-vertex-us-central1/nvt_benchmark \
--devices "0,1" \
--device-limit-frac 0.8 \
--device-pool-frac 0.9 \
--part-mem-frac 0.125 \
--profile  /out/dask-report.html \
--num-io-threads 0 
```


## Locally and Vertex AI


sudo docker run -it --rm --gpus all \
-v /home/ext_renatoleite_google_com/data:/data \
-v /home/ext_renatoleite_google_com/nvt_results:/nvt_results \
gcr.io/renatoleite-mldemos/nvt-nvidia-053 \
python dask-nvtabular-criteo-benchmark.py \
--data-path /data \
--out-path /nvt_results \
--devices "0" \
--device-limit-frac 0.8 \
--device-pool-frac 0.9 \
--num-io-threads 0 \
--part-mem-frac 0.125 \
--profile /nvt_results/dask-report.html

python run.py \
--data-path gs://renatoleite-criteo-partial/data \
--out-path gs://renatoleite-criteo-partial/nvt_benchmark \
--devices "0,1" \
--device-limit-frac 0.8 \
--device-pool-frac 0.9 \
--part-mem-frac 0.125 \
--profile /gcs/renatoleite-criteo-partial/dask-report.html \
--num-io-threads 0
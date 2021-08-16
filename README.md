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

### To create a DL vm for development
gcloud compute instances create ml-dev \
--project=renatoleite-mldemos \
--zone=us-east1-c \
--machine-type=n1-standard-8 \
--network-interface=network-tier=PREMIUM,subnet=default \
--metadata=install-nvidia-driver=True \
--maintenance-policy=TERMINATE \
--service-account=464015718044-compute@developer.gserviceaccount.com \
--scopes=https://www.googleapis.com/auth/cloud-platform \
--accelerator=count=1,type=nvidia-tesla-t4 \
--image-family=common-cu110 \
--image-project=deeplearning-platform-release \
--boot-disk-size=200GB \
--no-boot-disk-auto-delete \
--boot-disk-type=pd-ssd \
--boot-disk-device-name=ml-development \
--no-shielded-secure-boot \
--shielded-vtpm \
--shielded-integrity-monitoring \
--reservation-affinity=any
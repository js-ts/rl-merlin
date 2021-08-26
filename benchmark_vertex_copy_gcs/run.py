# Copyright (c) 2021 NVIDIA Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# Standard Libraries
import argparse
import logging
import pprint
import time

from google.cloud import aiplatform


PREPROCESS_FILE = 'dask-nvtabular-criteo-benchmark.py'


def run(args):

    aiplatform.init(
        project=args.project,
        location=args.region,
        staging_bucket=args.gcs_bucket
    )

    job_name = 'NVT_BENCHMARK_{}'.format(time.strftime("%Y%m%d_%H%M%S"))

    worker_pool_specs =  [
        {
            "machine_spec": {
                "machine_type": args.machine_type,
                "accelerator_type": args.accelerator_type,
                "accelerator_count": args.accelerator_num,
            },
            "replica_count": 1,
            "disk_spec": {
                "boot_disk_type": "pd-ssd",
                "boot_disk_size_gb": 3000,
            },
            "container_spec": {
                "image_uri": args.preprocess_image,
                "command": ["python", PREPROCESS_FILE],
                "args": [
                    '--data-path=' + args.data_path, 
                    '--out-path=' + args.out_path,
                    '--devices=' + args.devices,
                    '--profile=' + args.profile,
                ],
            },
        }
    ]

    logging.info(f'Starting job: {job_name}')

    job = aiplatform.CustomJob(
        display_name=job_name,
        worker_pool_specs=worker_pool_specs,
        
    )
    job.run(sync=True,
        restart_job_on_worker_restart=False,
    )

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--project',
                        type=str,
                        default='renatoleite-mldemos',
                        help='Project ID')
    parser.add_argument('--region',
                        type=str,
                        default='us-central1',
                        help='Region')
    parser.add_argument('--gcs_bucket',
                        type=str,
                        default='gs://renatoleite-staging',
                        help='GCS bucket')
    parser.add_argument('--vertex_sa',
                        type=str,
                        default='sa-admin@renatoleite-mldemos.iam.gserviceaccount.com',
                        help='Vertex SA')
    parser.add_argument('--machine_type',
                        type=str,
                        default='a2-highgpu-8g',
                        help='Machine type')
    parser.add_argument('--accelerator_type',
                        type=str,
                        default='NVIDIA_TESLA_A100',
                        help='Accelerator type')
    parser.add_argument('--accelerator_num',
                        type=int,
                        default=8,
                        help='Num of GPUs')
    parser.add_argument('--preprocess_image',
                        type=str,
                        default='us-east1-docker.pkg.dev/renatoleite-mldemos/docker-images/nvt-conda:latest',
                        help='Training docker image name')
    parser.add_argument('--data-path',
                        type=str,
                        default='/data',
                        help='Criteo parquet data location')
    parser.add_argument('--out-path',
                        type=str,
                        default='/output',
                        help='Output GCS location')
    parser.add_argument("--protocol",
                        choices=["tcp", "ucx"],
                        default="tcp",
                        type=str,
                        help="Communication protocol to use (Default 'tcp')")
    parser.add_argument("--devices",
                        default="0,1,2,3,4,5,6,7",
                        type=str,
                        help='Comma-separated list of visible devices (e.g. "0,1,2,3"). '
                        "The number of visible devices dictates the number of Dask workers (GPU processes) "
                        "The CUDA_VISIBLE_DEVICES environment variable will be used by default")
    parser.add_argument("--profile",
                        metavar="PATH",
                        default='/report/report_local_copy.html',
                        type=str,
                        help="Specify a file path to export a Dask profile report (E.g. dask-report.html)."
                        "If this option is excluded from the command, not profile will be exported")

    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%m-%y %H:%M:%S')

    logging.info(f"Args: {args}")

    run(args)
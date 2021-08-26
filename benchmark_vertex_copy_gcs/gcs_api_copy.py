from google.cloud import storage
from itertools import repeat
import concurrent.futures
import time


def list_blobs_with_prefix(bucket_name: str,
                           prefix: str, 
                           delimiter: str = None):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, delimiter=delimiter)

    return [blob.name for blob in blobs]

def download_blob(bucket_name: str, 
                  source_blob_name: str, 
                  destination_file_name: str):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    return (
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )


# Information needed to download the objects
bucket_name = 'renatoleite-criteo-partial'
prefix = ''
delimiter = None
blobs = list_blobs_with_prefix(bucket_name, prefix, delimiter)

# Destination folder
dest_folder = '/home/renatoleite/data/'
dest_files = [dest_folder + blob.split(sep='/')[-1] for blob in blobs]

start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_blob, 
                repeat(bucket_name), 
                blobs, 
                dest_files)

end_time = time.perf_counter()

print(f'Finished in {end_time-start_time} seconds.')
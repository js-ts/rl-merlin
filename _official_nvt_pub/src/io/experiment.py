from gcs_path import GcsPath

b = 'gs://rl-gcloud-alpha/'
test = GcsPath(b, 'txt', True, False)

test.extension.ext_name
test.path_metadata
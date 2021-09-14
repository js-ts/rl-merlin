from gcs_path import GcsPath

b = 'gs://rl-gcloud-alpha/efolderfdsfsd'
test = GcsPath(b, 'txt', False)

test.path_metadata
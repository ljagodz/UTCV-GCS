# NOTES: must set environment variable GOOGLE_APPLICATION_CREDENTIALS according to
# the bucket ID assigned in Google Cloud Storage account.
# DEPENDENCIES: pip install --upgrade google-cloud-storage
# SUPPORTING DOCS:
# https://cloud.google.com/storage/docs/uploading-objects
# https://cloud.google.com/storage/docs/reference/libraries

from google.cloud import storage
import datetime

# Function implementation for uploading file.

def upload_csv(bucket_name, source_file_name, destination_file_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_file_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_file_name))


# File upload below.

# Change this to whatever the bucket is called, or just call it UTCV-Bucket
bucket_name = 'testbucketutcv'
source = 'csvupload.csv'
destination = 'csvupload{}'.format(datetime.datetime.now()) # Necessary to differentiate between files uploaded to bucket.

upload_csv(bucket_name, source, destination)
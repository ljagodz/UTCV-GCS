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

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def list_blobs_with_prefix(bucket_name, prefix, delimiter=None):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs(prefix=prefix, delimiter=delimiter)

    print('Blobs:')
    for blob in blobs:
        print(blob.name)

    if delimiter:
        print('Prefixes:')
        for prefix in blobs.prefixes:
            print(prefix)

def get_blobs_with_prefix(bucket_name, prefix, delimiter=None):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs(prefix=prefix, delimiter=delimiter)
    return blobs

def test_exists(test_name, bucket_name):
    test_list = get_blobs_with_prefix(bucket_name, "/description", "/")
    for test in test_list:
        if test.name == test_name:
            return True
    return False

def create_new_test(test_name, bucket_name):
    if  test_exists(test_name, bucket_name):
        print("Failed, test already exists")
        return
    # Path to description files
    local = '/localstorage/description/' + test_name + '.txt'
    cloud = '/description/' + test_name

    # Create txt description file
    open(local, 'a').close()

    # Upload generated file into description folder in cloud
    upload_blob(bucket_name, local, cloud)
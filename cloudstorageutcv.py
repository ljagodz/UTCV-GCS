# NOTES: must set environment variable GOOGLE_APPLICATION_CREDENTIALS according to
# the bucket ID assigned in Google Cloud Storage account.
# DEPENDENCIES: pip install --upgrade google-cloud-storage
# SUPPORTING DOCS:
# https://cloud.google.com/storage/docs/uploading-objects
# https://cloud.google.com/storage/docs/reference/libraries

from google.cloud import storage
import datetime
from time import sleep
import serial

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


ser = serial.Serial('/dev/cu.usbmodem14201', 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish
while True:
     counter +=1
     #ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     print(ser.readline()) # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
     if counter == 255:
        counter = 32

# File upload below.

# Change this to whatever the bucket is called, or just call it UTCV-Bucket
#bucket_name = 'testbucketutcv'
#source = 'csvupload.csv'
#destination = 'csvupload{}'.format(datetime.datetime.now()) # Necessary to differentiate between files uploaded to bucket.

#upload_csv(bucket_name, source, destination)
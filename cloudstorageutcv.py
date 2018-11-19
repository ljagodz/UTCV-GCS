# NOTES: must set environment variable GOOGLE_APPLICATION_CREDENTIALS according to
# the bucket ID assigned in Google Cloud Storage account.
# DEPENDENCIES: pip install --upgrade google-cloud-storage
# pip install --upgrade pyserial
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

# BELOW ARE FUNCTIONS FOR DATA COLLECTION FROM ARDUINO.


def add_to_list(input, n):
    # input is string of digits, n is desired precision for data.
    # note: length of input string must be 2n.
    velocity.append(input[0:(n - 1)])
    voltage.append(input[n:(2*n - 1)])


def test_add_to_list(input):
    testlist.append(input)


# Initialize serial monitor port.
ser = serial.Serial('/dev/cu.usbmodem14201', 9600)  # Establish the connection on a specific port

# Boolean variables for checking whether test has started.
poll = True
test = False
n = 3  # Can change this value to desired precision as required.

# Lists containing data collected from serial monitor, to be formatted into .csv.
velocity = []
voltage = []
testlist = []

sleep(3)
ser.write('b'.encode('utf-8'))
sleep(0.5)

while poll:
    line = ser.readline()
    #print(line)
    if line == b'Start\r\n':
        poll = False
        test = True
    else:
        sleep(0.5)
        ser.write('b'.encode('utf-8'))

while test:
    input_line = ser.readline()  # Read the newest output from the Arduino
    if input_line == b'done\r\n':
        test = False
    else:
        test_add_to_list(input_line)
    sleep(.1)  # Delay for one tenth of a second

for i in testlist:
    print(i.decode('utf-8'))


# File upload below.

# Change this to whatever the bucket is called, or just call it UTCV-Bucket
# bucket_name = 'testbucketutcv'
# source = 'csvupload.csv'
# destination = 'csvupload{}'.format(datetime.datetime.now())

# upload_csv(bucket_name, source, destination)
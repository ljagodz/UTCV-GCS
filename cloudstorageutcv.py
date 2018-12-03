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
from calculation import *
from user_input import *
import serial

# BELOW ARE FUNCTIONS FOR DATA COLLECTION FROM ARDUINO.

def add_to_list(input, n):
    # input is string of digits, n is desired precision for data.
    # note: length of input string must be 2n.
    velocity.append(input[0:(n - 1)])
    voltage.append(input[n:(2*n - 1)])


def test_add_to_list(input):
    testlist.append(input)

#Function to run a test, returns list to be made into a CSV file:
# [Amount of Chemical, Distance, Average Velocity, Average Voltage]
# Note Arduino has to be running in a loop awaiting start signal
def collect_data(chemical_amount):
    # Initialize serial monitor port.
    ser = serial.Serial('/dev/cu.usbmodem14201', 9600) # Establish the connection on a specific port

    # Boolean variables for checking whether test has started.
    poll = True
    testing = False
    n = 3  # Can change this value to desired precision as required.

    # Value of period of polling sensors in seconds
    period = 0.5

    # Lists containing data collected from serial monitor, to be formatted into .csv.
    velocity = []
    voltage = []
    testlist = []

    while poll:
        ser.write('b'.encode('utf-8'))
        sleep(0.5)
        line = ser.readline()
        # print(line)
        if line == b'Start\r\n':
            poll = False
            testing = True

    while testing:
        input_line = ser.readline()  # Read the newest output from the Arduino
        if input_line == b'done\r\n':
            testing = False
        else:
            testlist.append(input_line)
            #ADD CODE TO APPEND TO VELOCITY AND VOLTAGE
        sleep(.5)  # Delay for half of a second


    if prompt_decision("Visualize data?"):
        print("Plotting Velocity and Voltage")
        linear_timeplot("velocity", velocity, period)
        linear_timeplot("voltage", voltage, period)

    distance_travelled = distance(velocity, period)
    average_volatage = average(voltage)
    average_velocity = average(velocity)

    test_output = {"velocity": velocity,
                    "voltage": voltage,
                    "summary": [chemical_amount, distance_travelled, average_velocity, average_volatage]
                   }

    return(test_output)




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

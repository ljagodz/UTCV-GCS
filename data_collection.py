from time import sleep
from calculation import *
from user_input import *
import serial

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
        sleep(period)  # Delay for half of a second


    if prompt_decision("Visualize data?"):
        print(" Plotting Velocity and Voltage")
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
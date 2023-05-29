import serial
import csv
import time

# Set the serial port and baud rate
ser = serial.Serial('COM8', 115200, timeout=1)
time.sleep(2)

# Create a CSV file and write the header row
with open('D:\\Internet Technologies Lab\\Arduino-CSV Project\\file1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "SensorValue"])

    # Read data from the serial port and write to the CSV file
    while True:
        line = ser.readline().decode().rstrip()
        if line:
            writer.writerow([time.time(), line])
            
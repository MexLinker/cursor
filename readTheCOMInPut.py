import serial
import time

# Configure the serial port (adjust the port name and baud rate as necessary)
ser = serial.Serial('COM13', 9600, timeout=1)  # Change 'COM3' to your port name
time.sleep(2)  # Wait for 2 seconds to ensure the serial connection is established

print("Reading serial data. Press Ctrl+C to stop.")

try:
    while True:
        # Read a line of data from the serial port
        # data = ser.readline().decode('utf-8').strip()

        data = ser.readline()
        
        # Print the data to the console
        if data:
            print(f"Received: {data}")
            print(type(data))
            number = int(data.decode().strip())
            print(number)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()

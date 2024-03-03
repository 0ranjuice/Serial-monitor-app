import time
import random
import serial


def generate_random_number():
    """Generate a random 8-digit number and send it to COM2"""
    ser = serial.Serial('COM2')  # Open COM2 port

    while True:
        random_number = random.randint(10000000, 99999999)  # Generate a random 8-digit number
        random_number_str = (str(random_number)+'\n').encode()  # Convert the number to bytes

        ser.write(random_number_str)  # Send the random number to COM2

        time.sleep(1)  # Wait for 1 second before sending the next number


# Start the process of generating random numbers and sending them to COM2
generate_random_number()

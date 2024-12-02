#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import argparse
from datetime import datetime
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection
from sensirion_i2c_scd import Scd4xI2cDevice
import logging

# Set up logging for general information (SensorData.log)
logging.basicConfig(
    filename='/home/tarek/SCD41/python-i2c-scd-master/examples/SensorData.log', 
    level=logging.INFO, 
    format='%(message)s'
)
logger = logging.getLogger()

# Set up logging for errors (error.log)
error_handler = logging.FileHandler('/home/tarek/SCD41/python-i2c-scd-master/examples/error.log')
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
logger.addHandler(error_handler)

parser = argparse.ArgumentParser()
parser.add_argument('--i2c-port', '-p', default='/dev/i2c-1')
args = parser.parse_args()

try:
    # Connect to the I²C 1 port
    with LinuxI2cTransceiver(args.i2c_port) as i2c_transceiver:
        # Create SCD4x device
        scd4x = Scd4xI2cDevice(I2cConnection(i2c_transceiver))

        # Make sure measurement is stopped, else we can't read serial number or
        # start a new measurement
        scd4x.stop_periodic_measurement()

        # Print the serial number of the device
        logger.info("scd4x Serial Number: {}".format(scd4x.read_serial_number()))

        # Start periodic measurement
        scd4x.start_periodic_measurement()

        # Run indefinitely and keep measuring
        while True:
            time.sleep(5)  # Wait 5 seconds between measurements
            try:
                co2, temperature, humidity = scd4x.read_measurement()

                # Debugging: Ensure valid sensor readings
                if co2 is None or temperature is None or humidity is None:
                    logger.warning("Invalid sensor readings detected!")
                    continue

                # Get the current timestamp in a readable format
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Log the data to the SensorData.log file
                logger.info(f"CO2: {co2}, Temperature: {temperature}, Humidity: {humidity}, {timestamp}")

            except Exception as e:
                logger.error(f"Error reading sensor data or logging: {str(e)}")

except Exception as e:
    logger.error(f"An error occurred: {str(e)}")

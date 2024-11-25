import time
from sensirion_i2c_driver import I2cConnection
from sensirion_i2c_scd4x import Scd4xSensor
from smbus2 import SMBus

def main():
    # Initialize I2C bus (use the appropriate I2C bus number, e.g., 1 for Raspberry Pi)
    i2c_bus_number = 1  # Change if using a different platform
    i2c_bus = SMBus(i2c_bus_number)

    # Create a connection to the sensor
    connection = I2cConnection(i2c_bus)
    scd4x = Scd4xSensor(connection)

    try:
        # Start periodic measurement
        scd4x.start_periodic_measurement()
        print("Measurement started. Waiting for first data...")

        # Wait for initial measurement (approx. 5 seconds)
        time.sleep(5)

        while True:
            # Read measurement
            if scd4x.data_ready():
                co2, temperature, humidity = scd4x.read_measurement()
                if co2 is not None:
                    print(f"CO2: {co2} ppm, Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %RH")
                else:
                    print("Invalid reading. Sensor warming up...")
            else:
                print("Data not ready, waiting...")
            
            # Wait before reading again
            time.sleep(5)

    except KeyboardInterrupt:
        print("Stopping measurement...")
    finally:
        # Stop periodic measurement and close the connection
        scd4x.stop_periodic_measurement()
        i2c_bus.close()
        print("Measurement stopped.")

if __name__ == "__main__":
    main()

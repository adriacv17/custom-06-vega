import time
from utils.utils_producer import create_producer, generate_machine_data, send_sensor_data
from utils.utils_logger import log_info

# Create Kafka producer instance
producer = create_producer()

# Generate and send sensor data to Kafka every few seconds
while True:
    # Generate random machine sensor data
    machine_data = generate_machine_data()

    # Send the generated data to Kafka
    send_sensor_data(producer, machine_data)

    # Log the data being sent
    log_info(f"Data sent: {machine_data}")

    # Wait for 5 seconds before sending the next data point
    time.sleep(5)

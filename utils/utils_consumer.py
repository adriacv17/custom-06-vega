import json
from kafka import KafkaConsumer
from collections import deque
import time
from utils.utils_config import get_kafka_broker_address, get_kafka_topic
from utils.utils_logger import log_error, log_info

# Initialize Kafka Consumer
def create_consumer():
    """Create and return Kafka consumer for industrial sensor data."""
    consumer = KafkaConsumer(
        get_kafka_topic(),
        bootstrap_servers=get_kafka_broker_address(),
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    return consumer

def process_sensor_data(message, timestamps, temperatures, pressures):
    """Process individual sensor data message."""
    try:
        data = message.value
        timestamps.append(data['timestamp'])
        temperatures.append(data['temperature'])
        pressures.append(data['pressure'])
    except KeyError as e:
        log_error(f"Missing key in sensor data: {e}")

def detect_anomaly(sensor_data):
    """Check for anomalies in the sensor data."""
    anomaly_message = None
    if sensor_data['temperature'] > 90:
        anomaly_message = "Anomaly Detected: High Temperature"
    elif sensor_data['pressure'] > 180:
        anomaly_message = "Anomaly Detected: High Pressure"
    
    if anomaly_message:
        log_info(anomaly_message)
    return anomaly_message

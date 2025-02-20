import random
import json
from datetime import datetime
from kafka import KafkaProducer
from utils.utils_config import get_kafka_broker_address, get_kafka_topic
from utils.utils_logger import log_info

# Initialize Kafka Producer
def create_producer():
    """Create and return Kafka producer."""
    producer = KafkaProducer(
        bootstrap_servers=get_kafka_broker_address(),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

def generate_machine_data():
    """Generate random sensor data for industrial machines."""
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    machine_id = f"machine_{random.randint(1, 10)}"
    temperature = round(random.uniform(70.0, 100.0), 1)
    pressure = round(random.uniform(100, 200), 1)
    return {
        "timestamp": timestamp,
        "machine_id": machine_id,
        "temperature": temperature,
        "pressure": pressure,
    }

def send_sensor_data(producer, data):
    """Send sensor data to Kafka topic."""
    producer.send(get_kafka_topic(), data)
    log_info(f"Sent: {data}")

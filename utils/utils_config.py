import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_kafka_broker_address():
    return os.getenv('KAFKA_BROKER_ADDRESS', 'localhost:9092')

def get_kafka_topic():
    return os.getenv('KAFKA_TOPIC', 'industrial_sensors')

def get_base_data_dir():
    return os.getenv('BASE_DATA_DIR', 'data')

def get_sensor_log_file_name():
    return os.getenv('SENSOR_LOG_FILE_NAME', 'sensor_data.json')

def get_sqlite_db_path():
    """Get the SQLite database path."""
    return os.getenv('SQLITE_DB_PATH', 'data/sensor_data.db')

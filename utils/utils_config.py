"""
Config Utility
File: utils/utils_config.py

This script provides the configuration functions for the project. 

It centralizes the configuration management 
by loading environment variables from .env in the root project folder
 and constructing file paths using pathlib. 

If you rename any variables in .env, remember to:
- recopy .env to .env.example (and hide the secrets)
- update the corresponding function in this module.
"""

###################################################
# Imports
###################################################

# import from Python Standard Library
import os

# import from external packages
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

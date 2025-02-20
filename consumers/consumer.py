from utils.utils_consumer import create_consumer, process_sensor_data, detect_anomaly
from utils.utils_logger import log_info
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib
from consumers.db_sqlite import insert_message, init_db
from utils.utils_config import get_base_data_dir

# Path to SQLite database
DB_PATH = pathlib.Path(get_base_data_dir()) / "sensor_data.db"

# Initialize SQLite database
init_db(DB_PATH)

# Create Kafka consumer instance
consumer = create_consumer()

# Initialize deque (fixed-length queues) to store the latest sensor data for plotting
timestamps = deque(maxlen=20)
temperatures = deque(maxlen=20)
pressures = deque(maxlen=20)

# Setup Matplotlib for real-time plotting (2 rows, 1 column)
fig, ax = plt.subplots(2, 1, figsize=(10, 8))  # Changed from (3, 1) to (2, 1)

# Temperature plot
temp_line, = ax[0].plot([], [], label='Temperature (°C)')
ax[0].set_xlim(0, 20)
ax[0].set_ylim(70, 100)
ax[0].set_title('Real-Time Temperature')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Temperature (°C)')
ax[0].legend()

# Pressure plot
pressure_line, = ax[1].plot([], [], label='Pressure (bar)')
ax[1].set_xlim(0, 20)
ax[1].set_ylim(100, 200)
ax[1].set_title('Real-Time Pressure')
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Pressure (bar)')
ax[1].legend()

# Function to update the plots in real-time
def update_plot(frame):
    try:
        # Poll the consumer for new messages
        message = consumer.poll(timeout_ms=1000)  # Wait for new messages
        for _, msgs in message.items():
            for msg in msgs:
                data = msg.value
                process_sensor_data(msg, timestamps, temperatures, pressures)
                detect_anomaly(data)  # Check for anomalies in the data

                # Create a processed message with necessary details
                message = {
                    "message": f"Machine data: {data}",
                    "author": data.get('machine_id'),
                    "timestamp": data.get('timestamp'),
                    "temperature": data.get('temperature'),
                    "pressure": data.get('pressure')
                }
                insert_message(message, DB_PATH)  # Insert the message into SQLite

    except Exception as e:
        log_info(f"Error: {e}")

    # Update the plot with the latest sensor data
    temp_line.set_data(range(len(temperatures)), list(temperatures))
    pressure_line.set_data(range(len(pressures)), list(pressures))

# Create an animated plot for real-time data visualization
ani = animation.FuncAnimation(fig, update_plot, interval=1000)
plt.tight_layout()
plt.show()

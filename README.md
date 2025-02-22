# Real-Time Industrial Sensor Monitoring System

This project is about monitoring sensor data in real time from industrial machines. We’re focusing on tracking things like **temperature** and **pressure** to make sure the equipment is running smoothly. We use **Kafka** for message streaming and **matplotlib** for visualizing the data in real-time.

## What’s Happening in This Project?

### The Pipeline

- **Producer**: The producer simulates machines sending sensor data (temperature and pressure) every few seconds. It generates random values and sends them to a Kafka topic called `industrial_sensors`.
- **Consumer**: The consumer picks up that data from Kafka, processes it, and then displays it in real-time on a graph. It helps you spot any unusual patterns or potential issues with the machines.

### What’s the Focus?

The main goal of this system is to keep an eye on how the machines are doing by checking key metrics (temperature and pressure). Here’s why that’s important:

- **Machine Health**: By keeping tabs on these parameters, you can predict when maintenance might be needed or if something’s going wrong with the equipment.
- **Anomaly Detection**: The system can raise an alarm when something’s off, like if the temperature spikes too high or the pressure goes out of range.

### What Happens with Each Data Point?

Each data point that comes in contains:
1. **Timestamp**: When the data was collected.
2. **Temperature and Pressure**: These are the key readings that we're tracking. The system checks if these values cross certain thresholds.
    - If the **temperature** goes above a certain level (e.g., 90°C), it’s flagged as an anomaly.
    - If the **pressure** exceeds a certain value (e.g., 180 bar), it's also flagged as an anomaly.
3. **Visualization**: The new data points are immediately added to live graphs, showing how things are changing over time. It’s a great way to monitor things in real-time.

### Why Is This Interesting?

It’s a simple yet powerful way to keep machines running smoothly. The real-time aspect means you can spot problems before they become big issues, saving time and preventing costly failures. It’s like having a constant health check for your machines.

### Real-Time Visualization

The data is displayed on live charts so you can see exactly what’s going on with temperature and pressure at any given moment. It updates continuously as new data comes in, giving you a clear picture of trends and any potential problems.

---

## Getting Started

### Step 1: Set Up Your Environment

Before running the project, make sure you've set up **Kafka** and **Zookeeper**. Follow the instructions in **SETUP-KAFKA.md**.

- Make sure you have **Python 3.11** installed.
- Start **Zookeeper** and **Kafka** if they’re not already running.

### Step 2: Fork the Repo and Set Up

Once you have everything ready, fork this project into your own GitHub account. Then you can run and experiment with it. You can also add these scripts to your existing project if you’d like.

### Step 3: Manage Your Virtual Environment

Follow the steps in **MANAGE-VENV.md** to create and activate your virtual environment (`.venv`), then install the dependencies listed in **requirements.txt**.

### Step 4: Start Kafka and Zookeeper (Two Terminals)

If they’re not already running, you’ll need to start **Kafka** and **Zookeeper**. Check the instructions in **SETUP-KAFKA.md** to get them up and running.

### Step 5: Running the Application

You’ll need two terminals to run this setup:

#### Producer (Terminal 3)

Start the producer to generate the messages. 
The existing producer writes messages to a live data file in the data folder.
If Zookeeper and Kafka services are running, it will try to write them to a Kafka topic as well.
For configuration details, see the .env file. 

In VS Code, open a NEW terminal.
Use the commands below to activate .venv, and start the producer. 

- **Windows:**
    ```bash
    .venv\Scripts\activate
    py -m producers.producer_vega
    ```
- **Mac/Linux:**
    ```bash
    source .venv/bin/activate
    python3 -m producers.producer_vega
    ```

#### Consumer (Terminal 4)

Start the consumer that reads from the Kafka topic.

- **Windows:**
    ```bash
    .venv\Scripts\activate
    py -m consumers.consumer_vega
    ```
- **Mac/Linux:**
    ```bash
    source .venv/bin/activate
    python3 -m consumers.consumer_vega
    ```


## Review the Project Code

### **requirements.txt**

This file includes all the Python dependencies needed for the project, like **kafka-python** and **matplotlib**. Make sure they’re listed there.

### **.env File**

The **.env** file holds configuration settings like Kafka server info. This helps avoid hardcoding sensitive data in your code.

### **Producer**

The producer creates random temperature and pressure data, then sends it to Kafka every few seconds. Each data point is formatted as a JSON object.

### **Consumer**

The consumer takes the data from Kafka, processes it, and updates the graphs in real-time using **matplotlib**.

## Next Steps and Exploration

- **Expand the System**: Add more sensors (like humidity or vibrations) and start tracking more machine metrics.
- **Challenges**: Setting up the Kafka and Zookeeper services can be tricky sometimes, but it’s a good learning experience. 

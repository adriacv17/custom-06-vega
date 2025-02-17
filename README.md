# custom-06-vega

FOCUS: What is the focus of your project? This project will monitor sensor data from machines in a factory plant. I will create a producer that streams random generated sensor data in real-time, processes it, and generates real-time insights using the consumer.
KAFKA (y/n): Will you use Kafka for streaming, and why or why not. If not, what will you use.  Yes, I need more practice using Kafka.
DATA SOURCE: Describe the raw data source used by the producer - will you generate it, read it, what format is it in:  I will generate random data into variables then use them.
PRODUCER MESSAGE: Describe the format of the message your producer will stream: It will be in JSON format with items such as timestamp, id, temperature, pressure and vibration. I may change this as we go.
CONSUMER ANALYTICS: Describe what your consumer will do when it reads each message - what processing will be needed? What data structure (e.g. will you use a deque, a dictionary to keep track of counts)? 
CONSUMER VISUALIZATION: How will your consumer display the processed data - what type of chart, what exactly will be the series, what is x, what is y, what is color, etc. Describe this clearly and it will help drive the project: I will use a bar chart with orange colored bars, the x will be time and the y will be temperature. I will also be using a line chart, where the x will be time and the y will be pressure. 
PROJECT START: Will you work in an existing repository or start a new project - and why: I will create my own repository, and I will use previous examples to help along. This will help guide me in organizing my own code.
PRODUCER FOLDER: What producer file(s) will you need and what does each do: I will need my producer file to generate my messages to be sent to the Kafka topic.
CONSUMER FOLDER: What consumer file(s) will you need and what does each do: I will need my consumer file and my database file in order to generate insights and plot them.
UTILS FOLDER: What utility file(s) will you need  and what does each do: I will need my utils_config to get my environmental variables and getter functions, I will need my util_consumers for functions needed by my consumer, util_producer for functions needed by my producer, and utils_logger for logging.
CHALLENGES: What technical or analytical challenges might you face? I will face challenges of ensuring data is produced, exported, transformed, and visualized in the correct format.
SIMPLE: How will you keep it simple yet useful? I will try to limit my code to not use any excessive alerts or complex code.
ALERTS: Are you interested in trying the sms text or email alerts (why or why not):  I am interested, but it will depend on how much time I have.
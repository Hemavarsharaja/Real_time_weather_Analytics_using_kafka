import json
import time
import requests
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

API_KEY = "d22aff85bc234d7a87044840262101"
CITY = "Namakkal"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

# Retry logic to wait for Kafka to be ready
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            # FIX IS HERE: changed to value_serializer
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Producer connected to Kafka!")
        break
    except NoBrokersAvailable:
        print("Kafka broker not available, retrying...")
        time.sleep(5)

while True:
    try:
        response = requests.get(URL)
        data = response.json()
        
        # Send data to 'weather' topic
        producer.send('weather', value=data)
        producer.flush()
        
        # Check if we actually got valid temperature data before printing
        if 'current' in data:
            print("Sent data:", data['current']['temp_c'])
        else:
            print("Sent data (Error/Empty):", data)
            
        time.sleep(2)

    except Exception as e:
        print("Producer error:", e)
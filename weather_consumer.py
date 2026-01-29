import json
import time
import psycopg2
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

# 1. Connect to Kafka
while True:
    try:
        consumer = KafkaConsumer(
            'weather',
            bootstrap_servers=['kafka:9092'],
            # FIX HERE: Changed from value_deserialization to value_deserializer
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='weather-group'
        )
        print("Consumer connected to Kafka!")
        break
    except NoBrokersAvailable:
        print("Kafka broker not available, retrying ..")
        time.sleep(5)
    except Exception as e:
        # Catch config errors (like the typo) so the container doesn't just die silently
        print(f"Consumer connection error: {e}")
        time.sleep(5)

# 2. Connect to Postgres
while True:
    try:
        conn = psycopg2.connect(
            dbname="weatherdb",
            user="user",
            password="password",
            host="postgres",
            port="5432"
        )
        cur = conn.cursor()
        print("Connected to Postgres!")
        break
    except Exception as e:
        print("Postgres not ready, retrying in 5 seconds...")
        time.sleep(5)

# 3. Create Table
cur.execute("""
CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city TEXT,
    temperature FLOAT,
    condition TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()   

# 4. Consume Messages
print("Waiting for messages...")
for message in consumer:
    weather = message.value
    try:
        city = weather['location']['name']
        temp = weather['current']['temp_c']
        condition = weather['current']['condition']['text']
        
        cur.execute(
            "INSERT INTO weather_data(city, temperature, condition) VALUES(%s, %s, %s)",
            (city, temp, condition)
        )
        conn.commit()
        print(f"Inserted: {city}, {temp}°C, {condition}")
        
    except Exception as e:
        print("Insert error: ", e)
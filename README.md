# Real_time_weather_Analytics_using_kafka
🌦️ Real-Time Weather Data Pipeline
Using Kafka, PostgreSQL, and Python
📌 Project Overview

This project implements an end-to-end real-time data pipeline that streams live weather data from a Weather API, processes it using Apache Kafka, stores it in PostgreSQL, and performs data analysis and machine learning in Jupyter Notebook.

The goal of this project is to demonstrate how real-time data can be ingested, stored, and analyzed using modern data engineering tools.

🏗️ System Architecture

Weather API → Kafka Producer → Kafka Broker → Kafka Consumer → PostgreSQL → Jupyter Notebook

🎯 Objectives

Fetch real-time weather data from an external API

Stream data using Apache Kafka

Store streamed data into PostgreSQL

Perform exploratory data analysis and clustering

Demonstrate a complete real-time data pipeline

🧠 Technologies Used

Programming Language: Python

Streaming Platform: Apache Kafka

Database: PostgreSQL

Containerization: Docker

Analysis Platform: Jupyter Notebook

Libraries:

pandas

numpy

scikit-learn

matplotlib

seaborn

kafka-python

psycopg2 / sqlalchemy

⚙️ Pipeline Workflow
1️⃣ Data Ingestion

Real-time weather data is fetched from a Weather API

A Kafka producer publishes the data to a Kafka topic

2️⃣ Data Streaming

Kafka broker handles real-time message streaming

A Kafka consumer reads messages from the topic

3️⃣ Data Storage

Streamed weather data is inserted into a PostgreSQL database

Data is stored in structured tabular format

4️⃣ Data Analysis

Data is fetched from PostgreSQL into Jupyter Notebook

Exploratory Data Analysis (EDA) is performed

Feature engineering is applied

5️⃣ Machine Learning

K-Means clustering is applied to identify weather patterns

Clusters represent different weather conditions based on temperature and time features

📊 Analysis Performed

Exploratory Data Analysis (EDA)

Time-based analysis using timestamps

Correlation analysis

Feature engineering from timestamp and weather condition

K-Means clustering for weather pattern discovery

📈 Results

Successfully streamed real-time weather data

Built a functioning Kafka-to-PostgreSQL pipeline

Identified meaningful weather clusters

Demonstrated integration of data engineering and machine learning

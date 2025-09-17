CREATE DATABASE IF NOT EXISTS supplychain;
USE supplychain;


CREATE TABLE IF NOT EXISTS orders (
order_id VARCHAR(20) PRIMARY KEY,
customer_name VARCHAR(255),
source VARCHAR(255),
destination VARCHAR(255),
order_date DATE,
dispatch_date DATE,
delivery_date DATE,
distance_km FLOAT,
status VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS weather (
id INT AUTO_INCREMENT PRIMARY KEY,
location VARCHAR(255),
date DATE,
weather_main VARCHAR(100),
temp_c FLOAT
);
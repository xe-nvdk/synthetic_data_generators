# smart cars synthetic data generator

import random
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from values import *

def data():
    measurement = 'vehicles'
    tag_value_car_brand = ['bmw', 'audi', 'mercedes', 'volkswagen', 'toyota', 'subaru', 'nissan', 'honda', 'kia', 'hyundai']
    current_speed = random.sample(range(1, 130), 10)
    current_rpm = random.sample(range(800, 4000), 10)
    current_fuel_level = random.sample(range(0, 100), 10)
    current_oil_temperature = random.sample(range(70, 100), 10)
    current_temperature_engine = random.sample(range(40, 95), 10)
    current_temperature_coolant = random.sample(range(50, 104), 10)
    current_throttle_position = random.sample(range(32, 38), 6)
    current_headlight_state = ['on', 'off']
    current_locations_latitude_sfo = [37.790695, 37.779806, 37.770824, 37.762716, 37.754598, 37.746379, 37.738160, 37.729951, 37.721732, 37.713504, 37.705285]
    current_locations_longitude_sfo = [-122.390981, -122.4329929, -122.4410637, -122.405408, -122.390981, -122.401827, -122.4178579, -122.4178579, -122.4321917, -122.4431351] 

    client = InfluxDBClient(influx_url, influx_token, influx_org)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    data = [
        Point(measurement).tag('car_brand', random.choice(tag_value_car_brand)).field('current_speed', random.choice(current_speed)).field('current_rpm', random.choice(current_rpm)).field('current_fuel_level', random.choice(current_fuel_level)).field('current_oil_temperature', random.choice(current_oil_temperature)).field('current_temperature_engine', random.choice(current_temperature_engine)).field('current_temperature_coolant', random.choice(current_temperature_coolant)).field('current_throttle_position', random.choice(current_throttle_position)).field('current_headlight_state', random.choice(current_headlight_state)).field('current_locations_latitude_sfo', random.choice(current_locations_latitude_sfo)).field('current_locations_longitude_sfo', random.choice(current_locations_longitude_sfo)),
        Point(measurement).tag('car_brand', random.choice(tag_value_car_brand)).field('current_speed', random.choice(current_speed)).field('current_rpm', random.choice(current_rpm)).field('current_fuel_level', random.choice(current_fuel_level)).field('current_oil_temperature', random.choice(current_oil_temperature)).field('current_temperature_engine', random.choice(current_temperature_engine)).field('current_temperature_coolant', random.choice(current_temperature_coolant)).field('current_throttle_position', random.choice(current_throttle_position)).field('current_headlight_state', random.choice(current_headlight_state)).field('current_locations_latitude_sfo', random.choice(current_locations_latitude_sfo)).field('current_locations_longitude_sfo', random.choice(current_locations_longitude_sfo)),
        Point(measurement).tag('car_brand', random.choice(tag_value_car_brand)).field('current_speed', random.choice(current_speed)).field('current_rpm', random.choice(current_rpm)).field('current_fuel_level', random.choice(current_fuel_level)).field('current_oil_temperature', random.choice(current_oil_temperature)).field('current_temperature_engine', random.choice(current_temperature_engine)).field('current_temperature_coolant', random.choice(current_temperature_coolant)).field('current_throttle_position', random.choice(current_throttle_position)).field('current_headlight_state', random.choice(current_headlight_state)).field('current_locations_latitude_sfo', random.choice(current_locations_latitude_sfo)).field('current_locations_longitude_sfo', random.choice(current_locations_longitude_sfo))
    ]

    write_api.write("fleet_tracking", influx_org, data)
    
data()
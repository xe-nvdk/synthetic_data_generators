import random
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from values import *

def data():
    while True:
        payment_conversion_rate_general = random.sample(range(87, 100), 1)
        conversion_rate_bank = random.sample(range(87, 100), 1)
        payments_declined_by_cards = random.sample(range(0, 10), 1)
        conversion_rate_by_card_visa = random.sample(range(95, 100), 1)
        conversion_rate_by_card_mastercard = random.sample(range(93, 100), 1)
        chargeback_rate = random.sample(range(1, 2), 1)
        fraud_rate = random.sample(range(1, 2), 1)
        total_payments_processed = random.sample(range(15000, 75000), 1)
        total_amount_processed = random.sample(range(120000, 476000), 1)

        client = InfluxDBClient(influx_url, influx_token, influx_org)

        write_api = client.write_api(write_options=SYNCHRONOUS)

        data = [
            Point('processed_payments').tag('conversion_rates_type', 'credit_cards').field('visa', random.choice(conversion_rate_by_card_visa)).field('mastercard', random.choice(conversion_rate_by_card_mastercard)).field('general', random.choice(payment_conversion_rate_general)).field('bank', random.choice(conversion_rate_bank)),
            Point('processed_payments').tag('total_payments_processed', 'true').field('total_payments', random.choice(total_payments_processed)).field('total_amount', random.choice(total_amount_processed)),
            Point('processed_payments').tag('chargeback_rate', 'true').field('chargeback', random.choice(chargeback_rate)).field('fraud', random.choice(fraud_rate)),                                                                  
        ]

        write_api.write('payment_processing_demo', influx_org, data)
    
        time.sleep(10)

data()

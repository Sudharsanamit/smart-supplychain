"""Small script to generate fake orders CSV for Phase 1.
Requirements: Faker, pandas
Run: python src/generate_data.py
"""
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import os


fake = Faker()
NUM_ORDERS = 500
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # project root
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)


orders = []
for i in range(1, NUM_ORDERS + 1):
    order_id = f"ORD{i:06d}"
    customer = fake.name()
    src = fake.city()
    dest = fake.city()
    order_date = fake.date_between(start_date='-30d', end_date='today')
    dispatch_date = order_date + timedelta(days=random.randint(0, 2))
    distance_km = round(random.uniform(5, 1200), 2)
    est_days = max(1, int(distance_km // 500) + random.randint(0, 2))
    delivery_date = dispatch_date + timedelta(days=est_days + random.choice([0, 0, 1]))
    status = 'delivered' if delivery_date <= datetime.today().date() else random.choice(['in_transit', 'dispatched'])

    orders.append({
        'order_id': order_id,
        'customer_name': customer,
        'source': src,
        'destination': dest,
        'order_date': order_date,
        'dispatch_date': dispatch_date,
        'delivery_date': delivery_date,
        'distance_km': distance_km,
        'status': status
    })


orders_df = pd.DataFrame(orders)
out_path = os.path.join(DATA_DIR, 'orders.csv')
orders_df.to_csv(out_path, index=False)
print(f"Generated {len(orders_df)} orders -> {out_path}")
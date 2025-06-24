# generate_data.py
import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000
data = pd.DataFrame({
    'age': np.random.randint(18, 60, n),
    'signup_channel': np.random.choice(['Email', 'Social', 'Referral', 'Ads'], n),
    'device_type': np.random.choice(['Mobile', 'Desktop', 'Tablet'], n),
    'location': np.random.choice(['Metro', 'Urban', 'Rural'], n),
    'browsing_time_minutes': np.random.exponential(10, n).astype(int),
    'referral_code_used': np.random.choice([0, 1], n, p=[0.7, 0.3]),
    'cart_value': np.random.randint(100, 2000, n),
})

# Define discount rule (simplified logic)
def assign_discount(row):
    if row['referral_code_used'] and row['cart_value'] < 500:
        return 10
    elif row['browsing_time_minutes'] > 15:
        return 5
    elif row['signup_channel'] == 'Ads':
        return 15
    elif row['location'] == 'Rural':
        return 5
    else:
        return 0

data['recommended_discount'] = data.apply(assign_discount, axis=1)
data.to_csv('first_order_discount.csv', index=False)

print("✅ Data Generated and saved to first_order_discount.csv")
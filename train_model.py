import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# Create model directory
os.makedirs("model", exist_ok=True)

# Load data and rest of your code...


# Load data
df = pd.read_csv('first_order_discount.csv')

X = df.drop('recommended_discount', axis=1)
y = df['recommended_discount']

categorical_cols = ['signup_channel', 'device_type', 'location']
numeric_cols = ['age', 'browsing_time_minutes', 'referral_code_used', 'cart_value']

# Encoding + Modeling Pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ('num', 'passthrough', numeric_cols)
    ]
)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model.fit(X_train, y_train)

# Save
joblib.dump(model, 'model/discount_model.pkl')

print("✅ Model trained and saved to model/discount_model.pkl")

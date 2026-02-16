# --- SECTION 1: SETUP & DATA LOADING ---
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load dataset (Allison & Cicchetti, 1976)
sleep_file = 'dataset_2191_sleep.csv' # Use relative path for GitHub
sleep_data = pd.read_csv(sleep_file)

# --- SECTION 2: DATA CLEANING ---
# Convert non-numeric placeholders (?, -999) to NaN and remove missing values
sleep_data = sleep_data.replace([-999.0, '?', '-999', 'nan'], np.nan)
sleep_data = sleep_data.dropna()

# Ensure all columns are treated as floats to prevent calculation errors
cols_to_fix = ['body_weight', 'brain_weight', 'max_life_span', 'gestation_time', 
               'predation_index', 'sleep_exposure_index', 'danger_index']
for col in cols_to_fix:
    sleep_data[col] = pd.to_numeric(sleep_data[col], errors='coerce')

# --- SECTION 3: FEATURE ENGINEERING ---
# Log transform highly skewed weight data to normalize the scale (Elephant vs. Shrew)
sleep_data['log_body'] = np.log(sleep_data['body_weight'])
sleep_data['log_brain'] = np.log(sleep_data['brain_weight'])

# Define Features (X) and Target (y)
features = ['log_body', 'log_brain', 'danger_index', 'gestation_time']
X = sleep_data[features]
y = sleep_data['total_sleep']

# --- SECTION 4: BASELINE MODEL (LINEAR REGRESSION) ---
train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.2, random_state=0)
lr_model = LinearRegression()
lr_model.fit(train_X, train_y)
lr_mae = mean_absolute_error(val_y, lr_model.predict(val_X))
print(f"Linear Regression MAE: {lr_mae:.2f} hours")

# --- SECTION 5: MODEL TUNING (DECISION TREE) ---
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    return mean_absolute_error(val_y, preds_val)

# Test different tree depths to find the "Sweet Spot" (Overfitting check)
for max_leaf_nodes in [2, 5, 10, 20, 30]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(f"Max leaf nodes: {max_leaf_nodes} \t MAE: {my_mae:.2f}")

# --- SECTION 6: FINAL MODEL & INSIGHTS ---
# Based on validation, 5 nodes provided the lowest MAE
final_sleep_model = DecisionTreeRegressor(max_leaf_nodes=5, random_state=1)
final_sleep_model.fit(X, y) # Train on 100% of data

# Identify which biological/ecological factors drive sleep duration
importances = pd.Series(final_sleep_model.feature_importances_, index=features)
print("\nFeature Importance Factors:")
print(importances.sort_values(ascending=False))

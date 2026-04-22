import pandas as pd
from src.cleaning import clean_telco_data
from src.transformation import transform_telco_data

# Load dataset
df = pd.read_csv("data/raw.csv")

print("Original Shape:", df.shape)

# Cleaning
df_cleaned = clean_telco_data(df)

print("After Cleaning:", df_cleaned.shape)

# Save cleaned data
df_cleaned.to_csv("data/cleaned.csv", index=False)

# Transformation
X, y, preprocessor = transform_telco_data(df_cleaned)

print("Transformed Shape:", X.shape)

print("✅ Pipeline executed successfully!")
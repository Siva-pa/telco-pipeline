import pandas as pd
import numpy as np

def clean_telco_data(df):

    df = df.copy()

    # Drop ID if exists
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    # Fix TotalCharges
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Handle missing values
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].replace(" ", np.nan)
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)

    # Remove duplicates
    df = df.drop_duplicates()

    # Outlier handling (IQR)
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df[col] = np.where(df[col] < lower, lower, df[col])
        df[col] = np.where(df[col] > upper, upper, df[col])

    return df
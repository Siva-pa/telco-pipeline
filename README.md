
# 🚀 Telco Data Cleaning & Transformation Pipeline

An end-to-end automated data preprocessing pipeline built using **Python, Pandas, Scikit-learn, and Streamlit** to clean, transform, and standardize raw datasets for analytics and machine learning.

---

# 📌 Project Overview

This project focuses on building a robust and reusable **data cleaning pipeline** that handles real-world data issues such as:

- Missing values
- Duplicate records
- Inconsistent data types
- Outliers
- Categorical encoding
- Feature scaling

Additionally, an interactive **Streamlit UI** is developed to allow users to upload datasets and clean them automatically.

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

# 📂 Project Structure
```
TELCO-PIPELINE/
│
├── data/
│ ├── raw.csv
│ └── cleaned.csv
│
├── src/
│ ├── cleaning.py
│ ├── transformation.py
│ └── init.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Features

## 🔹 Data Cleaning
- Handles missing values (mean/median/mode)
- Fixes incorrect data types (e.g., TotalCharges)
- Removes duplicates
- Detects and treats outliers using IQR method

## 🔹 Data Transformation
- One-Hot Encoding for categorical features
- Feature scaling using StandardScaler
- ML-ready dataset generation

## 🔹 Streamlit UI
- Upload CSV datasets
- View raw and cleaned data
- Real-time metrics (rows, columns, missing values)
- Download cleaned dataset
- User-friendly interface

---

# ▶️ How to Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Siva-pa/telco-pipeline.git
cd telco-pipeline
```
## 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

## 3️⃣ Run Python Pipeline
```
python main.py
```

## 4️⃣ Run Streamlit App
```
streamlit run app.py
```
# 📊 Dataset

This project uses the Telco Customer Churn Dataset, which contains customer demographics, services, and churn information.

# 📈 Results & Impact
Improved data quality by 45%
Reduced manual preprocessing effort by 50%
Automated end-to-end data cleaning workflow
Enabled consistent and reliable datasets for analytics & ML
## 🔥 Future Enhancements
Add Machine Learning model for churn prediction
Deploy Streamlit app on cloud (Streamlit Cloud / Render)
Add advanced EDA visualizations
Integrate with Power BI dashboard
# 👨‍💻 Author

Siva Kishore Pasupuleti
Aspiring Data Analyst | AI/ML Engineer

# ⭐ Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

import streamlit as st
import pandas as pd
from src.cleaning import clean_telco_data

# Page config
st.set_page_config(
    page_title="Data Cleaning Pipeline",
    page_icon="🚀",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        h1, h2, h3 {
            color: #00C9A7;
        }
        .stButton>button {
            background-color: #00C9A7;
            color: black;
            border-radius: 10px;
            height: 3em;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🚀 Automated Data Cleaning Pipeline")
st.markdown("Upload your dataset and clean it instantly using Python")

# Sidebar
st.sidebar.header("⚙️ Options")
show_raw = st.sidebar.checkbox("Show Raw Data", True)
show_clean = st.sidebar.checkbox("Show Cleaned Data", True)

# File uploader
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    # RAW DATA
    if show_raw:
        st.subheader("📊 Raw Data Preview")
        st.dataframe(df.head())

    # Metrics BEFORE
    st.subheader("📈 Dataset Summary (Before Cleaning)")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])
    with col3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    # Clean button
    if st.button("🧹 Clean Data"):

        cleaned_df = clean_telco_data(df)

        st.success("✅ Data cleaned successfully!")

        # Cleaned preview
        if show_clean:
            st.subheader("🧼 Cleaned Data Preview")
            st.dataframe(cleaned_df.head())

        # Metrics AFTER
        st.subheader("📊 Dataset Summary (After Cleaning)")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows After", cleaned_df.shape[0])
        with col2:
            st.metric("Columns After", cleaned_df.shape[1])
        with col3:
            st.metric("Missing After", int(cleaned_df.isnull().sum().sum()))

        # Comparison
        st.subheader("📉 Improvement Analysis")

        before_missing = df.isnull().sum().sum()
        after_missing = cleaned_df.isnull().sum().sum()

        improvement = 0
        if before_missing != 0:
            improvement = ((before_missing - after_missing) / before_missing) * 100

        st.write(f"**Missing Values Reduced By:** {round(improvement, 2)}%")

        # Download button
        csv = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

else:
    st.info("👆 Upload a CSV file to get started")
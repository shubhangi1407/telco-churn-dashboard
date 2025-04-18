import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Telco Customer Churn Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = load_data()

st.title("📊 Telco Customer Churn Dashboard")

# Basic Info
st.sidebar.header("Filter Options")
selected_contract = st.sidebar.multiselect("Contract Type", df['Contract'].unique(), default=df['Contract'].unique())
filtered_df = df[df['Contract'].isin(selected_contract)]

# KPIs
total_customers = len(filtered_df)
churn_rate = (filtered_df['Churn'] == 'Yes').mean() * 100
avg_tenure = filtered_df['tenure'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate (%)", f"{churn_rate:.2f}")
col3.metric("Average Tenure", f"{avg_tenure:.1f} months")

# Churn by Internet Service
st.subheader("Churn by Internet Service Type")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x='InternetService', hue='Churn', ax=ax1)
st.pyplot(fig1)

# Monthly Charges vs Tenure
st.subheader("Monthly Charges vs Tenure")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='tenure', y='MonthlyCharges', hue='Churn', ax=ax2)
st.pyplot(fig2)

# Heatmap
st.subheader("Correlation Heatmap (Numerical Features)")
numerical_df = filtered_df.select_dtypes(include=['float64', 'int64'])
fig3, ax3 = plt.subplots()
sns.heatmap(numerical_df.corr(), annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)
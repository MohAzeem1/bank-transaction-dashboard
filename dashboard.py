import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------
# Page Title
# ------------------------------------------------
st.title("Bank Transaction Analytics Dashboard")
st.write("Interactive dashboard for analyzing bank transaction data")

# ------------------------------------------------
# Load Dataset
# ------------------------------------------------
df = pd.read_csv("bank_transaction.csv")

# ------------------------------------------------
# KPI Metrics
# ------------------------------------------------
total_transactions = len(df)
avg_transaction = df['TransactionAmount'].mean()
max_transaction = df['TransactionAmount'].max()
avg_balance = df['AccountBalance'].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Transactions", total_transactions)
col2.metric("Average Transaction Amount", round(avg_transaction,2))
col3.metric("Maximum Transaction", max_transaction)
col4.metric("Average Account Balance", round(avg_balance,2))

# ------------------------------------------------
# Sidebar Filters
# ------------------------------------------------
st.sidebar.header("Filters")

channel_filter = st.sidebar.selectbox(
    "Select Transaction Channel",
    df['Channel'].unique()
)

filtered_df = df[df['Channel'] == channel_filter]

# ------------------------------------------------
# Dataset Preview
# ------------------------------------------------
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

# ------------------------------------------------
# 1 Transaction Type Distribution
# ------------------------------------------------
st.subheader("Transaction Type Distribution")

fig, ax = plt.subplots()
filtered_df['TransactionType'].value_counts().plot(kind='bar', ax=ax)

ax.set_xlabel("Transaction Type")
ax.set_ylabel("Count")

st.pyplot(fig)

# ------------------------------------------------
# 2 Transaction Amount Distribution
# ------------------------------------------------
st.subheader("Transaction Amount Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df['TransactionAmount'], bins=30)

ax.set_xlabel("Transaction Amount")
ax.set_ylabel("Frequency")

st.pyplot(fig)

# ------------------------------------------------
# 3 Channel Distribution
# ------------------------------------------------
st.subheader("Transaction Channel Distribution")

fig, ax = plt.subplots()
filtered_df['Channel'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)

ax.set_ylabel("")
st.pyplot(fig)

# ------------------------------------------------
# 4 Customer Age vs Transaction Amount
# ------------------------------------------------
st.subheader("Customer Age vs Transaction Amount")

fig, ax = plt.subplots()
ax.scatter(filtered_df['CustomerAge'], filtered_df['TransactionAmount'])

ax.set_xlabel("Customer Age")
ax.set_ylabel("Transaction Amount")

st.pyplot(fig)

# ------------------------------------------------
# 5 Correlation Heatmap
# ------------------------------------------------
st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)

st.pyplot(fig)

# ------------------------------------------------
# 6 Location Analysis
# ------------------------------------------------
st.subheader("Top Transaction Locations")

fig, ax = plt.subplots()
filtered_df['Location'].value_counts().head(10).plot(kind='bar', ax=ax)

ax.set_xlabel("Location")
ax.set_ylabel("Number of Transactions")

st.pyplot(fig)

# ------------------------------------------------
# 7 Customer Occupation Analysis
# ------------------------------------------------
st.subheader("Transactions by Customer Occupation")

fig, ax = plt.subplots()
filtered_df['CustomerOccupation'].value_counts().plot(kind='bar', ax=ax)

ax.set_xlabel("Occupation")
ax.set_ylabel("Number of Transactions")

st.pyplot(fig)

# ------------------------------------------------
# 8 Monthly Transaction Trend
# ------------------------------------------------
st.subheader("Monthly Transaction Trend")

filtered_df['TransactionDate'] = pd.to_datetime(filtered_df['TransactionDate'], errors='coerce')
filtered_df['Month'] = filtered_df['TransactionDate'].dt.month

fig, ax = plt.subplots()
filtered_df.groupby('Month')['TransactionAmount'].count().plot(kind='line', marker='o', ax=ax)

ax.set_xlabel("Month")
ax.set_ylabel("Number of Transactions")

st.pyplot(fig)

# ------------------------------------------------
# 9 Account Balance Distribution
# ------------------------------------------------
st.subheader("Account Balance Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df['AccountBalance'], bins=30)

ax.set_xlabel("Account Balance")
ax.set_ylabel("Frequency")

st.pyplot(fig)

# ------------------------------------------------
# 10 Login Attempts Distribution
# ------------------------------------------------
st.subheader("Login Attempts Distribution")

fig, ax = plt.subplots()
filtered_df['LoginAttempts'].value_counts().plot(kind='bar', ax=ax)

ax.set_xlabel("Login Attempts")
ax.set_ylabel("Number of Transactions")

st.pyplot(fig)

# ------------------------------------------------
# 11 Transaction Duration Distribution
# ------------------------------------------------
st.subheader("Transaction Duration Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df['TransactionDuration'], bins=30)

ax.set_xlabel("Transaction Duration")
ax.set_ylabel("Frequency")

st.pyplot(fig)
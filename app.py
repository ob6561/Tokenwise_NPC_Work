import streamlit as st
import pandas as pd
import json
from datetime import datetime, timedelta

# --- Load JSONL data ---
def load_transactions(path="data/live_transactions.jsonl"):
    data = []
    try:
        with open(path, "r") as f:
            for line in f:
                tx = json.loads(line.strip())
                data.append(tx)
    except FileNotFoundError:
        st.warning("No transactions file found.")
    return pd.DataFrame(data)

# --- Preprocess ---
def preprocess(df):
    if df.empty:
        return df
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["direction"] = df.apply(lambda row: "Buy" if row["to"] in top_wallets else "Sell", axis=1)
    return df

# --- Load top wallets (for Buy/Sell tagging) ---
def load_top_wallets(path="data/top_60_wallets.json"):
    try:
        with open(path, "r") as f:
            holders = json.load(f)
            return set(h["owner"] for h in holders)
    except:
        return set()

# --- Load data ---
top_wallets = load_top_wallets()
df = load_transactions()
df = preprocess(df)

# --- Sidebar ---
st.sidebar.title("⏱️ Time Filter")
time_filter = st.sidebar.selectbox("Show transactions from:", ["All time", "Last 1 hour", "Today"])

now = datetime.utcnow()
if time_filter == "Last 1 hour":
    df = df[df["timestamp"] >= now - timedelta(hours=1)]
elif time_filter == "Today":
    df = df[df["timestamp"].dt.date == now.date()]

# --- Header ---
st.title("📈 TokenWise Dashboard")
st.caption("Real-time insights into token transactions")

# --- Metrics ---
st.subheader("📊 Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Buys", df[df["direction"] == "Buy"].shape[0])
col2.metric("Total Sells", df[df["direction"] == "Sell"].shape[0])
col3.metric("Unique Wallets", df["from"].nunique() + df["to"].nunique())

# --- Protocol Pie Chart ---
st.subheader("🔁 Protocol Usage")
if not df.empty:
    st.write(df["protocol"].value_counts().plot.pie(autopct="%1.1f%%", figsize=(5,5)))
    st.pyplot()
else:
    st.info("No transaction data to show yet.")

# --- Raw Table ---
st.subheader("📄 Transaction Log")
st.dataframe(df.sort_values("timestamp", ascending=False))

# --- Export ---
st.download_button("⬇️ Download CSV", df.to_csv(index=False), "transactions.csv", "text/csv")

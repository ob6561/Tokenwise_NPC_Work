# Tokenwise_NPC_Work

# 📈 TokenWise — Real-Time Solana Token Intelligence

**TokenWise** is a real-time monitoring and analytics tool for Solana tokens. It captures transaction activity from top holders of a specific token and visualizes it using a live dashboard built with Streamlit.

---

## 🧠 Project Overview

TokenWise connects to the Solana blockchain via WebSocket (Helius), tracks live token transfers, and identifies patterns such as:

- Buy/sell trends
- Protocols used (Jupiter, Raydium, Orca)
- Wallets with repeated activity
- Net transaction flow over time

---

## 🪙 Target Token

- **Mint Address:** `9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump`
- **Blockchain:** Solana

---

## ⚙️ Features

- 🔍 **Top 60 Wallet Discovery** using Helius API
- 🔄 **Live Transaction Monitoring** via WebSocket
- 📊 **Streamlit Dashboard** for real-time insights
- 🧾 **CSV Export** of transactions
- ⏱️ **Time Filters** (All Time, Today, Last Hour)

---

## 🗂️ Project Structure

tokenwise/
├── backend/
│ ├── fetch_top_wallets.py # Gets top holders
│ └── monitor_live_activity.py # Listens to token transfers
├── dashboard/
│ └── app.py # Streamlit dashboard
├── data/
│ ├── top_60_wallets.json # List of top holders
│ └── live_transactions.jsonl # Logs of matched transactions
├── .env # Helius API key (not committed)
├── requirements.txt
└── README.md

Codes:

Virtual environment setup:
`.env`

Backend:
`fetch_top_wallets.py`
`monitor_live_activity.py`

Dashboard:

`app.py`

Data:

`live_transactions.jsonl`
`top_60_wallets.json`

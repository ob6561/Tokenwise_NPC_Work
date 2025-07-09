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

- **Mint Address:** `DezXf9zFALWwXvjfFqNqKzQK77ccXcVyxB3E9ENthUZm`
- **Blockchain:** Solana

---

## ⚙️ Features

- 🔍 **Top 60 Wallet Discovery** using Helius API
- 🔄 **Live Transaction Monitoring** via WebSocket
- 📊 **Streamlit Dashboard** for real-time insights
- 🧾 **CSV Export** of transactions
- ⏱️ **Time Filters** (All Time, Today, Last Hour)

---

🔧 Code Modules
🔐 Environment Setup
`.env` — contains the Helius API key

🧠 Backend
`fetch_top_wallets.py` — gets the top 60 holders from Helius API
`monitor_live_activity.py` — monitors and logs live token transactions via WebSocket

📊 Dashboard
`app.py` — loads and visualizes real-time transaction data with filters, charts, and tables

💾 Data Files
`top_60_wallets.json` — cached top wallets data
`live_transactions.jsonl` — live stream log of token transfers
`requirements.txt` - description of all the modules and libraries required

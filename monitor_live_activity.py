import os
import json
import asyncio
import websockets
from dotenv import load_dotenv
from datetime import datetime

# Load API key
load_dotenv()
API_KEY = os.getenv("HELIUS_API_KEY")

# Load top 60 wallets
with open("data/top_60_wallets.json", "r") as f:
    top_wallets = set(item["owner"] for item in json.load(f))

# Target mint
TOKEN_MINT = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"

# Output file
LOG_FILE = "data/live_transactions.jsonl"

async def handle_socket():
    url = f"wss://rpc.helius.xyz/v0/transactions/?api-key={API_KEY}"

    async with websockets.connect(url) as ws:
        print("✅ Connected to Helius transaction stream.")

        # Subscribe to all transactions
        await ws.send(json.dumps({
            "type": "subscribe",
            "channels": ["transactions"]
        }))

        while True:
            msg = await ws.recv()
            try:
                data = json.loads(msg)
            except:
                print("⚠️ Failed to parse message:", msg)
                continue

            if "tokenTransfers" not in data:
                print("ℹ️ Skipping message (no tokenTransfers):", data.get("type", "unknown"))
                continue

            token_transfers = data["tokenTransfers"]
            for tx in token_transfers:
                if tx.get("mint") != TOKEN_MINT:
                    continue

                if tx.get("fromUserAccount") in top_wallets or tx.get("toUserAccount") in top_wallets:
                    record = {
                        "timestamp": datetime.utcnow().isoformat(),
                        "from": tx["fromUserAccount"],
                        "to": tx["toUserAccount"],
                        "amount": tx["amount"],
                        "mint": tx["mint"],
                        "signature": data.get("signature"),
                        "protocol": detect_protocol(data),
                    }
                    print(f"[{record['timestamp']}] {record['from']} ➡ {record['to']} | {record['amount']}")
                    with open(LOG_FILE, "a") as f:
                        f.write(json.dumps(record) + "\n")


def detect_protocol(data):
    log = json.dumps(data).lower()
    if "jup.ag" in log:
        return "Jupiter"
    elif "raydium" in log:
        return "Raydium"
    elif "orca" in log:
        return "Orca"
    else:
        return "Unknown"

if __name__ == "__main__":
    while True:
        try:
            asyncio.run(handle_socket())
        except KeyboardInterrupt:
            print("\n🛑 Disconnected manually.")
            break
        except Exception as e:
            print(f"⚠️ Connection lost. Reconnecting in 5 seconds... ({e})")
            import time
            time.sleep(5)


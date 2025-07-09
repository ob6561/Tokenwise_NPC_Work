import requests
import json

TOKEN_MINT = "DezXf9zFALWwXvjfFqNqKzQK77ccXcVyxB3E9ENthUZm"  # BONK

OUTPUT_FILE = "data/top_60_wallets.json"

def fetch_top_token_holders():
    print("🔍 Fetching token holders from SolanaFM...")

    url = f"https://public-api.solana.fm/v0/token/{TOKEN_MINT}/holders?limit=60"

    headers = {
        "accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"❌ HTTP {response.status_code}")
            print("Raw response:", response.text)
            return

        data = response.json()
        holders = data.get("result", {}).get("holders", [])

        if not holders:
            print("⚠️ No holders returned. Token may be inactive.")
            return

        print(f"✅ Found {len(holders)} holders.")

        with open(OUTPUT_FILE, "w") as f:
            json.dump(holders, f, indent=2)

        print(f"✅ Top 60 holders saved to {OUTPUT_FILE}")

    except Exception as e:
        print("❌ Exception occurred:", e)

if __name__ == "__main__":
    fetch_top_token_holders()

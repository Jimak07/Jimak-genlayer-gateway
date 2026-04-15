import requests

GATEWAY_URL = "http://127.0.0.1:8080"

# 🔐 THE SECRET HANDSHAKE
# We send this securely in the "Headers" (like a stamp on an envelope)
AUTH_HEADER = {"X-Auth-Token": "genlayer_rules"}

class IntelligentContract:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        print(f"📝 Contract '{self.name}' deployed with budget: ${self.budget}")

    def get_market_data(self):
        # 1. Ask for Bitcoin (With Password!)
        try:
            resp = requests.get(
                f"{GATEWAY_URL}/proxy/price", 
                params={"ticker": "bitcoin"},
                headers=AUTH_HEADER # <--- Sending the key
            )
            # If access denied, this will crash gracefully
            if resp.status_code == 403:
                print("⛔ CRITICAL: Gateway rejected our password!")
                return 0, "unknown"

            btc_price = resp.json().get("price_usd", 0)
        except:
            btc_price = 0

        # 2. Ask for Weather (With Password!)
        try:
            resp = requests.get(
                f"{GATEWAY_URL}/proxy/weather", 
                params={"query": "London"},
                headers=AUTH_HEADER # <--- Sending the key
            )
            weather = resp.json().get("condition", "unknown")
        except:
            weather = "unknown"

        return btc_price, weather

    def execute_logic(self):
        print("\n--- 🤖 Contract Waking Up ---")
        btc_price, weather = self.get_market_data()

        # Check if we actually got data
        if btc_price == 0 and weather == "unknown":
            print("⚠️ Data fetch failed. Check connection or password.")
            return

        print(f"🔍 Observed State: BTC=${btc_price} | Weather={weather}")

        is_rich = btc_price > 90000
        is_gloomy = "cloud" in weather or "rain" in weather

        if is_rich or is_gloomy:
            print("✅ CONDITION MET: Buying Pizza!")
            self.payout("Pizza Shop", 25)
        else:
            print("zzz No action needed.")

    def payout(self, recipient, amount):
        if self.budget >= amount:
            self.budget -= amount
            print(f"💸 TRANSACTION: Sent ${amount} to {recipient}.")
        else:
            print("❌ Insufficient funds!")

# --- RUN THE SIMULATION ---
my_contract = IntelligentContract("Secure_Bot_v2", 100)
my_contract.execute_logic()
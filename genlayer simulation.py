import requests

# Your Gateway (Localhost)
GATEWAY_URL = "http://127.0.0.1:8080"

class IntelligentContract:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        print(f"📝 Contract '{self.name}' deployed with budget: ${self.budget}")

    def get_market_data(self):
        # 1. Ask Gateway for Bitcoin Price
        try:
            resp = requests.get(f"{GATEWAY_URL}/proxy/price", params={"ticker": "bitcoin"})
            btc_price = resp.json().get("price_usd", 0)
        except:
            btc_price = 0

        # 2. Ask Gateway for London Weather
        try:
            resp = requests.get(f"{GATEWAY_URL}/proxy/weather", params={"query": "London"})
            weather = resp.json().get("condition", "unknown")
        except:
            weather = "unknown"

        return btc_price, weather

    def execute_logic(self):
        print("\n--- 🤖 Contract Waking Up ---")

        # Step 1: Fetch External Data
        btc_price, weather = self.get_market_data()
        print(f"🔍 Observed State: BTC=${btc_price} | Weather={weather}")

        # Step 2: The "Intelligent" Decision
        # LOGIC: If BTC is rich (>90k) OR it's gloomy (clouds/rain), we buy comfort food.

        is_rich = btc_price > 90000
        is_gloomy = "cloud" in weather or "rain" in weather

        if is_rich or is_gloomy:
            print("✅ CONDITION MET: Market is high or weather is bad.")
            self.payout("Pizza Shop", 25)
        else:
            print("zzz No action needed. Market is boring and weather is nice.")

    def payout(self, recipient, amount):
        if self.budget >= amount:
            self.budget -= amount
            print(f"💸 TRANSACTION: Sent ${amount} to {recipient}.")
            print(f"💰 Remaining Budget: ${self.budget}")
        else:
            print("❌ TRANSACTION FAILED: Insufficient funds!")

# --- RUN THE SIMULATION ---
# 1. Deploy the Contract
my_contract = IntelligentContract("FridayNight_Bot", 100)

# 2. Trigger it once
my_contract.execute_logic()
import requests

GATEWAY_URL = "http://127.0.0.1:8080"

print("--- 🌍 Checking Weather (London) ---")
try:
    resp = requests.get(f"{GATEWAY_URL}/proxy/weather", params={"query": "London"})
    print(resp.json())
except:
    print("Weather Failed")

print("\n--- 💰 Checking Bitcoin Price ---")
try:
    # We ask for "bitcoin"
    resp = requests.get(f"{GATEWAY_URL}/proxy/price", params={"ticker": "bitcoin"})
    print(resp.json())
except:
    print("Crypto Failed")
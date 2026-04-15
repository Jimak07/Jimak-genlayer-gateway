import os
from fastapi import FastAPI, Header, HTTPException
import httpx
import uvicorn

app = FastAPI()

# SECURITY: We hardcode the password here to guarantee it works
def verify_password(x_auth_token: str = Header(None)):
    correct_password = "genlayer_rules"  # <--- FIXED: Hardcoded password

    if x_auth_token != correct_password:
        raise HTTPException(status_code=403, detail="⛔ ACCESS DENIED: Wrong Password")

@app.get("/")
def home():
    return {"status": "🔒 Secure Gateway Online"}

# --- WEATHER SERVICE (LOCKED) ---
@app.get("/proxy/weather")
async def proxy_weather(query: str, x_auth_token: str = Header(None)):
    verify_password(x_auth_token) # Check password first

    api_key = os.environ.get("OPENWEATHER_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()

        # Simulation Mode for inactive keys
        if str(data.get("cod")) == "401":
            return {"condition": "Simulation Mode", "temp": 285.5}

        if "weather" in data:
            return {
                "type": "Weather",
                "condition": data["weather"][0]["description"],
                "temp": data["main"]["temp"]
            }
        return {"error": "City not found"}

# --- CRYPTO SERVICE (LOCKED) ---
@app.get("/proxy/price")
async def proxy_price(ticker: str, x_auth_token: str = Header(None)):
    verify_password(x_auth_token) # Check password first

    api_key = os.environ.get("COINGECKO_KEY")
    headers = {"x-cg-demo-api-key": api_key}
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ticker}&vs_currencies=usd"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
        data = resp.json()

        if ticker in data:
            return {
                "type": "Finance",
                "asset": ticker,
                "price_usd": data[ticker]["usd"]
            }
        return {"error": "Coin not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
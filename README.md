# Secure GenLayer Oracle Gateway 🔒

A secure, multi-source data proxy and intelligent contract architecture built for the GenLayer Blockchain.

## 📖 Overview
Smart contracts operating on public blockchains face the "Oracle Problem"—they cannot securely hold private API keys required to fetch premium real-world data without exposing those keys on the public ledger. This project solves that vulnerability by introducing a secure FastAPI proxy layer. It allows GenLayer Intelligent Contracts to autonomously access real-time financial and environmental data (CoinGecko & OpenWeatherMap) while keeping API keys safely off-chain in encrypted environment variables.

## ✨ Key Features
* **Multi-Source Data Aggregation:** Unifies weather conditions and cryptocurrency prices into a single, structured JSON endpoint.
* **Security First:** Protects private API keys by routing requests through a secure server, preventing on-chain key leakage.
* **Custom Authentication:** Implements `X-Auth-Token` header verification, ensuring only authorized contracts can access the gateway data.
* **GenVM Production Ready:** Includes a strict, statically-typed contract compliant with the upcoming GenVM Linter standards for Testnet Bradbury.

## 🏗️ Architecture & File Structure

* `main.py`: The secure FastAPI Gateway proxy. Runs off-chain, holds the API secrets, and serves data to the blockchain.
* `genlayer_sim.py`: A local Python simulation demonstrating how an Intelligent Contract authenticates with the gateway and executes logic based on real-world conditions (e.g., "If BTC > $90k, execute transaction").
* `genvm_contract.py`: The production-ready GenLayer contract. Written with strict `gl.u256` typing and deterministic logic to pass GenVM compiler requirements.

## 🚀 Tech Stack
* **Language:** Python 3
* **Framework:** FastAPI, Uvicorn
* **Blockchain:** GenLayer (GenVM), Intelligent Contracts
* **External APIs:** CoinGecko (Finance), OpenWeatherMap (Environment)
* **Deployment:** Replit

## 💡 Proof of Concept Logic
The included simulation demonstrates an autonomous decision-making loop:
1. The contract "wakes up" and securely pings the Gateway.
2. The Gateway authenticates the request and fetches live data.
3. The contract evaluates the data: `IF Bitcoin > $90,000 OR Weather == 'Rain'`.
4. If conditions are met, the contract autonomously executes a financial transaction.

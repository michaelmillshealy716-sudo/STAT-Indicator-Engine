# STAT-Indicator-Engine

A quantitative technical analysis module built for agentic consumption. This engine serves as the statistical pre-processor for the FASE (Financial Agentic System Engine) architecture under Healy Vector Labs. 

## Core Functionality
The STAT engine is designed to monitor market data, calculate technical indicators (e.g., Exponential Moving Averages), and detect critical shifts in market momentum. 

Rather than generating human-readable alerts, the engine serializes its findings into standardized JSON telemetry. This allows the FASE agentic core to asynchronously ingest, interpret, and execute upon the data.

## Current Modules
* **Trend Logic (`src/indicators/trend_logic.py`):** Utilizes NumPy for high-performance EMA calculations and crossover detection (Bullish/Bearish).
* **Signal Bridge (`src/indicators/bridge.py`):** Acts as the serialization layer, converting raw mathematical crossovers into ISO-8601 timestamped JSON payloads.

## Upcoming Roadmap
* **Gaussian Variance Screening:** Implementation of anomaly detection to filter out low-volume, high-volatility "fake-out" signals.
* **Spectral Analysis:** Integration of Fourier transforms for deeper market cycle identification.

## Usage
Data must be passed into the engine as arrays. The bridge automatically handles outbound serialization:
```json
{
  "engine": "STAT-V1",
  "indicator": "EMA_Crossover",
  "value": 155.0,
  "signal": "BULLISH",
  "timestamp": "2026-04-15T12:49:42.057038Z"
}


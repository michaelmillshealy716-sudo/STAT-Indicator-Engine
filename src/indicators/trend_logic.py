import numpy as np
from src.indicators.bridge import format_signal
from src.indicators.gaussian_filter import validate_variance

def calculate_ema(data, period=20):
    values = np.array(data)
    alpha = 2 / (period + 1)
    ema = np.zeros_like(values)
    ema[0] = values[0]
    for i in range(1, len(values)):
        ema[i] = alpha * values[i] + (1 - alpha) * ema[i-1]
    return ema.tolist()

def detect_crossover(fast_ema, slow_ema, raw_prices):
    """
    STAT: Crossover Detection with Gaussian Variance Filtering.
    """
    # Bullish Crossover Logic
    if fast_ema[-1] > slow_ema[-1] and fast_ema[-2] <= slow_ema[-2]:
        if validate_variance(raw_prices):
            print("\n--- STAT: BULLISH CROSSOVER VALIDATED ---")
            telemetry = format_signal("EMA_Crossover", fast_ema[-1], "BULLISH")
            print(f"[TELEMETRY LOG]: {telemetry}")
            return "BULLISH"
        
    # Bearish Crossover Logic
    elif fast_ema[-1] < slow_ema[-1] and fast_ema[-2] >= slow_ema[-2]:
        if validate_variance(raw_prices):
            print("\n--- STAT: BEARISH CROSSOVER VALIDATED ---")
            telemetry = format_signal("EMA_Crossover", fast_ema[-1], "BEARISH")
            print(f"[TELEMETRY LOG]: {telemetry}")
            return "BEARISH"
            
    return "NEUTRAL"


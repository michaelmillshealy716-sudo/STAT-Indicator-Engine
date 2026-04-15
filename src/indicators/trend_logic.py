import numpy as np
from bridge import format_signal

def calculate_ema(data, period=20):
    """
    STAT: Exponential Moving Average
    Provides the 'smooth shift' for the transitional gear.
    """
    values = np.array(data)
    alpha = 2 / (period + 1)
    ema = np.zeros_like(values)
    ema[0] = values[0]
    for i in range(1, len(values)):
        ema[i] = alpha * values[i] + (1 - alpha) * ema[i-1]
    return ema.tolist()

def detect_crossover(fast_ema, slow_ema):
    """
    STAT: Crossover Detection
    The ignition spark for a 24K trade entry.
    """
    if fast_ema[-1] > slow_ema[-1] and fast_ema[-2] <= slow_ema[-2]:
        print("\n--- STAT: BULLISH CROSSOVER DETECTED ---")
        telemetry = format_signal("EMA_Crossover", fast_ema[-1], "BULLISH")
        print(f"[TELEMETRY LOG]: {telemetry}")
        return "BULLISH"
        
    elif fast_ema[-1] < slow_ema[-1] and fast_ema[-2] >= slow_ema[-2]:
        print("\n--- STAT: BEARISH CROSSOVER DETECTED ---")
        telemetry = format_signal("EMA_Crossover", fast_ema[-1], "BEARISH")
        print(f"[TELEMETRY LOG]: {telemetry}")
        return "BEARISH"
        
    return "NEUTRAL"


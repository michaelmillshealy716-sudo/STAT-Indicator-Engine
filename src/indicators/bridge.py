import json
from datetime import datetime

def format_signal(indicator_type, value, trend):
    """
    Wires the STAT output to the FASE input schema.
    """
    payload = {
        "engine": "STAT-V1",
        "indicator": indicator_type,
        "value": value,
        "signal": trend, # e.g., 'bullish_crossover' or 'bearish_crossover'
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return json.dumps(payload)


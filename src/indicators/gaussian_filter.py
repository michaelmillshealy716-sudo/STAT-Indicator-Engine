import numpy as np

def validate_variance(prices, window=20, threshold=1.0):
    """
    STAT: Gaussian Variance Filter
    Filters out market noise by ensuring the price action has 
    enough statistical significance to justify a signal.
    """
    if len(prices) < window:
        # Not enough data to calculate variance, default to pass
        return True 
        
    recent_data = np.array(prices[-window:])
    mean = np.mean(recent_data)
    std_dev = np.std(recent_data)
    
    if std_dev == 0:
        print("[FILTER] Flatline detected. Pure noise.")
        return False 
        
    current_price = prices[-1]
    z_score = abs(current_price - mean) / std_dev
    
    # If the move is smaller than our threshold, it's just Gaussian noise
    if z_score < threshold:
        print(f"[FILTER] BLOCKED: Z-Score ({z_score:.2f}) below threshold. Market is choppy.")
        return False
        
    print(f"[FILTER] VALIDATED: High variance breakout (Z-Score: {z_score:.2f}).")
    return True


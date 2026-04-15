from trend_logic import detect_crossover

print("\n[SYSTEM] INITIATING STAT ENGINE WIRING TEST...\n")

# Scenario 1: Fast EMA crosses ABOVE Slow EMA
fast_bull = [149.0, 155.0]
slow_bull = [151.0, 150.0]
detect_crossover(fast_bull, slow_bull)

# Scenario 2: Fast EMA crosses BELOW Slow EMA
fast_bear = [155.0, 149.0]
slow_bear = [150.0, 151.0]
detect_crossover(fast_bear, slow_bear)

print("\n[SYSTEM] TEST COMPLETE.")


from trend_logic import detect_crossover

print("\n[SYSTEM] INITIATING GAUSSIAN-GATED WIRING TEST...\n")

# Scenario 1: High Variance (Validated Breakout)
# Added 20 baseline prices so the window is full
history = [100] * 20 
prices_high_v = history + [101, 102, 101, 155] 
fast_bull = [140, 155]
slow_bull = [150, 150]

print("TEST 1: HIGH VARIANCE SCENARIO (SHOULD VALIDATE)")
detect_crossover(fast_bull, slow_bull, prices_high_v)

# Scenario 2: Low Variance (Blocked Noise)
# Added 20 baseline prices. The tiny wiggle at the end shouldn't trigger.
history_noise = [150] * 20
prices_low_v = history_noise + [150.1, 150.2, 150.1, 150.05]
fast_bear = [151, 149]
slow_bear = [150, 151]

print("\nTEST 2: LOW VARIANCE SCENARIO (SHOULD BLOCK)")
detect_crossover(fast_bear, slow_bear, prices_low_v)

print("\n[SYSTEM] TEST COMPLETE.")


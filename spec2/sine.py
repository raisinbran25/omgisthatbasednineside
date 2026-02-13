import numpy as np
import matplotlib.pyplot as plt

# 1. Configuration
fs = 8000          # Sampling rate (Hz)
duration = 2.0      # Seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# 2. Generate a "Chirp" signal (starts at 440Hz, ends at 2000Hz)
f_start = 440
f_end = 2000
# The frequency increases linearly, so we integrate to get phase
signal = np.sin(2 * np.pi * (f_start + (f_end - f_start) * t / (2 * duration)) * t)

# Add some random noise for realism
signal += 0.2 * np.random.normal(size=len(t))
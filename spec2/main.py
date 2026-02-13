import plot, fft, sine
import numpy as np

samples = 512
out = np.zeros((len(sine.signal) // samples, samples))

for i in range(len(sine.signal) // samples):
    win = sine.signal[i * samples : (i + 1) * samples]
    out[i] = fft.recursive_fft(win)


plot.plotThis(out)
    


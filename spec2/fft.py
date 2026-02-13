import numpy as np

def recursive_fft(x):
    """
    A recursive implementation of the 1D Cooley-Tukey FFT.
    The input x must have a length that is a power of 2.
    """
    N = len(x)
    
    # --- BASE CASE ---
    # A 1-point DFT is just the sample itself.
    if N <= 1:
        return x
    
    # --- DIVIDE ---
    # Split the signal into even-indexed and odd-indexed samples.
    # Mathematically: x[2m] and x[2m+1]
    even = recursive_fft(x[0::2])
    odd  = recursive_fft(x[1::2])
    
    # --- CONQUER / COMBINE ---
    # Create an array to hold the result
    T = [0] * N
    
    # We only need to loop N/2 times because of the Butterfly symmetry
    for k in range(N // 2):
        # Calculate the Twiddle Factor: e^(-i * 2 * pi * k / N)
        # This is the "rotation" that aligns the odd samples with the even ones
        twiddle = np.exp(-2j * np.pi * k / N) * odd[k]
        
        # The Butterfly Operation:
        # X[k]       = E[k] + (Twiddle * O[k])
        # X[k + N/2] = E[k] - (Twiddle * O[k])
        T[k]          = even[k] + twiddle
        T[k + N // 2] = even[k] - twiddle
        
    return np.array(T)
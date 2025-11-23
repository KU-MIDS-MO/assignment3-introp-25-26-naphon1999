import numpy as np

def moving_average(signal, window_size):
    n = len(signal)
    k = window_size // 2
    arr = np.zeros(n)

    for i in range(n):
        start = max(0, i-k)
        end = min(n-1, i+k)

        sums = 0
        counts = 0
        
        for j in range(start, end+1):
            sums += signal[j]
            counts += 1

        arr[i] = sums / counts
    
    return arr

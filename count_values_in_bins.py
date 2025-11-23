import numpy as np

def count_values_in_bins(data, bin_edges):
    counts = np.zeros(len(bin_edges)-1)

    for i in range(len(bin_edges)-1):
        lower_edge = bin_edges[i]
        upper_edge = bin_edges[i+1]

        for j in data:
            if lower_edge <= j < upper_edge:
                counts[i] += 1
            else:
                if i == len(bin_edges)-2 and j == upper_edge:
                    counts[i] += 1

    return counts


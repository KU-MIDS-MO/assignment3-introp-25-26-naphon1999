import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    scores[scores < min_score] = min_score
    scores[scores > max_score] = max_score

    scaled_scores = (scores - min_score) / (max_score - min_score)
    scaled_scores = np.array(scaled_scores, dtype=float)

    return scaled_scores
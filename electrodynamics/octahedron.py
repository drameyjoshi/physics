import numpy as np
import pandas as pd
import math

from itertools import combinations
from typing import Dict, Set

positions = {_ for _ in 'ABCDEF'}
M = np.array(
    [[0, 1, np.sqrt(2), 1, 1, 1],
    [1, 0, 1, np.sqrt(2), 1, 1],
    [np.sqrt(2), 1, 0, 1, 1, 1],
    [1, np.sqrt(2), 1, 0, 1, 1],
    [1, 1, 1, 1, 0, np.sqrt(2)],
    [1, 1, 1, 1, np.sqrt(2), 0]])
labels = [_ for _ in positions]
distances = pd.DataFrame(data=M, index=labels, columns=labels)

def U(positives: Set[str], negatives: Set[str]) -> float:
    """
    Compute potential energy of the crystal assuming d = 1.
    The input parameters tell where the positive and negative ions
    are located.
    """
    x = 0
    for p in positives:
        for q in positives:
            if p != q:
                x += 1/distances[p][q]

    for n in negatives:
        for m in negatives:
            if n != m:
                x += 1/distances[n][m]
    x /= 2 # To account for double counting
    
    for p in positives:
        for n in negatives:
            if p != n:
                x -= 1/distances[p][n]
    # No double counting happened in the previous loops.

    return x

def config_name(positives: Set[str], negatives: Set[str]) -> str:
    """
    Create a name for each microstate from the position of the positive and
    negative ions.
    """
    return  ''.join([_ + '+' for _ in positives]) + \
            ''.join([_ + '-' for _ in negatives])


def get_all_microstates() -> Dict[str, float]:
    microstates = {}
    for c in combinations(positions, 3):
        positives = {_ for _ in c}
        negatives = positions - positives    
        name = config_name(positives, negatives)
        microstates[name] = U(positives, negatives)

    return microstates

def show_all_microstates(ms: Dict[str, float]) -> None:
    keys = list(ms.keys())
    keys.sort()

    for k in keys:
        print('U({0}) = {1}'.format(k, np.round(ms[k], 4)))


def main():
    ms = get_all_microstates()
    show_all_microstates(ms)


if __name__ == '__main__':
    main()
    
    

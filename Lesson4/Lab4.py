import numpy as np
import sys

file1_path = sys.argv[1]
file2_path = sys.argv[2]
probability = float(sys.argv[3])

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    real_data = np.array([int(x) for x in file1.read().split()])
    synthetic_data = np.array([int(x) for x in file2.read().split()])

mask = np.random.choice([True, False], size=len(real_data), p=[probability, 1 - probability])
result = np.where(mask, real_data, synthetic_data)

print(result)

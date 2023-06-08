import numpy as np
from sklearn.datasets import make_circles
import os


output_dir = 'data/prepared'
os.makedirs(output_dir, exist_ok=True)

# Generate a dataset and plot it
np.random.seed(0)
X, y = make_circles(n_samples=200, noise=0.05)
np.save('data/prepared/inputData.npy', X)   # X is an array
np.save('data/prepared/outputData.npy', y)   # X is an array
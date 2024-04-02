# Example Python script for generating random numbers from a normal distribution
import numpy as np

# Generate random numbers from a normal distribution
mu, sigma = 0, 0.1  # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
print(s)

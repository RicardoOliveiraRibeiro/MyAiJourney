# Example Python script for gradient descent optimization
import numpy as np

# Define the loss function and its gradient
def loss_function(x):
    return x**2

def gradient(x):
    return 2*x

# Gradient descent optimization
learning_rate = 0.1
x = 10  # Initial guess
for i in range(100):
    x -= learning_rate * gradient(x)
print("Optimal value of x:", x)

# Function to compute Mean Square Error (MSE)
import numpy as np

def compute_mse(A_estimates, B_estimates, A_true, B_true):
    mse_A = np.mean((A_estimates - A_true) ** 2)
    mse_B = np.mean((B_estimates - B_true) ** 2)
    return mse_A, mse_B
# Compute Fisher Information Matrix for the line fitting algorithm
import numpy as np

def fisher_information_matrix(N, var):
    I_11 = N / var  # ∂²ln(p)/∂A²
    I_12_21 = (N * (N - 1)) / (2 * var)  # ∂²ln(p)/∂A∂B
    I_22 = (N * (N - 1) * (2 * N - 1)) / (6 * var)  # ∂²ln(p)/∂B²

    FIM = np.array([[I_11, I_12_21],
                    [I_12_21, I_22]])
    return FIM
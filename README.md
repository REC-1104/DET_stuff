# Line Fitting with Maximum Likelihood Estimation (MLE) and Cramér-Rao Lower Bound (CRLB)

This project demonstrates the application of Maximum Likelihood Estimation (MLE) to estimate the slope and intercept of a linear model. Additionally, the Cramér-Rao Lower Bound (CRLB) is used to verify the efficiency of the estimators.

## Table of Contents
- [Introduction](#introduction)
- [Steps and Methodology](#steps-and-methodology)
- [Results](#results)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This notebook calculates the MLE of the parameters \( A \) (intercept) and \( B \) (slope) for a line-fitting problem. The CRLB is then computed to check if the estimators are efficient. The theoretical bounds on the variance of the estimators are derived using the Fisher Information Matrix (FIM).

### Key Objectives:
- Compute MLE for slope (\( B \)) and intercept (\( A \))
- Compute the Cramér-Rao Lower Bound (CRLB) for both parameters
- Compare the MLE estimates against the CRLB to evaluate their efficiency

## Steps and Methodology

### 1. MLE Computation
- **MLE for \( B \)** (slope) is computed using:
  \[
  B_{\text{MLE}} = \frac{\sum(x - \bar{x})(n - \bar{n})}{\sum(n - \bar{n})^2}
  \]
- **MLE for \( A \)** (intercept) is computed as:
  \[
  A_{\text{MLE}} = \bar{x} - B_{\text{MLE}} \times \bar{n}
  \]

### 2. CRLB Computation
- The Fisher Information Matrix (FIM) is calculated based on the data.
- The Cramér-Rao Lower Bound (CRLB) is the inverse of the FIM, providing the theoretical lower bound on the variance of the estimators.

### 3. Comparison
- The MLE results for \( A \) and \( B \) are compared to their true values.
- Errors and variances are computed and compared with the CRLB.

## Results

| Parameter | MLE Estimate | True Value | Percentage Error | CRLB Variance |
|-----------|--------------|------------|------------------|---------------|
| A (intercept) | 2.0019       | 2.0        | 0.1928%          | 0.019985      |
| B (slope)     | 1.50005      | 1.5        | 0.0052%          | \(1.5 * 10^{-8}\) |

- The MLE estimates for both \( A \) and \( B \) fall within the bounds established by the CRLB, confirming the efficiency of the estimators.

## Requirements

To run the notebook, you will need:
- Python 3.x
- NumPy
- Matplotlib
- Jupyter Notebook

## Usage

1. Clone the repository.
    ```bash
    git clone <repository_url>
    ```
2. Install the necessary Python packages.
    ```bash
    pip install -r requirements.txt
    ```
3. Open the Jupyter notebook and run the cells to reproduce the results.
    ```bash
    jupyter notebook line_fitting.ipynb
    ```

import numpy as np
from fit import fit

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.7, 7.4, 20.1, 55.2, 148.4])

# Definícia exponenciálnej funkcie
def exponential_function(x, A, B, C):
    return A * np.exp(B * x) + C

fit(x_data, y_data, exponential_function)

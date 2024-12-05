import numpy as np
import matplotlib.pyplot as plt
from fit import fit

capacity = [0,1,2,3,4,5,6,7,8,9,10]
U = [3.007, 5.603, 6.89, 7.53, 7.91, 8.18, 8.35, 8.48, 8.59, 8.67, 8.72]

x = np.linspace(np.min(capacity), np.max(capacity), 100)
def custom_function(x):
    return 0*x + 8.72

plt.plot(x, custom_function(x), color='orange', linestyle=':', label='asymptota')

plt.scatter(capacity, U, marker='o', s=10, label='namerané hodnoty', color="blue")
# plt.scatter(x,y, marker=':', s=10, label='', color="orange")
# plt.errorbar(U_ce, I_c, fmt='o', capsize=7, color="blue")

# x = np.linspace(np.min(x_data), np.max(x_data), 100)

# plt.plot(x, custom_function(x, *fitted_params), color='orange', linestyle=':', label='fit')
plt.ylabel(r'$U$ [V]')
# plt.ylabel('T [s]')
plt.xlabel(r'$C$ [μF]')
plt.legend()
plt.show()

def exponential_function(x, A, B, C, D):
    return -A * np.exp(-C-B * x) + D

fit(capacity, U, exponential_function)

U = [2.2, 2, 1.8, 1.7, 1.6, 1.5, 1.4]
I = [0.6, 0.41, 0.25, 0.17, 0.14, 0.1, 0.09]

plt.scatter(I, U, marker='o', s=10, label='namerané hodnoty', color="blue")
# plt.errorbar(U_ce, I_c, fmt='o', capsize=7, color="blue")

# x = np.linspace(np.min(x_data), np.max(x_data), 100)

# plt.plot(x, custom_function(x, *fitted_params), color='orange', linestyle=':', label='fit')
plt.ylabel(r'$U$ [V]')
# plt.ylabel('T [s]')
plt.xlabel(r'$I$ [mA]')
plt.legend()
plt.show()

# R =
# U = 
# I = []

# for i in range()
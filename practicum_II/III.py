import numpy as np
from fit import fit
from linear_fit import fit_n
import matplotlib.pyplot as plt

U_be = [0.81350, 0.79473, 0.78105, 0.75513, 0.73080, 0.71900, 0.69981, 0.68084, 0.59533, 0.56503, 0.43433, 0.42631, 0.38014, 0.31125, 130.018/1000, 8.624/1000]
print(len(U_be))
I_b = [52.177, 34.930, 25.172, 12.5737, 6.0724, 4.1750, 2.1751, 1057/1000, 5.968/1000, 1.625/1000, 0.015/1000, 0.012/1000, 0.004/1000, 0.002/1000, 0.001/1000, 0.002/1000]
print(len(I_b))
# U_be = np.array(U_be)
# U_be = U_be*1000

def exponential_function(x, A, B, C):
    return A * np.exp(B * x) + C

fit(U_be, I_b, exponential_function)

U_be = 0.673
I_b = 0.1
U_ce = [19.197, 18.247, 17.162, 15.954, 13.292, 8.9316, 6.6464, 2.8654, 0.503, 0.225, 0.19133, 0.16242, 0.13695, 0.12988, 0.11502, 93.783/1000, 76.605/1000, 52.260/1000, 12.223/1000]
print(len(U_ce))
I_c = [14.979, 14.956, 14.922, 14.888, 14.792, 14.618, 14.445, 14.340, 14.114, 13.9, 13.539, 12.689, 11.267, 10.665, 9.2403, 6.8143, 4.7806, 2.3321, 0.1769]
print(len(I_c))

plt.scatter(U_ce, I_c, marker='o', s=10, label='namerané hodnoty', color="blue")
plt.errorbar(U_ce, I_c, fmt='o', capsize=7, color="blue")

# x = np.linspace(np.min(x_data), np.max(x_data), 100)

# plt.plot(x, custom_function(x, *fitted_params), color='orange', linestyle=':', label='fit')
plt.xlabel(r'$U_{CE}$ [V]')
# plt.ylabel('T [s]')
plt.ylabel(r'$I_{C}$ [mA]')
plt.legend()
plt.show()

U_ce = [7.691/1000, 19.709/1000, 36.975/1000, 49.767/1000, 60.132/1000, 69.340/1000, 75.217/1000, 90.869/1000, 113.761/1000, 0.14188, 0.18899, 0.2047, 0.3, 0.39341, 0.47892, 0.73342]
I_c = [0.2993, 1.15144, 4.1041, 6.7112, 9.2435, 11.749, 13.430, 18.097, 24.555, 30.888, 36.666, 37.835, 40.556, 41.258, 41.486, 41.653]

plt.scatter(U_ce, I_c, marker='o', s=10, label='namerané hodnoty', color="blue")
plt.errorbar(U_ce, I_c, fmt='o', capsize=7, color="blue")

# x = np.linspace(np.min(x_data), np.max(x_data), 100)

# plt.plot(x, custom_function(x, *fitted_params), color='orange', linestyle=':', label='fit')
plt.xlabel(r'$U_{CE}$ [V]')
# plt.ylabel('T [s]')
plt.ylabel(r'$I_{C}$ [mA]')
plt.legend()
plt.show()


I_c_1 = [14.486, 17.318, 19.941, 22.953, 25.710, 29.290, 30.357]
I_b_1 = [101, 121, 139.555, 160.478, 179.666, 204.55, 211.92]
I_c_2 = [8.260, 16.920, 19.427, 22.580, 25.448, 26.706, 33.018, 39.801]
I_b_2 = [57.077, 114.016, 131.819, 153.204, 172.848, 182.178, 224.91, 272.07]
I_b_1 = np.array(I_b_1)
I_b_1 = I_b_1/1000

I_b_2 = np.array(I_b_2)
I_b_2 = I_b_2/1000
# data = [I_c]
# x_list = [I_b]
# colors = ["orange"]
# labels = ["data","lineárny fit"]
# x_label = r'$I_{B}$ [mA]'
# y_label = r'$I_{C}$ [mA]'

# fit_n(data_list=[I_c_1, I_c_2], x_list=[I_b_1, I_b_2], colors=["orange", "blue"], labels=["",""], x_label=r'$I_{B}$ [\micro A]', y_label=r'$I_{C}$ [mA]')
fit_n(data_list=[I_c_1], x_list=[I_b_1], colors=["orange"], labels=["dáta"], x_label=r'$I_{B}$ [mA]', y_label=r'$I_{C}$ [mA]')
fit_n(data_list=[I_c_2], x_list=[I_b_2], colors=["orange"], labels=["dáta"], x_label=r'$I_{B}$ [mA]', y_label=r'$I_{C}$ [mA]')
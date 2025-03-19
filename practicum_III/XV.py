import numpy as np
import matplotlib.pyplot as plt
from table import table
from fit import fit as custom_fit
from average import statistics
from scipy.optimize import curve_fit
from math import exp

# V
U = [0.003, 1.086, 1.218, 1.231, 1.293, 1.335, 1.359, 1.393, 1.411, 1.432, 1.448, 1.460, 1.478, 1.497, 1.499, 1.506, 1.519, 1.527, 1.534, 1.543, 1.551, 1.561, 1.564, 1.571, 1.581, 1.58, 1.596, 1.606, 1.614, 1.626, 1.632, 1.639, 1.646, 1.648, 1.649, 1.650, 1.651, 1.652, 1.654, 1.656, 1.660, 1.666, 1.669, 1.672, 1.676, 1.681, 1.686]
# mA
I = [0, 0.001, 0.009, 0.012, 0.038, 0.073, 0.107, 0.184, 0.251, 0.371, 0.501, 0.630, 0.889, 1.168, 1.345, 1.535, 1.926, 2.205, 2.514, 2.895,3.283,  3.795, 3.956, 4.352, 5.007, 5.318, 6.012, 6.787, 7.458, 8.429, 8.977, 9.652, 10.444, 10.670, 10.834, 10.935, 11.021, 11.261, 11.776, 12.113, 13.085, 14.170, 14.774, 15.236, 16.107, 17.154, 18.208]
#\muA
I_phi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.06, 0.13, 0.20, 0.28, 0.38,0.60, 0.76, 0.8, 0.94, 1.18, 1.3, 1.6, 1.96, 2.33, 2.93, 3.37, 4.11, 6.25, 8.81, 12.75, 16.77, 20.53, 33.02, 63.24, 83.47, 141.77, 206.91, 243.05, 270.96, 323.43, 386.33, 448.3]

print(len(U))
print(len(I))
print(len(I_phi))

plt.plot(np.array(U), np.array(I), color="blue", marker='o',markersize=2 , label='', linestyle="")
plt.xlabel(r'$U\ [V]$')
plt.ylabel(r'$I\ [mA]$')
plt.legend()
plt.grid(False)
plt.show()


plt.plot(np.array(U), np.array(I_phi), color="orange", marker='o',markersize=2 , label='', linestyle="")
plt.xlabel(r'$U\ [V]$')
plt.ylabel(r'$I_{\phi}\ [mA]$')
plt.legend()
plt.grid(False)
plt.show()

def sigma_I_(I):
    sigma_I = []
    for i in range(len(I)):
        sigma_I.append(0.4/100*I[i])
    return sigma_I

def sigma_U_(U):
    sigma_U = []
    for i in range(len(U)):
        sigma_U.append(0.4/100*U[i])
    return sigma_U



def exp_fit(x,A,B):
    return A*2.71**(B*x)

custom_fit(U, I, exp_fit)

# V
U = [1.506, 1.519, 1.527, 1.534, 1.543, 1.551, 1.561, 1.564, 1.571, 1.581, 1.58, 1.596, 1.606, 1.614, 1.626, 1.632, 1.639, 1.646, 1.648, 1.649, 1.650, 1.651, 1.652, 1.654, 1.656, 1.660, 1.666, 1.669, 1.672, 1.676, 1.681, 1.686]
# mA
I = [1.535, 1.926, 2.205, 2.514, 2.895,3.283,  3.795, 3.956, 4.352, 5.007, 5.318, 6.012, 6.787, 7.458, 8.429, 8.977, 9.652, 10.444, 10.670, 10.834, 10.935, 11.021, 11.261, 11.776, 12.113, 13.085, 14.170, 14.774, 15.236, 16.107, 17.154, 18.208]
#\muA
I_phi = [0.06, 0.13, 0.20, 0.28, 0.38,0.60, 0.76, 0.8, 0.94, 1.18, 1.3, 1.6, 1.96, 2.33, 2.93, 3.37, 4.11, 6.25, 8.81, 12.75, 16.77, 20.53, 33.02, 63.24, 83.47, 141.77, 206.91, 243.05, 270.96, 323.43, 386.33, 448.3]

sigma_I = sigma_I_(I)
sigma_I_phi = sigma_I_(I_phi)
sigma_U = sigma_U_(U)

for i in range(len(U)):
    if U[i] == 1.650:
        index = i

print(I[index])
print(sigma_I[index])

# print(len(U))
# print(len(I))
# print(len(I_phi))

# print(sigma_I)
# print(sigma_I_phi)
# print(sigma_U)

# table(values=[U, I, I_phi], errors=[sigma_U, sigma_I, sigma_I_phi])

def exp_fit(x,A,B):
    return A*2.71**(B*x)

custom_fit(U, I, exp_fit)

def fit_vals(I_f, U_f):

    I_f_fit = []
    U_vals_for_fit = []

    for i in range(len(I_f)):
        if i>=28 and i<=32:
            I_f_fit.append(I_f[i])
            U_vals_for_fit.append(U_f[i])

    return I_f_fit, U_vals_for_fit

def function(x,k,q):
    return k*x + q

I_fit, U_fit = fit_vals(I_phi, U)
custom_fit(I_fit, U_fit, function)
custom_fit(U_fit, I_fit, function)



stupnica = [17.612, 18.2056, 20.2795, 20.85955]
lambda_ = [407, 435, 546, 578]

(18.2111+ 18.2001)/2
(20.2771+ 20.2819)/2
(20.8540+ 20.8651)/2
(20.8962 + 20.9010)/2


custom_fit(stupnica, lambda_, function)

I_1 = 18.208
I_2 = 15.538
I_3 = 12.775
I_4 = 10.230


I = I_1

T = [16, 14, 13, 41]

def read_data(file_path):
    d_dilky = []
    d_nm = []
    signal = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Skip the first line (header)
        for line in lines[1:]:
            values = line.strip().split()
            if len(values) == 3:
                d_dilky.append(float(values[0]))
                d_nm.append(float(values[1]))
                signal.append(int(values[2]))

    return d_dilky, d_nm, signal

def max_dieliky(signal, wv):

    maxsignal = max(signal)

    for i in range(len(signal)):
        if signal[i] == maxsignal:
            maxwv = wv[i]
    
    print(maxwv)

    return maxwv, maxsignal

# Example usage
file_path = "./data_XV/jopek7.txt"  # Change this to your actual file path
d_dilky_7, d_nm_7, signal_7 = read_data(file_path)

file_path = "./data_XV/jopek8.txt"  # Change this to your actual file path
d_dilky_8, d_nm_8, signal_8 = read_data(file_path)

file_path = "./data_XV/jopek9.txt"  # Change this to your actual file path
d_dilky_9, d_nm_9, signal_9 = read_data(file_path)

file_path = "./data_XV/jopek10.txt"  # Change this to your actual file path
d_dilky_10, d_nm_10, signal_10 = read_data(file_path)

file_path = "./data_XV/jopek.txt"  # Change this to your actual file path
d_dilky_1, d_nm_1, signal_1 = read_data(file_path)

file_path = "./data_XV/jopek2.txt"  # Change this to your actual file path
d_dilky_2, d_nm_2, signal_2 = read_data(file_path)

file_path = "./data_XV/jopek3.txt"  # Change this to your actual file path
d_dilky_3, d_nm_3, signal_3 = read_data(file_path)

file_path = "./data_XV/jopek4.txt"  # Change this to your actual file path
d_dilky_4, d_nm_4, signal_4 = read_data(file_path)

file_path = "./data_XV/jopek5.txt"  # Change this to your actual file path
d_dilky_5, d_nm_5, signal_5 = read_data(file_path)

file_path = "./data_XV/jopek6.txt"  # Change this to your actual file path
d_dilky_6, d_nm_6, signal_6 = read_data(file_path)

wv_3, maxsignal_3 = max_dieliky(signal_3, d_nm_3)
wv_4, maxsignal_4 = max_dieliky(signal_4, d_nm_4)
wv_5, maxsignal_5 = max_dieliky(signal_5, d_nm_5)
wv_6, maxsignal_6 = max_dieliky(signal_6, d_nm_6)

statistics(data=[wv_3, wv_4, wv_5, wv_6])


plt.plot(np.array(d_nm_3), np.array(signal_3), color="red", marker='o',markersize=1 , label='24', linestyle="")
plt.plot(np.array(d_nm_7), np.array(signal_7), color="green", marker='o',markersize=1 , label='16', linestyle="")
plt.plot(np.array(d_nm_8), np.array(signal_8), color="orange", marker='o',markersize=1 , label='14', linestyle="")
plt.plot(np.array(d_nm_9), np.array(signal_9), color="blue", marker='o',markersize=1 , label='13', linestyle="")
plt.plot(np.array(d_nm_10), np.array(signal_10), color="black", marker='o',markersize=1 , label='41', linestyle="")
plt.xlabel(r'$\lambda\ [nm]$')
plt.ylabel(r'$signal$')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(d_nm_1), np.array(signal_1), color="green", marker='o',markersize=2 , label='', linestyle="")

plt.xlabel(r'$y$')
plt.ylabel(r'$signal$')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(d_nm_3), np.array(signal_3), color="red", marker='o',markersize=1 , label="18.208 mA", linestyle="-")
plt.plot(np.array(d_nm_4), np.array(signal_4), color="blue", marker='o',markersize=1 , label="15.538 mA", linestyle="-")
plt.plot(np.array(d_nm_5), np.array(signal_5), color="purple", marker='o',markersize=1 , label="12.775 mA", linestyle="-")
plt.plot(np.array(d_nm_6), np.array(signal_6), color="black", marker='o',markersize=2 , label="10.230 mA", linestyle="-")
plt.xlabel(r'$\lambda\ [nm]$')
plt.ylabel(r'$signal$')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(d_nm_3), np.array(signal_3), color="red", marker='o',markersize=1 , label="18.208 mA", linestyle="-")
plt.xlabel(r'$\lambda\ [nm]$')
plt.ylabel(r'$signal$')
plt.legend()
plt.grid(False)
plt.show()
plt.plot(np.array(d_nm_4), np.array(signal_4), color="blue", marker='o',markersize=1 , label="15.538 mA", linestyle="-")
plt.xlabel(r'$\lambda\ [nm]$')
plt.ylabel(r'$signal$')
plt.legend()
plt.grid(False)
plt.show()
plt.plot(np.array(d_nm_5), np.array(signal_5), color="purple", marker='o',markersize=1 , label="12.775 mA", linestyle="-")
plt.xlabel(r'$\lambda\ [nm]$')
plt.ylabel(r'$signal$')
plt.legend()
plt.grid(False)
plt.show()
plt.plot(np.array(d_nm_6), np.array(signal_6), color="black", marker='o',markersize=2 , label="10.230 mA", linestyle="-")
plt.xlabel(r'$\lambda\ [nm]$')
plt.ylabel(r'$signal$')
plt.legend()
plt.grid(False)
plt.show()

wv_7, maxsignal_7 = max_dieliky(signal_7, d_nm_7)
wv_8, maxsignal_8 = max_dieliky(signal_8, d_nm_8)
wv_9, maxsignal_9 = max_dieliky(signal_9, d_nm_9)
wv_10, maxsignal_10 = max_dieliky(signal_10, d_nm_10)

T = [24, 16, 14, 13, 41]
wv = [wv_3,wv_7, wv_8, wv_9, wv_10]
maxsignal = [maxsignal_3, maxsignal_7, maxsignal_8, maxsignal_9, maxsignal_10]

plt.plot(np.array(T), np.array(wv), color="orange", marker='o',markersize=5 , label='', linestyle="")

plt.ylabel(r'$\lambda\ [nm]$')
plt.xlabel(r'$T\ [^\circ C]$')
plt.legend()
plt.grid(False)
plt.show()

custom_fit(T, wv, function)

plt.plot(np.array(T), np.array(maxsignal), color="orange", marker='o',markersize=5 , label='', linestyle="")

plt.ylabel(r'$signal$')
plt.xlabel(r'$T\ [^\circ C]$')
plt.legend()
plt.grid(False)
plt.show()

custom_fit(T, wv, function)

# V
U = [0.003, 1.086, 1.218, 1.231, 1.293, 1.335, 1.359, 1.393, 1.411, 1.432, 1.448, 1.460, 1.478, 1.497, 1.499, 1.506, 1.519, 1.527, 1.534, 1.543, 1.551, 1.561, 1.564, 1.571, 1.581, 1.58, 1.596, 1.606, 1.614, 1.626, 1.632, 1.639, 1.646, 1.648, 1.649, 1.650, 1.651, 1.652, 1.654, 1.656, 1.660, 1.666, 1.669, 1.672, 1.676, 1.681, 1.686]
# mA
I = [0, 0.001, 0.009, 0.012, 0.038, 0.073, 0.107, 0.184, 0.251, 0.371, 0.501, 0.630, 0.889, 1.168, 1.345, 1.535, 1.926, 2.205, 2.514, 2.895,3.283,  3.795, 3.956, 4.352, 5.007, 5.318, 6.012, 6.787, 7.458, 8.429, 8.977, 9.652, 10.444, 10.670, 10.834, 10.935, 11.021, 11.261, 11.776, 12.113, 13.085, 14.170, 14.774, 15.236, 16.107, 17.154, 18.208]
#\muA
I_phi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.06, 0.13, 0.20, 0.28, 0.38,0.60, 0.76, 0.8, 0.94, 1.18, 1.3, 1.6, 1.96, 2.33, 2.93, 3.37, 4.11, 6.25, 8.81, 12.75, 16.77, 20.53, 33.02, 63.24, 83.47, 141.77, 206.91, 243.05, 270.96, 323.43, 386.33, 448.3]


for i in range(len(I)):

    if I[i] == 18.208:
        index = i
    
print(maxsignal_3/(U[index]*I[index]))
print(I_phi[i]/(U[index]*I[index]))



# plt.plot(np.array(d_nm_2), np.array(signal_2), color="orange", marker='o',markersize=1 , label='', linestyle="")
# plt.xlabel(r'$\lambda\ [nm]$')
# plt.ylabel(r'$signal$')
# plt.legend()
# plt.grid(False)
# plt.show()
# plt.plot(np.array(d_nm_3), np.array(signal_3), color="red", marker='o',markersize=1 , label='', linestyle="")
# plt.xlabel(r'$\lambda\ [nm]$')
# plt.ylabel(r'$signal$')
# plt.legend()
# plt.grid(False)
# plt.show()
# plt.plot(np.array(d_nm_4), np.array(signal_4), color="blue", marker='o',markersize=1 , label='', linestyle="")
# plt.xlabel(r'$\lambda\ [nm]$')
# plt.ylabel(r'$signal$')
# plt.legend()
# plt.grid(False)
# plt.show()
# plt.plot(np.array(d_nm_5), np.array(signal_5), color="purple", marker='o',markersize=1 , label='', linestyle="")
# plt.xlabel(r'$\lambda\ [nm]$')
# plt.ylabel(r'$signal$')
# plt.legend()
# plt.grid(False)
# plt.show()
# plt.plot(np.array(d_nm_6), np.array(signal_6), color="black", marker='o',markersize=2 , label='', linestyle="")
# plt.xlabel(r'$\lambda\ [nm]$')
# plt.ylabel(r'$signal$')
# plt.legend()
# plt.grid(False)
# plt.show()
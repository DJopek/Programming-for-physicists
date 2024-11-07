import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from poly_fit import polynomial_fit
from math import pi
from linear_fit import fit
from linear_fit import fit_2

R_value = 20
C = [1, 3, 5, 7, 9]
T = [0.01396, 0.03047, 0.03202, 0.03826, 0.04368]

# [C] = microF
# [R] = Ohm 

n = [4,5,4,4,4]

for i in range(len(n)):
    T[i] = T[i]/n[i]

print(T)


def custom_function(x, a, K):
    x = np.asarray(x)
    return 2*pi*np.sqrt(a*x) + K

polynomial_fit(C,T,custom_function)

def custom_function(x,a, K):
    return 2*np.sqrt(a/x) + K

R = [890, 550, 450, 390, 350]

polynomial_fit(C,R,custom_function)

tau = []


R = 1000

for i in range(len(C)):
    tau.append(R*C[i]*10**(-6))

print(tau)

b = [913.03, 307.75, 192.07, 141.17, 106.13]

tau_measurement = []

for i in range(len(b)):
    tau_measurement.append(1/b[i])

print(tau_measurement)

fit_2(tau, tau_measurement, C)
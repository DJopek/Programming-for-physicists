import numpy as np
from fit import fit
from average import statistics
import matplotlib.pyplot as plt
from table import table_justvalues
from table import table

l = 1212
sigma_l = 2
t = 5.04*10**(-6)
sigma_t = 0.1/100*t

print("t = " + str(t) + " \pm " + str(sigma_t))

v = l/t
sigma_v = (
    (sigma_l/t)**2
    + (l*sigma_t/t**2)**2
)**0.5

print(v)
print(sigma_v)

T = 15
I_15 = [2, 10, 15, 20, 25, 30, 32, 34, 36, 38, 40, 45, 50]
U_15 = [0, 0, 0, 0.040, 0.080, 0.120, 0.280, 0.480, 0.720, 0.960, 1.08, 1.6, 1.96]

plt.plot(I_15, U_15, color="blue", marker='o', markersize=3, label=r'T = 15$^{\circ}$', linestyle="")
plt.xlabel(r'I [mA]')
plt.ylabel(r'U [mV]')
plt.legend()
plt.grid(False)
plt.show()

T = 20
I_20 = [2, 10, 15, 20, 25, 30, 32, 34, 36, 38, 40, 45, 50]
U_20 = [0, 0, 0, 0, 0, 0.080, 0.240, 0.400, 0.640, 0.920, 1.04, 1.48, 2.04]

plt.plot(I_20, U_20, color="orange", marker='o', markersize=3, label=r'T = 20$^{\circ}$', linestyle="")
plt.xlabel(r'I [mA]')
plt.ylabel(r'U [mV]')
plt.legend()
plt.grid(False)
plt.show()

T = 25
I_25 = [10, 15, 20, 25, 30, 32, 34, 36, 37, 39, 42, 45, 50]
U_25 = [0, 0, 0, 0, 0.120, 0.160, 0.400, 0.640, 0.800, 0.960, 1.2, 1.44, 1.88]

plt.plot(I_25, U_25, color="red", marker='o', markersize=3, label=r'T = 25$^{\circ}$', linestyle="")
plt.xlabel(r'I [mA]')
plt.ylabel(r'U [mV]')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(I_15, U_15, color="blue", marker='o', markersize=3, label=r'T = 15$^{\circ}$', linestyle="")
plt.plot(I_20, U_20, color="orange", marker='o', markersize=3, label=r'T = 20$^{\circ}$', linestyle="")
plt.plot(I_25, U_25, color="red", marker='o', markersize=3, label=r'T = 25$^{\circ}$', linestyle="")
plt.xlabel(r'I [mA]')
plt.ylabel(r'U [mV]')
plt.legend()
plt.grid(False)
plt.show()

def sigmaU(U):
    sigma_U = []
    for i in range(len(U)):
        sigma_U.append(1/100 * U[i])

    return sigma_U

sigma_I = []
for i in range(len(I_15)):
    sigma_I.append(0.5)
sigma_U_15 = sigmaU(U_15)
sigma_U_20 = sigmaU(U_20)
sigma_U_25 = sigmaU(U_25)

# table_justvalues(values=[I_15, U_15, I_20, U_20, I_25, U_25])
table(values=[I_15, U_15, I_20, U_20, I_25, U_25], errors=[sigma_I, sigma_U_15, sigma_I, sigma_U_20, sigma_I, sigma_U_25])

I = 1 #mA
T = 23.7 #deg C

phi = [-20, -16, -12, -10, -8, -4, 0, 4, 8, 10, 16, 20] #deg
U = [0, 0.080, 0.080, 0.080, 0.160, 0.240, 0.440, 0.360, 0.240, 0.160, 0.080, 0.040 ] # mV

sigma_phi = []
for i in range(len(phi)):
    sigma_phi.append(float(1))

sigma_U = sigmaU(U)

plt.plot(phi, U, color="orange", marker='o', markersize=3, label="", linestyle="")
plt.xlabel(r'$\phi$ [deg]')
plt.ylabel(r'U [mV]')
plt.legend()
plt.grid(False)
plt.show()

def gaussian(x, A, mu, K):
    return A * np.exp(-K*((x - mu) ** 2))

fit(phi, U, gaussian)

print(sigma_U)
# table_justvalues(values=[phi, U])
table(values=[phi, U], errors=[sigma_phi, sigma_U])
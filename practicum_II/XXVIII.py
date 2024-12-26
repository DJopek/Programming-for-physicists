import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from fit import fit
from fit import fit_dx
from fit import fit_multi

I = [0.002/1000, 7.68, 12.47, 17.35, 22.33, 27.33, 37.08, 46.58, 55.19, 64.14, 71.44, 77.34, 83.48]
U = [0.014/1000, 0.472, 0.498, 0.505, 0.514, 0.521, 0.531, 0.539, 0.545, 0.551, 0.557, 0.559, 0.561]
Intensity = [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# plt.scatter(Intensity, I, marker='o', s=10, label='')
# plt.ylabel(r'$I$ [mA]')
# # plt.ylabel('T [s]')
# plt.xlabel(r'$I$ [sun]')
# plt.legend()
# plt.show()

# plt.scatter(Intensity, U, marker='o', s=10, label='')

# plt.ylabel(r'$U$ [V]')
# # plt.ylabel('T [s]')
# plt.xlabel(r'$I$ [sun]')
# plt.legend()
# plt.show()

I = [14.282/1000, 11.575/1000, 9.318/1000, 5.909/1000, 2.591/1000]
I = [14.282, 11.575, 9.318, 5.909, 2.591]
U = [105.5, 93.5, 80.8, 59.5, 30.6]
V = [15, 12.5, 10.5, 7.5, 4.5]

# plt.scatter(V, U, marker='o', s=10, label='')

# plt.ylabel(r'$U$ [mV]')
# # plt.ylabel('T [s]')
# plt.xlabel(r'$U$ [V]')
# plt.legend()
# plt.show()

# plt.scatter(V, I, marker='o', s=10, label='')

# plt.scatter(V, I, marker='o', s=10, label='')
# plt.ylabel(r'$I$ [μA]')
# # plt.ylabel('T [s]')
# plt.xlabel(r'$U$ [V]')
# plt.legend()
# plt.show()

def max_i(max_P, P, V, I):
    for i in range(len(P)):
        if P[i] == max_P:
            print(V[i])
            print(I[i])

def poly_fit_7(x, a, b, c, d, e, f, g, h):
    return a*x**7 + b*x**6 + c*x**5 + d*x**4 + e*x**3 + f*x**2 + g*x + h

def poly_fit_5(x, a, b, c, d, e, f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f

def derivation(x, a, b, c, d, e, f):
    return 5*a*x**4 + 4*b*x**3 + 3*c*x**2 + 2*d*x**1 + e + 0*f

def poly_fit_3(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

R = [0.1, 0.3, 0.6, 0.9, 1, 3, 6, 9, 10, 20, 25, 30, 35, 40, 50, 60, 70, 90, 100, 120, 130, 150, 12, 14, 16, 18, 22]
V = [3.591/1000, 10.737/1000, 14.923/1000, 21.810/1000, 24/1000, 68.648/1000, 135.10/1000, 0.2, 0.22, 0.387, 0.425, 0.446, 0.458, 0.467, 0.478, 0.485, 0.489, 0.495, 0.497, 0.50, 0.502, 0.512, 0.266, 0.303, 0.337, 0.367, 0.404]
I = [] 
sigma_I = []
sigma_U = []
sigma_R = []

P = []

sigma_P = []

for i in range(len(R)):
    I.append(V[i]/R[i])
for i in range(len(I)):
    P.append(V[i]*I[i])

for i in range(len(V)):
    sigma_U.append(0.01*V[i])
for i in range(len(R)):
    sigma_R.append(0.01*R[i])
for i in range(len(I)):
    sigma_I.append(
        (
            (-sigma_R[i]*V[i]/R[i]**2)**2 + (sigma_U[i]/R[i])**2
        )**0.5
    )
for i in range(len(V)):
    sigma_P.append(
        (
            (I[i]*sigma_U[i])**2 + (V[i]*sigma_I[i])**2
        )**0.5
    )

print("")
print("0.25")

# plt.scatter(V, I, marker='o', s=10, label='')
# plt.xlabel(r'$U$ [V]')
# plt.ylabel(r'$I$ [A]')
# # plt.legend()
# plt.show()

# fit(V,I,poly_fit_3)
# fit(V,I,poly_fit_5)
# fit(V,I,poly_fit_7)

# plt.scatter(V, P, marker='o', s=10, label='')
# # plt.ylabel('T [s]')
# plt.xlabel(r'$U$ [V]')
# plt.ylabel(r'$I$ [A]')
# plt.show()

# fit(V,P,poly_fit_5)
# fit_dx(V,P,poly_fit_5, derivation)
# fit_multi(V,P,V,I, poly_fit_7)


# U_max = 0.378 \pm 0.004
# P_max = 0.00757 \pm 0.00008
# => I_max = 0.01999 \pm 0.0002
# => R_max = 18.9 \pm 0.2

print("P: ")
print((np.array(P)*1000).tolist())
print("sigma_P")
print((np.array(sigma_P)*1000).tolist())
print("I: ")
print((np.array(I)*1000).tolist())
print("sigma_I")
print((np.array(sigma_I)*1000).tolist())
print("U")
print((np.array(V)*1000).tolist())
print("sigma_U")
print((np.array(sigma_U)*1000).tolist())
print("R")
print(R)
print("sigma_R")
print(sigma_R)
# print("max P")
# print(max(P))
# max_i(max(P), P, V, I)
# print(max(P)/0.25)
print("")

R = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 6, 7, 8, 12, 14, 16, 18, 22]
V = [50.67/1000, 0.24, 0.396, 0.476, 0.497, 0.507, 0.513, 0.516, 0.519, 0.521, 0.523, 0.526, 0.527, 0.281, 0.318, 0.351, 0.428, 0.447, 0.460, 0.470, 0.484]
I = [] 
sigma_I = []
sigma_U = []
sigma_R = []

P = []

sigma_P = []

for i in range(len(R)):
    I.append(V[i]/R[i])
for i in range(len(I)):
    P.append(V[i]*I[i])

for i in range(len(V)):
    sigma_U.append(0.01*V[i])
for i in range(len(R)):
    sigma_R.append(0.01*R[i])
for i in range(len(I)):
    sigma_I.append(
        (
            (-sigma_R[i]*V[i]/R[i]**2)**2 + (sigma_U[i]/R[i])**2
        )**0.5
    )
for i in range(len(V)):
    sigma_P.append(
        (
            (I[i]*sigma_U[i])**2 + (V[i]*sigma_I[i])**2
        )**0.5
    )

print("")
print("0.5")
print("")

# plt.scatter(V, I, marker='o', s=10, label='')
# plt.xlabel(r'$U$ [V]')
# plt.ylabel(r'$I$ [A]')
# plt.show()

# fit(V,I,poly_fit_3)
# fit(V,I,poly_fit_5)
# fit(V,I,poly_fit_7)


# plt.scatter(V, P, marker='o', s=10, label='')
# plt.xlabel(r'$U$ [V]')
# plt.ylabel(r'$P$ [W]')
# plt.show()

# fit(V,P,poly_fit_5)
# fit_dx(V,P,poly_fit_5, derivation)
# fit_multi(V,P,V,I, poly_fit_7)


# U_max = 0.387 \pm 0.004
# P_max = 0.0160 \pm 0.0002
# => I_max = 0.0412 \pm 0.0004
# => R_max = 9.39 \pm 0.09

print("P: ")
print(np.array(P)*1000)
print("sigma_P")
print(np.array(sigma_P)*1000)
print("I: ")
print(np.array(I)*1000)
print("sigma_I")
print(np.array(sigma_I)*1000)
print("U")
print(np.array(V)*1000)
print("sigma_U")
print(np.array(sigma_U)*1000)
print("R")
print(R)
print("sigma_R")
print(sigma_R)
# print("max P")
# print(max(P))
# max_i(max(P), P, V, I)
print("")


R = [0.1, 0.3, 0.6, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
V = [25.7/1000, 42.32/1000, 65.4/1000, 94.0/1000, 103.04/1000, 191.3/1000, 0.267, 0.325, 0.369, 0.399, 0.421, 0.437, 0.450, 0.460, 0.488, 0.503]
I = [] 
sigma_I = []
sigma_U = []
sigma_R = []

P = []

sigma_P = []

for i in range(len(R)):
    I.append(V[i]/R[i])
for i in range(len(I)):
    P.append(V[i]*I[i])

for i in range(len(V)):
    sigma_U.append(0.01*V[i])
for i in range(len(R)):
    sigma_R.append(0.01*R[i])
for i in range(len(I)):
    sigma_I.append(
        (
            (-sigma_R[i]*V[i]/R[i]**2)**2 + (sigma_U[i]/R[i])**2
        )**0.5
    )
for i in range(len(V)):
    sigma_P.append(
        (
            (I[i]*sigma_U[i])**2 + (V[i]*sigma_I[i])**2
        )**0.5
    )

print("")
print("1")
print("")

# plt.scatter(V, I, marker='o', s=10, label='')
# plt.xlabel(r'$U$ [V]')
# plt.ylabel(r'$I$ [A]')
# plt.show()

# fit(V,I,poly_fit_3)
# fit(V,I,poly_fit_5)
# fit(V,I,poly_fit_7)


# plt.scatter(V, P, marker='o', s=10, label='')
# plt.xlabel(r'$U$ [V]')
# plt.ylabel(r'$P$ [W]')
# plt.show()

# fit(V,P,poly_fit_5)
# fit_dx(V,P,poly_fit_5, derivation)
# fit_multi(V,P,V,I, poly_fit_7)


# U_max = 0.358 \pm 0.004
# P_max = 0.0270 \pm 0.0003
# => I_max = 0.0411 \pm 0.004
# => R_max = 8.71 \pm 0.08

print("P: ")
print(np.array(P)*1000)
print("sigma_P")
print(np.array(sigma_P)*1000)
print("I: ")
print(np.array(I)*1000)
print("sigma_I")
print(np.array(sigma_I)*1000)
print("U")
print(np.array(V)*1000)
print("sigma_U")
print(np.array(sigma_U)*1000)
print("R")
print(R)
print("sigma_R")
print(sigma_R)
# print("max P")
# print(max(P))
# max_i(max(P), P, V, I)
print("")

# U_max = 0.378 \pm 0.004
# P_max = 0.00750 \pm 0.00008
# => I_max = 0.01999 \pm 0.0002
# => R_max = 18.9 \pm 0.2

# U_max = 0.387 \pm 0.004
# P_max = 0.0160 \pm 0.0001
# => I_max = 0.0412 \pm 0.0004
# => R_max = 9.39 \pm 0.09

# U_max = 0.358 \pm 0.004
# P_max = 0.0270 \pm 0.0005
# => I_max = 0.0411 \pm 0.004
# => R_max = 8.71 \pm 0.08

U_max = [0.378, 0.387, 0.358]
I_max = [0.01999, 0.0412, 0.0411]
sigma_U_max = [0.004, 0.004, 0.004]
P_max = [0.00757, 0.0160, 0.0270]
R_max = [18.9, 9.39, 8.71]
sigma_P_max = [0.00008, 0.0001, 0.0005]
sigma_I_max = []
sigma_R_max = []

for i in range(len(U_max)):
    sigma_I_max.append(
    (
        (-P_max[i]*sigma_U_max[i]/U_max[i]**2)**2 + (sigma_P_max[i]/U_max[i])**2
    )**0.5
    )

for i in range(len(U_max)):
    sigma_R_max.append((
        (-U_max[i]*sigma_I_max[i]/I_max[i]**2)**2 + (sigma_U_max[i]/I_max[i])**2
    )**0.5
    )

print("")
print("U_max")
print(U_max)
print("sigma_U")
print(sigma_U_max)
print("I_max")
print(I_max)
print("sigma_I: ")
print(sigma_I_max)
print("P_max")
print(P_max)
print("sigma_P_max")
print(sigma_P_max)
print("R_max")
print(R_max)
print("sigma_R: ")
print(sigma_R_max)


I = [22.33, 46.58, 83.48]
U = [0.514, 0.539, 0.561]
ff = []
sigma_I = [0.02, 0.05, 0.08]
sigma_U = [0.001, 0.001, 0.001]
sigma_FF = []
P_sun = [0.25, 0.5, 1]
eta = []
sigma_eta = []

for i in range(len(I)):
    ff.append(P_max[i]/(I[i]*U[i]))

for i in range(len(ff)):
    sigma_FF.append(
        (
            (sigma_P_max[i]/(I[i]*U[i]))**2 
            + (-sigma_I[i]*P_max[i]/(I[i]**2 *U[i]))**2
            + (-sigma_U[i]*P_max[i]/(U[i]**2 *I[i]))**2
        )**0.5
    )

print("")
print("FF")
print(ff)
print("sigma FF")
print(sigma_FF)

for i in range(len(P_max)):
    eta.append(P_max[i]/P_sun[i]*3)
    sigma_eta.append(sigma_P_max[i])

print("")
print("eta")
print(eta)
print("sigma eta")
print(sigma_eta)
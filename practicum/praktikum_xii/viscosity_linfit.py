import numpy as np
import matplotlib.pyplot as plt

# data=np.loadtxt("data.txt")
# print(data[:,1])
# data_y = data[:,1]

# for i in range (len(data_y)):
#     data_y[i] = np.log(data_y[i])

# model,V=np.polyfit(data[:,0],data_y,1,cov=True)
# y_fit=np.polyval(model,data[:,0])
# fig,ax=plt.subplots()

# ax.plot(data[:,0],y_fit,c="red")
# ax.set_xlabel("x", fontsize=15)
# ax.set_ylabel("y", fontsize=15)
# ax.set_yscale('log')

# plt.savefig("fit_log_e.png",dpi=600)

# print("y=ax+b")
# print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
# print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
# print("cov(a,b) = ",V[0,1])
# print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

# data = [332.083, 332.035, 329.051, 267.055, 226.045, 193.031, 165.049]
# v = []
# A = 0.003003

# for i in range (len(data)):
#     v.append(A * data[i])

# print(v)

data = [150.070, 152.072, 151.001, 153.030, 150.098, 150.064, 150.013, 149.073, 149.007, 149.087]

l = 146/1000
r = 1.29/2000
V = 0.00004
pi = 3.14
h = 5.67/100
rho = 997
g = 9.81
sigma_V = 0.0000005
sigma_h = 0.06/100
sigma_t = 0.6
sigma_rho = 1
sigma_r = 0.02/1000
sigma_l = 2/1000
sigma_g = 0
eta = 0.0009698859371840063
v = 0.20367303948141752
Re = 270.1209810757622
t = 150.3
d = V/(pi * r**2)
sigma_d = ((1/(pi * r**2) *sigma_V)**2 + (-2*V/(pi * r**3) *sigma_r)**2)**0.5

velocity = []
nu = []
Re = []

for i in range (len(data)):
    velocity.append(V/(data[i] * pi * r**2))

for i in range(len(data)):
    nu.append((pi * r**4 * h * rho * g * data[i])/(8 * V * l))

for i in range(len(velocity)):
    Re.append((2 * r * rho * velocity[i])/(nu[i]))

print(v)
print(nu)
print(Re)


import math

# Equation 1
def sigma_v_squared(sigma_V, sigma_t, sigma_r, t, V, r):
    term1 = (1 / (t * math.pi * r**2) * sigma_V)**2
    term2 = (-V / (t**2 * math.pi * r**2) * sigma_t)**2
    term3 = (-2 * V / (t * math.pi * r**3) * sigma_r)**2
    return term1 + term2 + term3

# Equation 2
def sigma_eta_squared(sigma_r, sigma_h, sigma_rho, sigma_g, sigma_t, sigma_V, sigma_l, h, rho, g, t, V, l, r):
    term1 = (4 * math.pi * h * rho * g * t * r**3 / (8 * V * l) * sigma_r)**2
    term2 = (math.pi * rho * g * t * r**4 / (8 * V * l) * sigma_h)**2
    term3 = (math.pi * h * g * t * r**4 / (8 * V * l) * sigma_rho)**2
    term4 = (math.pi * rho * h * t * r**4 / (8 * V * l) * sigma_g)**2
    term5 = (math.pi * rho * g * h * r**4 / (8 * V * l) * sigma_t)**2
    term6 = (-math.pi * rho * g * h * t * r**4 / (8 * V**2 * l) * sigma_V)**2
    term7 = (-math.pi * rho * g * h * t * r**4 / (8 * V * l**2) * sigma_l)**2
    return term1 + term2 + term3 + term4 + term5 + term6 + term7

# Equation 3
def sigma_Re(sigma_h, sigma_rho, sigma_v, sigma_eta, rho, v, r, eta):
    term1 = (2 * rho * v / eta * sigma_h)**2
    term2 = (2 * r * v / eta * sigma_rho)**2
    term3 = (2 * r * rho / eta * sigma_v)**2
    term4 = (-2 * r * rho * v / eta**2 * sigma_eta)**2
    return term1 + term2 + term3 + term4


sigma_v_avg = 0.001
sigma_eta_avg = 0.000003
sigma_Re_avg = 1
# Example usage
sigma_v_sq = sigma_v_squared(sigma_V, sigma_t, sigma_r, t, V, r)
# print("Sigma_v^2:", sigma_v_sq)

sigma_v = (sigma_v_sq + sigma_v_avg**2)**0.5
print("Sigma_v:", sigma_v)


sigma_eta_sq = sigma_eta_squared(sigma_r, sigma_h, sigma_rho, sigma_g, sigma_t, sigma_V, sigma_l, h, rho, g, t, V, l, r)
# print("Sigma_eta^2:", sigma_eta_sq)

sigma_eta = (sigma_eta_sq)**0.5
print("Sigma_eta:", sigma_eta)


sigma_Re_sq = sigma_Re(sigma_r, sigma_rho, sigma_v, sigma_eta, rho, v, r, eta)
# print("Sigma_Re^2:", sigma_Re_sq)

sigma_Re_val = (sigma_Re_sq + sigma_Re_avg**2)**0.5
print("Sigma_Re:", sigma_Re_val)

# data = [332.083, 332.035, 329.051, 267.055, 226.045, 193.031, 165.049]

# k = 0.003003
# v = []

# for i in range(len(data)):
#     v.append(k*data[i]/1000000)

# print(v)

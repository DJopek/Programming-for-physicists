from average import statistics
import numpy as np

# [wolfram, meď, kanthal, železo, mosadz, chromnikel]

l = [89.9, 90.0, 89.8, 89.7, 89.8, 89.9]

d_chromnikel = [1.0, 1.0, 0.99, 1.02, 1.0]
d_mosadz = [0.59, 0.59, 0.6, 0.6, 0.59]
d_Fe = [0.41, 0.41, 0.41, 0.41, 0.41]
d_kanthal = [0.52, 0.5, 0.5, 0.5, 0.5]
d_Cu = [1.35, 1.34, 1.35, 1.35, 1.34]
d_W = [0.69, 0.69, 0.69, 0.69, 0.69]

# statistics(d_chromnikel)
# statistics(d_mosadz)
# statistics(d_Fe)
# statistics(d_kanthal)
# statistics(d_Cu)
# statistics(d_W)
# statistics(l)

d = [0.69, 1.346, 0.504, 0.41, 0.594, 1.002]
sigma_d = [0, 0.00244948974278318, 0.0040000000000000036, 0, 0.00244948974278318, 0.00489897948556636]

l = 89.85000000000001
sigma_l = 0.0428174419288841

ab = [1/1000, 1/1000, 1, 1, 1/1000, 1]
R_W = [170, 37, 6.3, 1.5, 248, 1.2]

R_n = 0.1
R_p = [1000, 100, 1, 1, 100, 1]
R_T = [1400, 11, 63, 15, 222, 12]

X = []

for i in range(len(R_W)):
    X.append(R_W[i] * ab[i])

print("X: ")
print(X)

R_droty = 26/1000

X_2 = []

for i in range(len(X)):
    X_2.append(X[i] - R_droty)

print("X bez drotov: ")
print(X_2)

R_x = []

for i in range(len(R_T)):
    R_x.append(R_n/R_p[i] * R_T[i])

print("R_x: ")
print(R_x)


R = [0.138083, 0.011050, 6.270232, 1.480750, 0.221652, 1.179631]
sigma_R = 0.000069
rho = []
sigma_rho = []

rho_W = []
sigma_rho_W = []

rho_W_2 = []
sigma_rho_W_2 = []

rho_T = []
sigma_rho_T = []

def rho_values(R, sigma_R, rho, sigma_rho):
    for i in range(len(R)):
        rho.append(R[i]*3.14*d[i]**2/(4*l))
        sigma_rho.append(np.sqrt(((-R[i]*3.14*(d[i])**2)/(4*l**2) * sigma_l)**2 + ((3.14*(d[i])**2)/(4*l) * sigma_R)**2 + ((3.14*R[i]*d[i])/(2*l) * sigma_d[i])**2))

    print("rho: ")
    print(rho)
    print("sigma_rho")
    print(sigma_rho)

print("R: ")
rho_values(R, sigma_R, rho, sigma_rho)
print("W: ")
rho_values(X, R_droty, rho_W, sigma_rho_W)
print("W minus drociky: ")
rho_values(X_2, 0, rho_W_2, sigma_rho_W_2)
print("T: ")
rho_values(R_x, 0, rho_T, sigma_rho_T)
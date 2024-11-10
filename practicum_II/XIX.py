from average import statistics
from math import pi
import numpy as np
from linear_fit import fit_4
from linear_fit import fit_n

# sigma_T = 2*reakcny cas
sigma_T = 0.004
T_40 = [161.4, 161.2, 161.5]

# statistics(T_40)

T = 161.36666666666667
sigma_avg = 0.08819171036882363

T = T/40
sigma_avg = sigma_avg/40
sigma_T = sigma_T/40

print("T: " + str(T))
# print(sigma_avg)
# print(sigma_T)

sigma_T = (sigma_T**2+sigma_avg**2)**0.5
print("sigma_T: " + str(sigma_T))

J = 2.72*10**(-4)
sigma_J = 0

D = (4*pi**2*J)/(T**2)
sigma_D = np.sqrt(
    ((4*pi**2*sigma_J)/(T**2))**2 + (-2*(4*pi**2*J*sigma_T)/(T**3))**2
)

print("D: " + str(D*10**4))
print("sigma_D: " + str(sigma_D*10**4))

r = [25/200, 25/200, 39/200, 39/200]
l = 125
N = [10,5,10, 5]
sigma_r = 2*0.001/2
sigma_l = 0.001/2

# N=10, r=12.5
I_1 = [4.05, 3.51, 3.01, 2.5, 2.02, 1.5, 1, 0.59, 0]
d_1 = [13.1, 9.9, 7.1, 4.2, 1.3, -1.6, -4.5, -6.8, -10.2]
d_0_1 = -10.2
x_1 = []

# N=5, r=12.5
I_2 = [4.0, 3.5, 3.01, 2.51, 2, 1.5, 1, 0.5, 0]
d_2 = [1.4, -0.2, -1.6, -3, -4.5, -6, -7.4, -8.8, -10.4]
d_0_2 = -10.4
x_2 = []

# N=10, r=19.5
I_3 = [4.0, 3.51, 3.0, 2.51, 2, 1.5, 1, 0.5, 0]
d_3 = [1.6, 0.2, -1.2, -1.7, -4.2, -5.7, -7, -8.5, -10]
d_0_3 = -10
x_3 = []

# N=5, r=19.5
I_4 = [4.0, 3.5, 3.01, 2.5, 2, 1.5, 1, 0.5, 0]
d_4 = [-4.3, -4.9, -5.7, -6.5, -7, -7.8, -8.5, -9.3, -9.9]
d_0_4 = -9.9
x_4 = []

print("")
print("")

def x_vals(d_0, d, x):
    for i in range(len(d)):
        x.append(abs(d_0 - d[i]))

    print(x)

x_vals(d_0_1, d_1, x_1)
x_vals(d_0_2, d_2, x_2)
x_vals(d_0_3, d_3, x_3)
x_vals(d_0_4, d_4, x_4)

a_1 = []
a_2 = []
a_3 = []
a_4 = []

def a_vals(x, a):
    for i in range(len(x)):
        a.append(x[i]/(2*l))

a_vals(x_1, a_1)
a_vals(x_2, a_2)
a_vals(x_3, a_3)
a_vals(x_4, a_4)

print("")
print("")

k, sigma_k = fit_4(a_1, a_2, a_3, a_4, I_1, I_2, I_3, I_4)

print("")
print("")

print("k: ")
print(np.array(k))
print("sigma_k: ")
print(np.array(sigma_k))

print("")
print("")

p = []
sigma_p = []

for i in range(len(r)):
    p.append(2*r[i]*k[i]*D/N[i])
    sigma_p.append(np.sqrt(
        (2*D*k[i]*sigma_r/N[i])**2 + (2*r[i]*k[i]*sigma_D/N[i])**2 + (2*r[i]*D*sigma_k[i]/N[i])**2
    ))

print("p: ")
print(np.array(p))
print("sigma p: ")
print(np.array(sigma_p))

print("")
print("")

statistics(p)

print("")
print("")

print("p Amper: ")
print(np.array(p)/(4*pi*10**(-7)))

print("")
print("")

statistics(np.array(p)/(4*pi*10**(-7)))



# a, sigma_a, b, sigma_b = fit_n(data_list=[a_1, a_2], x_list=[I_1, I_2], colors=['orange', 'red'], labels=['N=10, r=12.5cm', 'N=5, r=12.5cm'], x_label="I[A]", y_label=r"$\alpha$[rad]")

# print(np.array(a))
# print(np.array(b))
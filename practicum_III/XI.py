from average import statistics
import numpy as np
import matplotlib.pyplot as plt
from fit import fit
from table import table

dieliky_destilka = [1+1/4+10/100, 1+2/4+10/100, 1+1/4+0/100]
print(dieliky_destilka)
dieliky_50 = [4+2/4+0.2, 4+3/4+11/100, 4+3/4+5/100]
dieliky_100 = [8, 8+0/3+8/100, 8+1/4+2/100]
dieliky_150 = [12+1/4+11/100, 12+2/4, 12+0/4+6/100]
dieliky_200 = [16 + 2/4, 16+3/4, 16+1/4+3/100]
dieliky_250 = [20, 20+2/4+17/100, 19+3/4+14/100]

print("")
print(dieliky_destilka)
statistics(dieliky_destilka)
print("")
print(dieliky_50)
statistics(dieliky_50)
print("")
print(dieliky_100)
statistics(dieliky_100)
print("")
print(dieliky_150)
statistics(dieliky_150)
print("")
print(dieliky_200)
statistics(dieliky_200)
print("")
print(dieliky_250)
statistics(dieliky_250)

destilka = 1.5110000000000001
error_destilka = 0.13121483655948868

c50 = 4.786666666666666
error_c50 = 0.04666666666666669

c100 = 8.144444444444444
error_c100 = 0.10696716930274441

c150 = 12.306666666666667
error_c150 = 0.12978614889287837

c200 = 16.51
error_c200 = 0.13576941236277504

c250 = 20.186666666666667
error_c250 = 0.24374394579375983

c = [0, 50, 100, 150, 200, 250]
phi = [destilka, c50, c100, c150, c200, c250]
error_phi = [error_destilka, error_c50, error_c100, error_c150, error_c200, error_c250]

def alfa_values(phi_1, phi_0):
    return phi_1-phi_0

phi_0 = destilka

alfa = []

for i in range(len(phi)):
    alfa.append(alfa_values(phi[i], phi_0))

error_alfa = []

for i in range(len(error_phi)):
    error_alfa.append(
        (error_phi[i]**2
        + error_destilka**2
        )**0.5
    )

d  = 1

print(alfa)
print(error_alfa)

# plt.plot(np.array(alfa), np.array(c), color="blue", marker='o',markersize=2 , label='', linestyle="")
plt.errorbar(c, alfa, yerr=error_alfa, fmt='o', color="blue", markersize=5, linestyle="", capsize=10, label="")
plt.xlabel(r'c [g/l]')
plt.ylabel(r'$\alpha\ [^\circ]$')
plt.legend()
plt.grid(False)
plt.show()

table(values=[phi], errors=[error_phi])
print("")
table(values=[alfa], errors=[error_alfa])


def linfit(x,A,B):
    return A*x+B


fit(c, alfa, linfit)

uhol_p = [12, 11+2/4+8/100, 10+2/4+9/100, 10+10/100,9+2/4, 8+2/4+7/100, 8+1/4]
uhol_m = [16+14/100, 15+2/4,14+3/4+12/100, 14+2/4, 13+3/4, 12+3/4+4/100, 12+1/4]
I_p = [0,0.505, 1.018, 1.513, 2.006, 2.508, 3.003]
I_m = [2.996, 2.483, 2.019, 1.547, 1.033, 0.484, 0]

uhol = [12, 11+2/4+8/100, 10+2/4+9/100, 10+10/100,9+2/4, 8+2/4+7/100, 8+1/4, 16+14/100, 15+2/4,14+3/4+12/100, 14+2/4, 13+3/4, 12+3/4+4/100, 12+1/4]
I = [0,0.505, 1.018, 1.513, 2.006, 2.508, 3.003, -2.996, -2.483, -2.019, -1.547, -1.033, -0.484, -0]

print("")
statistics(data=[uhol[0], uhol[len(uhol)-1]])

phi_0 = 12.125
error_phi_0 = 0.125

uhol = [12.125, 11+2/4+8/100, 10+2/4+9/100, 10+10/100,9+2/4, 8+2/4+7/100, 8+1/4, 16+14/100, 15+2/4,14+3/4+12/100, 14+2/4, 13+3/4, 12+3/4+4/100]
I = [0,0.505, 1.018, 1.513, 2.006, 2.508, 3.003, -2.996, -2.483, -2.019, -1.547, -1.033, -0.484]

print(uhol)

for i in range(len(I)):
    I[i] = -I[i]

error_I = []

for i in range(len(I)):
    error_I.append(0.01*I[i])

alfa = []

for i in range(len(uhol)):
    alfa.append(alfa_values(uhol[i], phi_0))

print(error_I)

B = []
sigma_B = []

for i in range(len(I)):
    B.append(0.0138*I[i])

for i in range(len(B)):
    sigma_B.append(0.0138*error_I[i])


fit(I, alfa, linfit)
fit(B, alfa, linfit)

print(I)
print(error_I)
print(B)
print(sigma_B)
print(alfa)
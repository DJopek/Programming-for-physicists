from average import statistics
from fit import fit
from table import table
import numpy as np
import matplotlib.pyplot as plt
from table import table_justvalues

V_glyc = [10, 8, 6, 5, 4] # ml
V_voda = [0, 2, 4, 5, 6] # ml
m_glyc = [] # g
m_voda = [] # g

rho_gly = 1.261
rho_v = 0.998

for i in range(len(V_glyc)):
    m_glyc.append(rho_gly*V_glyc[i])

for i in range(len(V_voda)):
    m_voda.append(rho_v*V_voda[i])

C_m = [] # g/l
C_V = [100, 80, 60, 50, 40] # %

V = 10 # ml
sigma_V = 0.1 # ml

for i in range(len(V_glyc)):
    C_m.append(rho_gly*V_glyc[i]*1000/V)

def err_m(rho):
    sigma_m = []
    for i in range(5):
        sigma_m.append(rho*sigma_V/V**2)
    return sigma_m

sigma_m_voda = err_m(rho_v)
sigma_m_glyc = err_m(rho_gly)

sigma_cV = []
for i in range(len(V_glyc)):
    sigma_cV.append(
        (
            (sigma_V/V)**2
            +(V_glyc[i]*sigma_V/V**2)**2
        )**0.5
    )

sigma_cm = []

for i in range(len(m_glyc)):
    sigma_cm.append(
        (
            (rho_gly*m_glyc[i]*sigma_V/V**2)**2
            +(rho_gly*sigma_m_glyc[i]/V)**2
        )**0.5
    )

sigma_V = [0.1, 0.1, 0.1, 0.1, 0.1]

table(values=[V_glyc, V_voda, m_glyc, m_voda, C_m, C_V], errors=[sigma_V, sigma_V, sigma_m_glyc, sigma_m_voda, sigma_cm, sigma_cV])


n_D_100 = [1.469,1.470, 1.470]
Z_100 = [41,42, 42]

n_D_80 = [1.410, 1.410, 1.410]
Z_80 = [42, 40, 40]

n_D_60 = [1.460, 1.4605, 1.4595]
Z_60 = [38, 37, 38]

n_D_50 = [1.435, 1.434, 1.435]
Z_50 = [41, 42, 39]

n_D_40 = [1.441, 1.442, 1.443]
Z_40 = [38, 39, 40]

n_D_0 = [1.331, 1.331, 1.331]
Z_0 = [42, 41, 42]

statistics(n_D_100)
statistics(Z_100)

print("")
statistics(n_D_80)
statistics(Z_80)

print("")
statistics(n_D_60)
statistics(Z_60)

print("")
statistics(n_D_50)
statistics(Z_50)


print("")
statistics(n_D_40)
statistics(Z_40)

print("")
statistics(n_D_0)
statistics(Z_0)

C_V = [100, 80, 60, 50, 40, 0] # %


n_D = [1.470, 1.410, 1.4600, 1.4347, 1.442, 1.331]
n_D = [1.470,1.4600, 1.442, 1.4347, 1.410, 1.331]
error_n_D = [0.003, 0.001, 0.0003, 0.0003, 0.0006, 0.001]
Z = [41.7, 40.7, 37.7, 40.7, 39, 41.7]
error_Z = [0.3, 0.7, 0.3, 0.9, 0.6, 0.3]

table(values=[n_D, Z], errors=[error_n_D, error_Z])

def linfit(x,A,B):
    return A*x+B

fit(C_V, n_D, linfit)

Delta = []
A = [0.02433, 0.02435, 0.0244, 0.02443, 0.0245, 0.02484]
B = [0.02902, 0.02941, 0.03015, 0.0305, 0.03113, 0.03304]
sigma = [-0.588, -0.545, -0.407, -0.545, -0.454, -0.588]

for i in range(len(A)):
    Delta.append(A[i]+sigma[i]*B[i])

print("")
print("Delta")
print(Delta)
print("")

plt.plot(np.array(C_V), np.array(Delta), color="#66B2FF", marker='o',markersize=4 , linestyle="")
plt.xlabel(r'$c_V$ [%]')
plt.ylabel(r'$\Delta$')
plt.grid(False)
plt.show()

uhol_0 = np.linspace(0, 330, 12)

print(uhol_0)

uhol_1 = [34,34,34,34,34,34,34,34,34,34,34,34]
minutes = [24, 30, 37, 41, 50, 50, 35, 35, 35, 40, 42, 42]

for i in range(len(minutes)):
    uhol_1[i] = uhol_1[i] + minutes[i]/60

print(uhol_1)

table_justvalues(values=[uhol_0, uhol_1])

print("uhol 1")
statistics(uhol_1)

uhol = [0, 180]
sklo = [59.7, 60]
opticke_sklo = [59+25/60, 59+28/60]
pyrex = [57+6/10, 57+10/60]

table_justvalues(values=[uhol, sklo, opticke_sklo, pyrex])

print("sklo")
statistics(sklo)
print("opticke sklo")
statistics(opticke_sklo)
print("pyrex")
statistics(pyrex)
print("")

# riadny_uhol = [61, 61, 61, 61, 62, 62, 61, 61, 61, 61, 61, 61]
# riadny_minuty = [51, 50, 50, 50, 0, 0, 55, 53, 54, 49, 50, 50]
# mimoriadny_uhol = [61, 62, 62, 62, 62, 61, 61, 62, 62, 62, 62, 61]
# mimoriadny_minuty = [51, 14, 30, 20, 0, 54, 57, 21, 34, 20, 0, 55]

riadny_uhol = [61, 61, 61, 61, 62, 62, 61, 61, 61, 61, 61, 61]
riadny_minuty = [51, 50, 50, 50, 0, 0, 55, 53, 54, 49, 50, 50]
mimoriadny_uhol = [61, 62, 62, 62, 62, 61, 61, 62, 62, 62, 62, 61]
mimoriadny_minuty = [51, 14, 30, 20, 0, 57, 57, 21, 20, 20, 0, 41]

for i in range(len(uhol_0)):
    riadny_uhol[i] = riadny_uhol[i] + riadny_minuty[i]/60

for i in range(len(uhol_0)):
    mimoriadny_uhol[i] = mimoriadny_uhol[i] + mimoriadny_minuty[i]/60

print(riadny_uhol)
statistics(riadny_uhol)
print(mimoriadny_uhol)
statistics(mimoriadny_uhol)


n_guľa = 1/np.sin(2*3.1415*34.640277777777776/360)
n_sklo = 1/np.sin(2*3.1415*59.85/360)
n_opticke_sklo = 1/np.sin(2*3.1415*59.44166666666666/360)
n_pyrex = 1/np.sin(2*3.1415*57.38333333333333/360)


n_riadny = []
n_mimoriadny = []

for i in range(len(riadny_uhol)):
    n_riadny.append(n_guľa*np.sin(2*3.1415*riadny_uhol[i]/360))

for i in range(len(mimoriadny_uhol)):
    n_mimoriadny.append(n_guľa*np.sin(2*3.1415*mimoriadny_uhol[i]/360))

print("riadny")
statistics(n_riadny)

riadny_stred = []

for i in range(len(uhol_0)):
    riadny_stred.append(1.551577797424357)

deviation = []

for i in range(len(n_riadny)):
    deviation.append(1.551577797424357-n_riadny[i])

print(deviation)

mimoriadny_korekcia = []

for i in range(len(n_mimoriadny)):
    mimoriadny_korekcia.append(n_mimoriadny[i]+deviation[i])

def sinus(x,A,B,C,D):
    return A*np.sin(2*3.1415*(B*x+C)/360)+D

fit(uhol_0, mimoriadny_korekcia, sinus)

plt.plot(np.array(uhol_0), np.array(n_riadny), color="orange", marker='o',markersize=4 , label='riadny paprsok', linestyle="")
plt.plot(np.array(uhol_0), np.array(riadny_stred), color="black", marker='',markersize=4 , label='stredná hodnota', linestyle="-")
plt.plot(np.array(uhol_0), np.array(n_mimoriadny), color="blue", marker='o',markersize=5 , label='mimoriadny paprsok', linestyle="")
plt.xlabel(r'$\varphi [^ \circ$]')
plt.ylabel(r'n')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(uhol_0), np.array(n_riadny), color="orange", marker='o',markersize=4 , label='riadny paprsok', linestyle="")
plt.plot(np.array(uhol_0), np.array(riadny_stred), color="black", marker='',markersize=4 , label='stredná hodnota', linestyle="-")
plt.plot(np.array(uhol_0), np.array(mimoriadny_korekcia), color="blue", marker='o',markersize=4 , label='mimoriadny paprsok', linestyle="")
plt.xlabel(r'$\varphi [^ \circ$]')
plt.ylabel(r'n')
plt.legend()
plt.grid(False)
plt.show()

table_justvalues(values=[uhol_0, riadny_uhol, mimoriadny_uhol, n_riadny, n_mimoriadny])
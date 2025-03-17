from math import exp, log
from fit import fit
from table import table
import csv
import numpy as np
import matplotlib.pyplot as plt
from linear_fit import fit as linfit
from table import round_values_errors


def csv_to_graph(file_path, color):
    U = []
    I_f = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            u = row[1].replace(',', '.')
            i_f = row[0].replace(',', '.')
            u = float(u)
            i_f = float(i_f)
            U.append(u)
            I_f.append(i_f)

    # plt.plot(U, I_f, color=color, marker='o', markersize=1, label="", linestyle="-")
    # plt.xlabel("U [V]")
    # plt.ylabel("I [A]")
    # plt.legend()
    # plt.grid(False)
    # plt.show()

    return U, I_f

def voltage(U, I_f, R):

    U_f = []

    for i in range(len(U)):
        U_f.append(U[i]-R*I_f[i])

    U_f = np.sort(np.array(U_f))

    return U_f.tolist()

U_1, I_f_1 = csv_to_graph(file_path="./data_V/Jopek_VA_1.csv", color="red") # svetelna charakteristika pre 5-513YD 
U_2, I_f_2 = csv_to_graph(file_path="./data_V/Jopek_VA_2.csv", color="green") # VA charakteristika pre 560LB7D
U_3, I_f_3 = csv_to_graph(file_path="./data_V/Jopek_VA_3.csv", color="blue") # svetelna charakteristika pre 560LB7D
U_4, I_f_4 = csv_to_graph(file_path="./data_V/Jopek_VA_4.csv", color="orange") # svetelna charakteristika pre 5-513YD
U_5_1, I_f_5_1 = csv_to_graph(file_path="./data_V/Jopek_T_1_1.csv", color="black")
U_5_2, I_f_5_2 = csv_to_graph(file_path="./data_V/Jopek_T_1_2.csv", color="black")
U_6_1, I_f_6_1 = csv_to_graph(file_path="./data_V/Jopek_T_2_1.csv", color="black")
U_6_2, I_f_6_2 = csv_to_graph(file_path="./data_V/Jopek_T_2_2.csv", color="black")
U_7_1, I_f_7_1 = csv_to_graph(file_path="./data_V/Jopek_T_3_1.csv", color="black")
U_7_2, I_f_7_2 = csv_to_graph(file_path="./data_V/Jopek_T_3_2.csv", color="black")




R_1 = 390
R_2 = 330

sigma_R_1 = 0.01*R_1
sigma_R_2 = 0.01*R_2

U_f_1 = voltage(U_1, I_f_1, R_1)
U_f_2 = voltage(U_2, I_f_2, R_2)


plt.plot(np.array(U_f_1), np.array(I_f_1), color="orange", marker='o',markersize=1 , label='5-513YD', linestyle="-")
plt.plot(np.array(U_f_2), np.array(I_f_2), color="blue", marker='o',markersize=1 , label='560LB7D', linestyle="-")
plt.xlabel("U[V]")
plt.ylabel("I[A]")
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(I_f_2)*1000, np.array(I_f_3)*1000000, color="orange", marker='o',markersize=1 , label='5-513YD', linestyle="-")
# plt.xlabel("I[A]")
# plt.ylabel("If[A]")
# plt.legend()
# plt.grid(False)
# plt.show()

plt.plot(np.array(I_f_1)*1000, np.array(I_f_4)*1000000, color="blue", marker='o',markersize=1 , label='560LB7D', linestyle="-")
plt.xlabel("I[mA]")
plt.ylabel(r'$I_\Phi$' + str("[") + r'$\mu$' + str("A]"))
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(U_5_1), np.array(I_f_5_1), color="blue", marker='o',markersize=1 , label='0.2mA', linestyle="-")
plt.plot(np.array(U_5_2), np.array(I_f_5_2), color="blue", marker='o',markersize=1 , label='', linestyle="-")
plt.plot(np.array(U_6_1), np.array(I_f_6_1), color="black", marker='o',markersize=1 , label='0.4mA', linestyle="-")
plt.plot(np.array(U_6_2), np.array(I_f_6_2), color="black", marker='o',markersize=1 , label='', linestyle="-")
plt.plot(np.array(U_7_1), np.array(I_f_7_1), color="orange", marker='o',markersize=1 , label='0.6mA', linestyle="-")
plt.plot(np.array(U_7_2), np.array(I_f_7_2), color="orange", marker='o',markersize=1 , label='', linestyle="-")
plt.xlabel("U[V]")
plt.ylabel("I[A]")
plt.legend()
plt.grid(False)
plt.show()

def ln_vals(I_f, U_):

    I_f_ln = []
    U_vals_for_ln = []

    for i in range(len(I_f)):
        if I_f[i] >= 0:
            I_f_ln.append(log(I_f[i]))
            U_vals_for_ln.append(U_[i])

    return I_f_ln, U_vals_for_ln

I_f_1_ln, U_1_vals_for_ln = ln_vals(I_f_1, U_1)
I_f_2_ln, U_2_vals_for_ln = ln_vals(I_f_2, U_2)

plt.plot(np.array(U_1_vals_for_ln), np.array(I_f_1_ln), color="orange", marker='o',markersize=1 , label='5-513YD', linestyle="-")
plt.plot(np.array(U_2_vals_for_ln), np.array(I_f_2_ln), color="blue", marker='o',markersize=1 , label='560LB7D', linestyle="-")
plt.xlabel("U[V]")
plt.ylabel("ln(I)[ln(A)]")
plt.legend()
plt.grid(False)
plt.show()

def fit_ln_vals(I_f_ln, U_vals_for_ln):

    I_f_ln_fit = []
    U_vals_for_ln_fit = []

    for i in range(len(I_f_ln)):
        # if i>=6 and i<=11: #yellow
        if i>=7 and i<=10: #blue 
            I_f_ln_fit.append(I_f_ln[i])
            U_vals_for_ln_fit.append(U_vals_for_ln[i])

    return I_f_ln_fit, U_vals_for_ln_fit

I_f_1_ln_fit, U_1_vals_for_ln_fit = fit_ln_vals(I_f_1_ln, U_1_vals_for_ln)
I_f_2_ln_fit, U_2_vals_for_ln_fit = fit_ln_vals(I_f_2_ln, U_2_vals_for_ln)

linfit(I_f_1_ln_fit, U_1_vals_for_ln_fit)
linfit(I_f_2_ln_fit, U_2_vals_for_ln_fit)

def sigma_U_I(U, I_f):

    sigma_U = []
    sigma_I_f = []

    for i in range(len(U)):
        sigma_U.append(0.01/100*U[i])

    for i in range(len(I_f)):
        sigma_I_f.append(0.01/100*I_f[i])

    return sigma_U, sigma_I_f

sigma_U_1, sigma_I_f_1 = sigma_U_I(U_1, I_f_1)
sigma_U_2, sigma_I_f_2 = sigma_U_I(U_2, I_f_2)


def sigma_voltage(U, R, I_f, sigma_U, sigma_I_f, sigma_R):

    sigma_U_f = []

    for i in range(len(U)):
        sigma_U_f.append((
            (sigma_U[i])**2
            +(-I_f[i]*sigma_R)**2
            +(-R*sigma_I_f[i])**2
        )**0.5)

    return sigma_U_f

sigma_U_f_1 = sigma_voltage(U_1, R_1, I_f_1, sigma_U_1, sigma_I_f_1, sigma_R_1)
sigma_U_f_2 = sigma_voltage(U_2, R_2, I_f_2, sigma_U_2, sigma_I_f_2, sigma_R_2)

# print("")
# table(values=[U_1, I_f_1, U_f_1], errors=[sigma_U_1, sigma_I_f_1, sigma_U_f_1])
# print("")
# table(values=[U_2, I_f_2, U_f_2], errors=[sigma_U_2, sigma_I_f_2, sigma_U_f_2])
# print("")

k = 1.38*10**(-23)
e = 1.602*10**(-19)
K_1 = 20.144251364429213
sigma_K_1 = 0.21419867833469658
K_2 = 16.66299177506905
sigma_K_2 = 0.3615970660043379




def the_constant(e, k, K):
    return e/(k*K)

def sigma_constant(K, sigma_K):
    return e*sigma_K/(k*K**2)

nT_1 = the_constant(e, k, K_1)
nT_2 = the_constant(e, k, K_2)
sigma_nT_1 = sigma_constant(K_1, sigma_K_1)
sigma_nT_2 = sigma_constant(K_2, sigma_K_2)

print("")
print("nT1 = " + str(nT_1) + "\pm" + str(sigma_nT_1))
print("")
print("nT2 = " + str(nT_2) + "\pm" + str(sigma_nT_2))

def static_resistance(U_f_0, I_f_0):
    return U_f_0/I_f_0

def sigma_static_resistance(U_f_0, I_f_0, sigma_U_f_0, sigma_I_f_0):
    return (
        (sigma_U_f_0/I_f_0)**2
        + (U_f_0*sigma_I_f_0/I_f_0**2)**2
    )**0.5

for i in range(len(I_f_1)):
    if I_f_1[i] == 20/1000:
        index_1 = i

for j in range(len(I_f_2)):
    if I_f_2[j] == 0.0201:
        index_2 = j

sigma_R_d_1 = sigma_static_resistance(U_f_1[index_1], I_f_1[index_1], sigma_U_f_1[index_1], sigma_I_f_1[index_1])

print(U_f_1[index_1])
print(I_f_1[index_1])
print(sigma_U_f_1[index_1])
print(sigma_I_f_1[index_1])

sigma_R_d_2 = sigma_static_resistance(U_f_2[index_2], I_f_2[index_2], sigma_U_f_2[index_2], sigma_I_f_2[index_2])

print(U_f_2[index_2])
print(I_f_2[index_2])
print(sigma_U_f_2[index_2])
print(sigma_I_f_2[index_2])


R_d_1 = static_resistance(U_f_1[index_1], I_f_1[index_1])
print("")
print("R_d_1 = " + str(R_d_1) + "\pm" + str(sigma_R_d_1))
R_d_2 = static_resistance(U_f_2[index_2], I_f_2[index_2])
print("")
print("R_d_1 = " + str(R_d_2) + "\pm" + str(sigma_R_d_2))

def dynamic_resistance(R_d, nT, k, e, U_f_0):
    return R_d*(nT*k)/(e*U_f_0)

R_di_1 = dynamic_resistance(R_d_1, nT_1, k, e, U_f_1[index_1])
R_di_2 = dynamic_resistance(R_d_2, nT_2, k, e, U_f_2[index_2])

def sigma_dynamic_resistance(R_d, nT, k, e, U_f_0, sigma_R_d, sigma_U_f_0, sigma_nT):
    return (
        (nT*k*sigma_R_d/(e*U_f_0))**2
        + (nT*k*R_d*sigma_U_f_0/(e*U_f_0**2))**2
        + (k*R_d*sigma_nT/(e*U_f_0))**2
    )**0.5

sigma_R_di_1 = sigma_dynamic_resistance(R_d_1, nT_1, k, e, U_f_1[index_1], sigma_R_d_1, sigma_U_f_1[index_1], sigma_nT_1)
sigma_R_di_2 = sigma_dynamic_resistance(R_d_2, nT_2, k, e, U_f_2[index_2], sigma_R_d_2, sigma_U_f_2[index_2], sigma_nT_2)

print("")
print("R_di_1 = " + str(R_di_1) + "\pm" + str(sigma_R_di_1))
print("")
print("R_di_2 = " + str(R_di_2) + "\pm" + str(sigma_R_di_2))


def fit_ln_vals(I_f, U_f):

    I_f_fit = []
    U_vals_for_fit = []

    for i in range(len(I_f)):
        if i>=45 and i<=70: #yellow
        # if i>=45 and i<=60: #blue
            I_f_fit.append(I_f[i])
            U_vals_for_fit.append(U_f[i])

    return I_f_fit, U_vals_for_fit

I_f_1_fit, U_f_1_fit = fit_ln_vals(I_f_1, U_f_1)
linfit(I_f_1_fit, U_f_1_fit)

I_f_2_fit, U_f_2_fit = fit_ln_vals(I_f_2, U_f_2)
linfit(I_f_2_fit, U_f_2_fit)

print("U*_1")
print(0.13666875191673614/0.07468285290677643)
print("U*_2")
print(0.1027983838029585/0.03853612192620708)


I_f = [0.2, 0.4, 0.6]
I_phi = [58.5*10**(-9), 0.236*10**(-6), 0.486*10**(-6)]
I_co = [30.68*10**(-6), 144.3*10**(-6), 0.322*10**(-3)]


def sigma_I(I):
    sigma_I = []
    for i in range(len(I)):
        sigma_I.append(0.1/100*I[i])
    return sigma_I
sigma_I_F = sigma_I(I_f)
sigma_I_phi = sigma_I(I_phi)
sigma_I_co = sigma_I(I_co)

def G(I_co, I_phi, sigma_I_co, sigma_I_phi):
    G = []
    sigma_G = []

    for i in range(len(I_co)):
        G.append(I_co[i]/I_phi[i])
        sigma_G.append(
            (
                (sigma_I_co[i]/I_phi[i])**2
                +(sigma_I_phi[i]*I_co[i]/I_phi[i]**2)**2
            )**0.5
        )

    return G, sigma_G

G,sigma_G = G(I_co, I_phi, sigma_I_co, sigma_I_phi)

print("")
print(G)
print("")
print(sigma_G)
print("")

I_f = [0.2, 0.4, 0.6]
I_phi = [58.5, 0.236, 0.486]
I_co = [30.68, 144.3, 0.322]

sigma_I_F = sigma_I(I_f)
sigma_I_phi = sigma_I(I_phi)
sigma_I_co = sigma_I(I_co)

table(values=[I_f, I_phi, I_co, G], errors=[sigma_I_F, sigma_I_phi, sigma_I_co, sigma_G])
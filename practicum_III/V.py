from math import exp, log
from fit import fit
from table import table
import csv
import numpy as np
import matplotlib.pyplot as plt

# k = 
# T = 
# e = 

# U_f = []

# U_f_1 = 
# I_f_1 = 
# U_f_2 = 
# I_f_2 = 

# I_co = 
# I_phi = 

# U_f_0 = 
# I_f_0 = 

# sigma_U_f_0 = 
# sigma_I_f_0 = 

# def the_constant(e, k, T, U_f_1, I_f_1, U_f_2, I_f_2):
#     return e/(k*T) * (U_f_1 - U_f_2)/(log(I_f_1/I_f_2))

# n = the_constant(e, k, T, U_f_1, I_f_1, U_f_2, I_f_2)

# def static_resistance(U_f_0, I_f_0):
#     return U_f_0/I_f_0

# R_d = static_resistance()

# def sigma_static_resistance(U_f_0, I_f_0, sigma_U_f_0, sigma_I_f_0):
#     return (
#         (sigma_U_f_0**2/I_f_0)**2
#         + (U_f_0*sigma_I_f_0**2/I_f_0**2)**2
#     )**0.5

# sigma_R_d = sigma_static_resistance(U_f_0, I_f_0, sigma_U_f_0, sigma_I_f_0)

# def dynamic_resistance(R_d, n, k, T, e, U_f_0):
#     return R_d*(n*k*T)/(e*U_f_0)

# R_id = dynamic_resistance

# def sigma_dynamic_resistance(R_d, n, k, T, e, U_f_0, sigma_R_d, sigma_U_f_0, sigma_n):
#     return (
#         (n*k*T*sigma_R_d/(e*U_f_0))**2
#         + (n*k*T*R_d*sigma_U_f_0/(e*U_f_0**2))**2
#         + (k*T*R_d*sigma_n/(e*U_f_0))**2
#     )**0.5

# def P_N_current(I_0, e, U_f, n, k, T):
#     return I_0*exp(
#         (e*U_f[i])/(n*k*T)
#     )

# I_f = []

# for i in range(len(U_f)):
#     I_f.append(P_N_current(I_0, e, U_f[i], n, k, T))

# def photoelectric_current_in_collector(G, I_phi):
#     return G*I_phi

# fit(I_phi, I_co, photoelectric_current_in_collector)

# color='blue'
# label_x=r'$\lambda$ [nm]'
# label_y=r'$\frac{1}{\omega_r^2}\ [s^{2}]$'
# table(values=[r_rounded, E_1_rounded, E_2_rounded, J_1_rounded, J_2_rounded], errors=[sigma_r_rounded, sigma_E_1_rounded, sigma_E_2_rounded, sigma_J_1_rounded, sigma_J_2_rounded])

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

    # plt.plot(U, I_f, color=color, marker='o', markersize=1, label="", linestyle="")
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

U_1, I_f_1 = csv_to_graph(file_path="./data_V/Jopek_VA_1.csv", color="red")
U_2, I_f_2 = csv_to_graph(file_path="./data_V/Jopek_VA_2.csv", color="green")
U_3, I_f_3 = csv_to_graph(file_path="./data_V/Jopek_VA_3.csv", color="blue") # svetelna charakteristika pre 5-513YD
U_4, I_f_4 = csv_to_graph(file_path="./data_V/Jopek_VA_4.csv", color="orange") # svetelna charakteristika pre 560LB7D
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


plt.plot(np.array(U_f_1), np.array(I_f_1), color="blue", marker='o',markersize=1 , label='560LB7D', linestyle="None")
plt.plot(np.array(U_f_2), np.array(I_f_2), color="orange", marker='o',markersize=1 , label='5-513YD', linestyle="None")
plt.xlabel("U[V]")
plt.ylabel("I[A]")
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(I_f_2), np.array(I_f_3), color="orange", marker='o',markersize=1 , label='5-513YD', linestyle="None")
plt.plot(np.array(I_f_2), np.array(I_f_4), color="blue", marker='o',markersize=1 , label='560LB7D', linestyle="None")
plt.xlabel("I[A]")
plt.ylabel("If[A]")
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(U_5_1), np.array(I_f_5_1), color="blue", marker='o',markersize=1 , label='', linestyle="")
plt.plot(np.array(U_5_2), np.array(I_f_5_2), color="blue", marker='o',markersize=1 , label='', linestyle="")
plt.plot(np.array(U_6_1), np.array(I_f_6_1), color="black", marker='o',markersize=1 , label='', linestyle="")
plt.plot(np.array(U_6_2), np.array(I_f_6_2), color="black", marker='o',markersize=1 , label='', linestyle="")
plt.plot(np.array(U_7_1), np.array(I_f_7_1), color="red", marker='o',markersize=1 , label='', linestyle="")
plt.plot(np.array(U_7_2), np.array(I_f_7_2), color="red", marker='o',markersize=1 , label='', linestyle="")
plt.xlabel("")
plt.ylabel("")
plt.legend()
plt.grid(False)
plt.show()


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
T = 25-273.15
e = 1.602*10**(-19)




def the_constant(e, k, T, U_f_1, I_f_1, U_f_2, I_f_2):
    return e/(k*T) * (U_f_1 - U_f_2)/(log(I_f_1/I_f_2))

n = the_constant(e, k, T, U_f_1, I_f_1, U_f_2, I_f_2)

print("")
print("n = " + str(n))
print("")

print("")
print("K = " + str(e/(n*k*T)))
print("")

def static_resistance(U_f_0, I_f_0):
    return U_f_0/I_f_0

# R_d = static_resistance()

def sigma_static_resistance(U_f_0, I_f_0, sigma_U_f_0, sigma_I_f_0):
    return (
        (sigma_U_f_0**2/I_f_0)**2
        + (U_f_0*sigma_I_f_0**2/I_f_0**2)**2
    )**0.5

# sigma_R_d = sigma_static_resistance(U_f_0, I_f_0, sigma_U_f_0, sigma_I_f_0)

def dynamic_resistance(R_d, n, k, T, e, U_f_0):
    return R_d*(n*k*T)/(e*U_f_0)

# R_id = dynamic_resistance

def sigma_dynamic_resistance(R_d, n, k, T, e, U_f_0, sigma_R_d, sigma_U_f_0, sigma_n):
    return (
        (n*k*T*sigma_R_d/(e*U_f_0))**2
        + (n*k*T*R_d*sigma_U_f_0/(e*U_f_0**2))**2
        + (k*T*R_d*sigma_n/(e*U_f_0))**2
    )**0.5
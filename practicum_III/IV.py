import numpy as np
import matplotlib.pyplot as plt
import csv
from linear_fit import fit
from average import statistics
from table import round_values_errors
from table import table
from fit import fit as fit_any

csv_file = "./data_IV/data.csv"

wavelength = []
human_eye_sensitivity = []

with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)

    for row in reader:
        wavelength.append(int(row[0]))
        human_eye_sensitivity.append(float(row[1].replace(",", ".")))

plt.plot(np.array(wavelength), np.array(human_eye_sensitivity), color='blue', marker='o',markersize=1 , label='')
plt.xlabel(r'$\lambda$ [nm]')
# plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
plt.ylabel('Relatívna citlivosť [%]')
# plt.title('')
plt.legend()
plt.grid(False)
plt.show()



def csv_to_graph(file_path, color, label):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            # row = [value for value in row if value]
            row = [value for value in row if value and value != ";"]
            data.append(row)

    array = np.array(data, dtype=str)

    wavelength = array[:, 0].astype(float)
    data = array[:, 1].astype(float)

    # Convert scientific notation to normal float representation
    data = np.vectorize(lambda x: float(x))(data)

    plt.plot(np.array(wavelength), np.array(data), color=color, marker='o',markersize=1 , label=label)
    plt.xlabel(r'$\lambda$ [nm]')
    plt.ylabel("E [W.m" + r'$^{-2}$' + ".nm" + r'$^{-1}$' + "]")
    # plt.title('')
    plt.legend()
    plt.grid(False)
    plt.show()

csv_to_graph(file_path="./data_IV/Jopek_1_lx.csv", color="blue", label="zdroj 1 - LED")
csv_to_graph(file_path="./data_IV/Jopek_1_W.csv", color="blue", label="zdroj 1 - LED")
csv_to_graph(file_path="./data_IV/Jopek_2_lx.csv", color="orange", label="zdroj 2 - žiarovka")
csv_to_graph(file_path="./data_IV/Jopek_2_W.csv", color="orange", label="zdroj 2 - žiarovka")

def csv_to_E_e(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            # row = [value for value in row if value]
            row = [value for value in row if value and value != ";"]
            data.append(row)

    array = np.array(data, dtype=str)

    wavelength = array[:, 0].astype(float)
    data = array[:, 1].astype(float)

    # Convert scientific notation to normal float representation
    data = np.vectorize(lambda x: float(x))(data)

    phi_e = []

    for i in range(len(data)):
        phi_e.append(4*3.1415*0.2**2 * data[i])

    return phi_e


def csv_to_integral(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            # row = [value for value in row if value]
            row = [value for value in row if value and value != ";"]
            data.append(row)

    array = np.array(data, dtype=str)

    wavelength = array[:, 0].astype(float)
    data = array[:, 1].astype(float)

    # Convert scientific notation to normal float representation
    data = np.vectorize(lambda x: float(x))(data)

    print("")
    print(np.trapezoid(data, wavelength))
    print("")

csv_to_integral(file_path="./data_IV/Jopek_1_lx_2.csv")
csv_to_integral(file_path="./data_IV/Jopek_1_W_2.csv")
csv_to_integral(file_path="./data_IV/Jopek_2_lx_2.csv")
csv_to_integral(file_path="./data_IV/Jopek_2_W_2.csv")

def csv_to_K(file_path_1, file_path_2):
    data = []
    with open(file_path_1, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            # row = [value for value in row if value]
            row = [value for value in row if value and value != ";"]
            data.append(row)

    array = np.array(data, dtype=str)

    wavelength = array[:, 0].astype(float)
    data = array[:, 1].astype(float)

    # Convert scientific notation to normal float representation
    data = np.vectorize(lambda x: float(x))(data)

    data_1 = data

    data = []
    with open(file_path_2, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            # row = [value for value in row if value]
            row = [value for value in row if value and value != ";"]
            data.append(row)

    array = np.array(data, dtype=str)

    wavelength = array[:, 0].astype(float)
    data = array[:, 1].astype(float)

    # Convert scientific notation to normal float representation
    data = np.vectorize(lambda x: float(x))(data)

    data_2 = data

    K = []

    for i in range(len(data_1)):
        K.append(data_2[i]/data_1[i])

    return wavelength, K

    plt.plot(np.array(wavelength), np.array(K), color='blue', marker='o',markersize=1 , label='')
    plt.xlabel(r'$\lambda$ [nm]')
    plt.ylabel("K [lmW" + r'$^{-1}$' + "]")
    # plt.title('')
    plt.legend()
    plt.grid(False)
    plt.show()

wavelength, K_1 = csv_to_K(file_path_1="./data_IV/Jopek_1_W.csv", file_path_2="./data_IV/Jopek_1_lx.csv")
wavelength, K_2 = csv_to_K(file_path_1="./data_IV/Jopek_2_W.csv", file_path_2="./data_IV/Jopek_2_lx.csv")

plt.plot(np.array(wavelength), np.array(K_1), color='blue', marker='o',markersize=1 , label='zdroj 1 - LED')
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel("K [lmW" + r'$^{-1}$' + "]")
# plt.title('')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(wavelength), np.array(K_2), color='orange', marker='o',markersize=1 , label='zdroj 2 - žiarovka')
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel("K [lmW" + r'$^{-1}$' + "]")
# plt.title('')
plt.legend()
plt.grid(False)
plt.show()

plt.plot(np.array(wavelength), np.array(K_1), color='blue', marker='o',markersize=1 , label='zdroj 1 - LED')
plt.plot(np.array(wavelength), np.array(K_2), color='orange', marker='o',markersize=1 , label='zdroj 2 - žiarovka')
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel("K [lmW" + r'$^{-1}$' + "]")
# plt.title('')
plt.legend()
plt.grid(False)
plt.show()


wavelength, K_1 = csv_to_K(file_path_1="./data_IV/Jopek_1_W_2.csv", file_path_2="./data_IV/Jopek_1_lx_2.csv")
wavelength, K_2 = csv_to_K(file_path_1="./data_IV/Jopek_2_W_2.csv", file_path_2="./data_IV/Jopek_2_lx_2.csv")

phi_e_1 = csv_to_E_e(file_path="./data_IV/Jopek_1_W_2.csv")
# plt.plot(np.array(wavelength), np.array(phi_e_1), color='blue', marker='o',markersize=1 , label='zdroj 1 - LED')
# plt.grid(False)
# plt.show()

phi_e_2 = csv_to_E_e(file_path="./data_IV/Jopek_2_W_2.csv")
# plt.plot(np.array(wavelength), np.array(phi_e_2), color='blue', marker='o',markersize=1 , label='zdroj 1 - LED')
# plt.grid(False)
# plt.show()

K_phi_1 = []
K_phi_2 = []

for i in range(len(K_1)):
    K_phi_1.append(683* K_1[i] * phi_e_1[i])

# plt.plot(np.array(wavelength), np.array(K_phi_1), color='blue', marker='o',markersize=1 , label='zdroj 1 - LED')
# plt.grid(False)
# plt.show()

for i in range(len(K_2)):
    K_phi_2.append(683* K_2[i] * phi_e_2[i])

# plt.plot(np.array(wavelength), np.array(K_phi_2), color='blue', marker='o',markersize=1 , label='zdroj 1 - LED')
# plt.grid(False)
# plt.show()

print("")
print(np.trapezoid(K_phi_1, wavelength)) # I don't have any clue why it's showing nan
print(np.trapezoid(K_phi_2, wavelength)) # Also this doesn't look right
print("")




E_lx_1 = 397.326116049025
E_w_1 = 1.2551242377
E_lx_2 = 367.57657672774997
E_w_2 = 2.5062487174999997

phi_1 = 4*3.141529*0.2**2*E_lx_1
phi_2 = 4*3.141529*0.2**2*E_lx_2

print("")
print("phi_1 = " + str(phi_1))
print("")

print("")
print("phi_2 = " + str(phi_2))
print("")

eta_1 = 4*3.141529*0.2**2*E_lx_1/2
eta_2 = 4*3.141529*0.2**2*E_lx_2/25

print("")
print("eta_1 = " + str(eta_1))
print("")

print("")
print("eta_2 = " + str(eta_2))
print("")




r = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50] # m

over_r2 = []

for i in range(len(r)):
    over_r2.append(1/(r[i]**2))

E_1 = [472, 253, 158, 110, 80, 61, 49, 40] # lx
E_2 = [815, 435, 269, 184, 136, 105, 84, 70] # lx

#plotting and fitting the values
plt.plot(np.array(r), np.array(E_1), color='blue', marker="o", linestyle="-", label='zdroj 1 - LED')
plt.plot(np.array(r), np.array(E_2), color='orange', marker='o',linestyle="-", label='zdroj 2 - žiarovka')
plt.xlabel('r [m]')
# plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
plt.ylabel('E [lx]')
# plt.title('')
plt.legend()
plt.grid(False)
plt.show()

# print("")
# print("")
# fit(E_1, over_r2)
# print("")
# print("")
# fit(E_2, over_r2)
# print("")
# print("")

# caulculation and averaging computed values
J_1 = [] # cd
J_2 = [] # cd

for i in range(len(r)):
    J_1.append(E_1[i]*r[i]**2)
    J_2.append(E_2[i]*r[i]**2)

print("")
print("J_1:")
print(J_1)
statistics(J_1)
print("")
print("J_2:")
print(J_2)
statistics(J_2)


def calculate_error(measured_value, percentage_error):
    relative_error = (percentage_error / 100) * measured_value
    # total_error = relative_error + absolute_error
    return relative_error

percentage_error = 3
# absolute_error = 10

sigma_E_1 = []
sigma_E_2 = []

for i in range(len(E_1)):
    sigma_E_1.append(calculate_error(E_1[i], percentage_error))

for i in range(len(E_2)):
    sigma_E_2.append(calculate_error(E_2[i], percentage_error))

sigma_r = 1/2000
sigma_J_1 = []
sigma_J_2 = []

for i in range(len(r)):
    sigma_J_1.append(
        np.sqrt(
            (2*E_1[i]*sigma_r)**2
            + (r[i]**2*sigma_E_1[i])
            )
    )

for i in range(len(r)):
    sigma_J_2.append(
        np.sqrt(
            (2*E_2[i]*sigma_r)**2
            + (r[i]**2*sigma_E_2[i])
            )
    )
sigma_r = []

for i in range(len(r)):
    sigma_r.append(1/2000)

r_rounded, sigma_r_rounded = round_values_errors(r, sigma_r)
E_1_rounded,sigma_E_1_rounded = round_values_errors(E_1, sigma_E_1)
E_2_rounded,sigma_E_2_rounded = round_values_errors(E_2, sigma_E_2)
J_1_rounded,sigma_J_1_rounded = round_values_errors(J_1, sigma_J_1)
J_2_rounded,sigma_J_2_rounded = round_values_errors(J_2, sigma_J_2)

print("")
print("sigma_J_1:")
print(sigma_J_1_rounded)
statistics(sigma_J_1_rounded)
print("")
print("sigma_J_2:")
print(sigma_J_2_rounded)
statistics(sigma_J_2_rounded)

print("")
print("")
table(values=[r_rounded, E_1_rounded, E_2_rounded, J_1_rounded, J_2_rounded], errors=[sigma_r_rounded, sigma_E_1_rounded, sigma_E_2_rounded, sigma_J_1_rounded, sigma_J_2_rounded])
print("")
print("")

E_1 = [291, 405, 354, 305, 278, 298, 357, 416, 312, 356, 516, 509, 500, 490, 481, 490, 483, 364]
E_2 = [658, 530, 672, 541, 554, 552, 618, 576, 509, 490, 586, 650, 605, 601, 598, 640, 583, 462]
theta = np.linspace(0, 340, 18)
theta_rads = []

for i in range(len(theta)):
    theta_rads.append(2*3.1415*theta[i]/360)

plt.figure(figsize=(5, 5))
ax = plt.subplot(111, projection='polar')

ax.plot(theta_rads, E_1, marker='o', linestyle=':')

ax.set_theta_zero_location("E")
ax.set_theta_direction(1)
# ax.set_title()
ax.legend()

plt.show()

plt.figure(figsize=(5, 5))
ax = plt.subplot(111, projection='polar')

ax.plot(theta_rads, E_2, marker='o', linestyle=':')

ax.set_theta_zero_location("E")
ax.set_theta_direction(1)
# ax.set_title()
ax.legend()

plt.show()

# plt.axes(projection = 'polar') 
r = []
# deg = [0, 20, 40, 60, 80, 160+180, 140+180, 120+180, 100+180, 360]
deg = [0, 20, 40, 60, 80, 100+180, 120+180, 140+180, 160+180, 360]
rads = []
# E = [52.2, 46.9, 33.8, 18.0, 3.2, 47, 33.8, 18.2, 3.3, 52.2]
E = [52.2, 46.9, 33.8, 18.0, 3.2, 3.3, 18.2, 33.8, 47, 52.2]

for i in range(len(deg)):
    rads.append(2*3.1415*deg[i]/360)

# for i in range(len(E)):
#     r.append(E[i]/np.sin(rads[i]))

# plt.polar(rads, E, 'b.') 

# plt.show() 

plt.figure(figsize=(5, 5))
ax = plt.subplot(111, projection='polar')

ax.plot(rads, E, marker='o', linestyle=':')

ax.set_theta_zero_location("E")
ax.set_theta_direction(1)
# ax.set_title()
ax.legend()

plt.show()


J = []
B = []

d = 2.76/100

for i in range(len(E)):
    J.append(0.2**2*E[i])
    B.append(J[i]/(3.1415 * d**2/4 * np.cos(rads[i])))

def function(x, A):
    return A*np.cos(2*3.1415*x/360)

fit_any(x_data=[0, 20, 40, 60, 80, -80, -60, -40, -20, -0], y_data=J, custom_function=function)

plt.plot(np.array([0, 20, 40, 60, 80, -80, -60, -40, -20, -0]), np.array(B), color='blue', marker='o', linestyle="", markersize=5 , label='')
plt.xlabel('')
# plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
plt.ylabel('')
# plt.title('')
plt.legend()
plt.grid(False)
plt.show()

def calculate_error(measured_value, percentage_error, absolute_error):
    relative_error = (percentage_error / 100) * measured_value
    total_error = relative_error + absolute_error
    return total_error

percentage_error = 3
absolute_error = 10
sigma_E = []

for i in range(len(E)):
    sigma_E.append(calculate_error(E[i], percentage_error, absolute_error))

sigma_J = []
sigma_r = 0.005/200
sigma_S = 2*3.1415*d/2*sigma_r
sigma_theta = 0.5*2*3.1415/360

for i in range(len(E)):
    sigma_J.append(
        (
            ((d/2)**2 * sigma_E[i])**2
            + (2*(d/2)*E[i]*sigma_r)**2
        )**0.5
    )
sigma_B = []

for i in range(len(J)):
    sigma_B.append(
        (
            (1/(3.1415 * d**2/4 * np.cos(rads[i])) * sigma_J[i])**2
            + (-J[i]/((3.1415 * d**2/4)**2 * (np.cos(rads[i]))) *sigma_S)**2
            + (J[i]/(3.1415 * d**2/4 * (np.cos(rads[i]))**2 ) * np.sin(rads[i]) * sigma_theta)**2
        )**0.5
    )

print("")
print(str(B[0]) + "\pm" + str(sigma_B[0]))
r = 1.25/1000
rho = 998
eta = 0.0010518
l = 0.25
g = 9.81
pi = 3.14

# V_A = [62, 100, 180, 50, 48, 60, 68, 102, 62, 58, 80, 98]
# t_A = [24, 35, 54, 31, 33, 37, 42, 49, 31, 22, 30, 28]
# h_A = [15.7, 15.1, 21.4, 6.5, 6.8, 9.1, 9.4, 10.8, 11.2, 12, 13.4, 18]
# delta_h_A = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# h_A = [2.4, 2.9, 3.2, 4, 4.5, 5.2, 6.9, 7.1, 7.8, 8.3, 8.8, 10, 19.2, 20.3, 21.5, 22.5, 24, 25]
# h_critical = [19.2, 20.3, 21.5, 24, 25]
# V_A = [38, 50, 62, 78, 98, 64, 70, 80, 94, 64, 92, 86, 172, 228, 238, 242, 244, 238]
# t_A = [33, 30, 35, 31, 35, 21, 18, 21, 23, 17, 19,16, 23, 25, 26, 26, 26, 24]
# delta_h_A = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.3, 0.2, 0.2, 0.2]


h_A = [2.4, 2.6, 2.8, 3.2, 3.5, 3.7, 3.8, 4.1, 4.6, 5.1, 5.9, 5.5, 8, 9, 9.3, 7.7, 10.6, 17.2, 17.9, 18.5, 20.2, 21.7]
h_critical = [8, 9, 9.3, 7.7, 10.6]
V_A = [46, 46, 64, 80, 76, 80, 82, 82, 82, 100, 84, 70, 80, 82, 100, 96, 88, 100, 86, 84, 62, 86]
t_A = [21, 19, 29, 28, 26, 24, 23, 20, 23, 22, 16, 14, 13, 13, 17, 18, 14, 12, 11, 10, 9,10]
delta_h_A = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1, 1, 1, 1.5, 0.3, 0.2, 0.3, 0.2, 0.2, 0.1]

print(len(h_A))

print(len(V_A))

print(len(t_A))

print(len(delta_h_A))

for i in range(len(h_A)):
    h_A[i]=h_A[i]/100

for i in range(len(delta_h_A)):
    delta_h_A[i] = delta_h_A[i]/100

Q_A = []

for i in range(len(V_A)):
    Q = V_A[i] / t_A[i]
    Q_A.append(Q)

v_A = []

for i in range(len(Q_A)):
    v = V_A[i]/1000000 / (t_A[i] * (pi*r**2))
    v_A.append(v)

Re_A = []

for i in range(len(v_A)):
    Re = r * rho * v_A[i] / eta
    Re_A.append(Re)

Q_v_A = []
delta_p_A = []
sigma_delta_P_A = []

for i in range(len(h_A)):
    delta_P = h_A[i] * rho * g
    delta_p_A.append(delta_P)
    Q_v = pi * r**4 * delta_P / (8 * eta * l)
    Q_v_A.append(Q_v)
    sigma_delta_P = delta_h_A[i] * rho * g
    sigma_delta_P_A.append(sigma_delta_P)

k_A = []

for i in range(len(Re_A)):
    k = delta_p_A[i] * 2 * r / (l * rho * v_A[i])
    k_A.append(k)

k_A_16 = []

for i in range(len(Re_A)):
    k = 16/Re_A[i]
    k_A_16.append(k)

delta_p_A_2 = []

for i in range(len(v_A)):
    delta_P = k_A[i] * l/r * 0.5 * rho * v_A[i]
    delta_p_A_2.append(delta_P)

Q_v_A_2 = []

for i in range(len(v_A)):
    Q = pi * r**2 * v_A[i]
    Q_v_A_2.append(Q)

print("Q:")
print(Q_A)
print("v_A")
print(v_A)
print("Re:")
print(Re_A)
print("Q_v_A")
print(Q_v_A)
print("delta_P:")
print(delta_p_A)
print("sigma_delta_P")
print(sigma_delta_P_A)
print("k_A")
print(k_A)
print("k_A_16")
print(k_A_16)
print("delta_p_A_2")
print(delta_p_A_2)
print("Q_v_A_2")
print(Q_v_A_2)


delta_p = delta_p_A  # Example value for delta_p
sigma_r = 0.05/1000  # Example error for r
sigma_eta = 0  # Example error for eta
sigma_l = 0.005  # Example error for l
sigma_delta_p = sigma_delta_P_A
sigma_Q_v = []

# Formula for Q_v
# Q_v = (pi * r**4) / (8 * eta * l) * delta_p[i]

for i in range(len(sigma_delta_p)):
# Partial derivatives
    dQ_dr = (4 * pi * r**3) / (8 * eta * l) * delta_p[i]
    dQ_deta = -(pi * r**4) / (8 * eta**2 * l) * delta_p[i]
    dQ_dl = -(pi * r**4) / (8 * eta * l**2) * delta_p[i]
    dQ_ddelta_p = (pi * r**4) / (8 * eta * l)

    # Error propagation
    sigma_Q = ((dQ_dr * sigma_r)**2 + (dQ_deta * sigma_eta)**2 + (dQ_dl * sigma_l)**2 + (dQ_ddelta_p * sigma_delta_p[i])**2)**0.5
    sigma_Q_v.append(sigma_Q/1000000)

# Print the formulas and partial derivatives
# print("Formula for Q_v:", Q_v)
# print("\nPartial derivatives:")
# print("dQ/dr:", dQ_dr)
# print("dQ/deta:", dQ_deta)
# print("dQ/dl:", dQ_dl)
# print("dQ/ddelta_p:", dQ_ddelta_p)
# print("\nError of Q_v:", sigma_Q_v)
print("sigma_Q_v")
print(sigma_Q_v)

V = V_A
for i in range (len(V)):
    V[i] = V[i]/1000000

sigma_v_A = []
sigma_t = 0.4
sigma_V = 1/1000000
t = t_A

for i in range(len(V)):
    # Partial derivatives
    dv_dV = 1 / (t[i] * pi * r**2)
    dv_dt = -V[i] / (t[i]**2 * pi * r**2)
    dv_dr = -2 * V[i] / (t[i] * pi * r**3)

    # Error propagation
    sigma_v = ((dv_dV * sigma_V)**2 + (dv_dt * sigma_t)**2 + (dv_dr * sigma_r)**2)**0.5
    sigma_v_A.append(sigma_v)

print("sigma_v_A")
print(sigma_v_A)


sigma_rho = 0
sigma_v  = sigma_v_A
v = v_A
sigma_Re_A = []

for i in range(len(v)):
    dRe_dr = rho * v[i] / eta
    dRe_drho = r * v[i] / eta
    dRe_dv = r * rho / eta
    dRe_deta = -r * rho * v[i] / eta**2

    # Error propagation
    sigma_Re = ((dRe_dr * sigma_r)**2 + (dRe_drho * sigma_rho)**2 + (dRe_dv * sigma_v[i])**2 + (dRe_deta * sigma_eta)**2)**0.5
    sigma_Re_A.append(sigma_Re)

print("sigma_Re_A")
print(sigma_Re_A)

sigma_k_A = []

v = v_A
delta_p = delta_p_A
sigma_delta_p = sigma_delta_P_A
sigma_v = sigma_v_A

for i in range(len(sigma_Re_A)):
    # Partial derivatives
    dk_ddelta_p = 2 * r / (l * rho * v[i])
    dk_dr = delta_p[i] * 2 / (l * rho * v[i])
    dk_dl = -delta_p[i] * 2 * r / (l**2 * rho * v[i])
    dk_drho = -delta_p[i] * 2 * r / (l * rho**2 * v[i])
    dk_dv = -delta_p[i] * 2 * r / (l * rho * v[i]**2)

    # Error propagation
    sigma_k = ((dk_ddelta_p * sigma_delta_p[i])**2 + (dk_dr * sigma_r)**2 + (dk_dl * sigma_l)**2 +(dk_drho * sigma_rho)**2 + (dk_dv * sigma_v[i])**2)**0.5
    sigma_k_A.append(sigma_k)

print("sigma_k_A")
print(sigma_k_A)


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array(delta_p_A)
data = np.array(Q_A)
error_data_x = np.array(sigma_delta_P_A)
error_data_y = np.array(sigma_Q_v)

data_2 = []
for i in range(len(Q_v_A)):
    data_2.append(Q_v_A[i] * 1000000)

# Linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(x, data)

# Predicted values
predicted = slope * x + intercept

slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = stats.linregress(x, data_2)

predicted_2 = slope_2 * x + intercept_2


# Plot
plt.errorbar(x, data, yerr=error_data_y, xerr=error_data_x, fmt='o', elinewidth=2)
plt.plot(x, predicted, color='red', label='Závislosť Q od delta P')

plt.plot(x, predicted_2, color="green", linestyle='dashed', label="Teoretická závislosť")
# plt.plot(x, predicted_2)
plt.xlabel('delta P [Pa]')
plt.ylabel('Q [ml/s]')
plt.title('Závislosť Q od delta P')
plt.legend()
plt.grid(True)
plt.show()

print("Slope:", slope)
print("Intercept:", intercept)

model,V=np.polyfit(x,data,1,w=1.0/error_data_x,cov=True)
y_fit=np.polyval(model,x)
fig,ax=plt.subplots()
# ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
ax.plot(x,y_fit,c="red")
ax.set_xlabel("x", fontsize=15)
ax.set_ylabel("y", fontsize=15)
# plt.show()

print("y=ax+b")
print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
print("cov(a,b) = ",V[0,1])
print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))



import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 16 / x

# Generate x values
x_values = np.linspace(1, 2000, 100)  # Adjust the range as per your data

# Generate corresponding y values using the function
y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values, label='Function: 16/Re')

# Plot the points (assuming you have x_data and y_data)
x_data = Re_A  # Example x data
y_data = k_A  # Example y data
y_errors = sigma_k_A
x_errors = sigma_Re_A

plt.scatter(x_data, y_data, color='red', label='Points')

plt.errorbar(x_data, y_data, yerr=y_errors, xerr=x_errors , fmt='o', color='red', label='Points with Error Bars')


# Add labels and legend
plt.xlabel('Re')
plt.ylabel('k')
plt.title('16/Re a naše hodnoty')
plt.legend()

# Set y-axis limit
plt.ylim(0, 0.02)

# Show plot
plt.grid(True)
plt.show()

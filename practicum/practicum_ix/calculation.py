import numpy as np
import matplotlib.pyplot as plt

m = [1, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]
n_zatazovanie = [19, 17.6, 17.4, 17.1, 16.8, 16.5, 16.3, 16, 15.7, 15.4, 15.2, 14.9, 14.6, 14.4, 14.1, 13.8]
n_odoberanie = [19, 17.6, 17.3, 17.0, 16.8, 16.5, 16.2, 16.0, 15.7, 15.4, 15.1, 14.8, 14.6, 14.3, 14.1, 13.8]
L = 96
r = 3.87/2
g = 9.81
delta_l = []
alpha = []
F = []
sigma_delta_l = []

for i in range(len(n_zatazovanie)):
    alpha.append(abs((n_zatazovanie[i] - 19)/(2*L)))

for i in range(len(alpha)):
    delta_l.append(r*alpha[i])

for i in range(len(m)):
    F.append(m[i]*g)

sigma_R = 0.01
sigma_L = 0.5
sigma_n = 0.05

for i in range(len(delta_l)):
    sigma_delta_l.append(((abs((n_zatazovanie[i] - 19)/(2*L))*sigma_R)**2 + (r*abs((n_zatazovanie[i] - 19)/(2*L**2))*sigma_L)**2 + (r/(2*L) *sigma_n)**2)**0.5)

x = np.array([1, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
data = np.array([0.0, 0.013999999999999985, 0.016000000000000014, 0.018999999999999986, 0.021999999999999992, 0.025, 0.026999999999999993, 0.03, 0.03300000000000001, 0.036, 0.038000000000000006, 0.040999999999999995, 0.044000000000000004, 0.04599999999999999, 0.049, 0.05199999999999999])

# Perform linear regression
slope, intercept = np.polyfit(x, data, 1)

# Predicted values using the linear model
predicted = slope * x + intercept

# Plotting the data and the linear fit
plt.scatter(x, data, label='Data')
plt.errorbar(x, data, yerr=sigma_delta_l, fmt='o', capsize=7)
plt.plot(x, predicted, color='red', label='Linear Fit')
plt.xlabel('m [kg]')
plt.ylabel('Δl [cm]')
# plt.title('Závislosť prehybu od hmotnosti závaží mosadz')
plt.legend()
plt.grid(True)
plt.show()

print("Slope:", slope)
print("Intercept:", intercept)

# print(alpha)
print(delta_l)
# print(F)
print(sigma_delta_l)

# This is for errors of the fit
model,V=np.polyfit(x,data,1,cov=True)
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

sigma_l_0 = 3/100
sigma_k = 0.00014557886715174206/100
sigma_d = 0.001/100

l_0 = 1.14
g = 9.81
k = 0.02727710843373495/100
pi = 3.14
d = 0.05/100

El_0 = 4*g/(k*pi*d**2)
Ek = -4*l_0*g/(k**2 *pi*d**2)
Ed = -8*l_0*g/(k *pi*d**3)

sigma_E = (El_0*sigma_l_0)**2 + (Ek*sigma_k)**2 + (Ed*sigma_d)**2

E = 4*l_0*g/(k*pi*d**2)
print("sigma_E: " + str(sigma_E**(1/2)))
print("E: " + str(E))




# Second part
# data = np.array([1.3, 2.2, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9, 10])
data = np.array([4.5, 4.9, 5.4, 6.3, 8.2])

# x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
x = np.array([0.01, 0.03, 0.06, 0.11, 0.21])

# error = [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
error = [0.05,0.05,0.05,0.05,0.05]


# Perform linear regression
slope, intercept = np.polyfit(x, data, 1)

# Predicted values using the linear model
predicted = slope * x + intercept

# Plotting the data and the linear fit
plt.scatter(x, data, label='Data')
plt.errorbar(x, data, yerr=error, fmt='o', capsize=7)
plt.plot(x, predicted, color='red', label='Linear Fit')
plt.xlabel('m [kg]')
plt.ylabel('y [mm]')
# plt.title('Závislosť prehybu od hmotnosti závaží mosadz')
plt.legend()
plt.grid(True)
plt.show()

print("Slope:", slope)
print("Intercept:", intercept)

# print(alpha)
print(delta_l)
# print(F)
print(sigma_delta_l)

# This is for errors of the fit
model,V=np.polyfit(x,data,1,cov=True)
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

# Oceľ
k = 9.75151515151515/1000
g = 9.81
a = 11.95/1000
b = 1.96/1000
l = 41/100

E = g*l**3 / (4*k*a*b**3)

sigma_l = 1/100
sigma_k = 0.05231114091403686/1000
sigma_a = 0.01/1000
sigma_b = sigma_a

El = 3*g*l**2/(4*k*a*b**3)
Eb = -3*g*l**3/(4*k*a*b**4)
Ek = -g*l**3/(4*k**2 *a*b**3)
Ea = -g*l**3/(4*k*a**2 *b**3)

sigma_E = (El*sigma_l)**2 + (Ek*sigma_k)**2 + (Ea*sigma_a)**2 + (Eb*sigma_b)**2

print("E = " + str(E))
print("sigma_E: " + str(sigma_E**(1/2)))


# Mosadz
k = 18.4090909090909/1000
g = 9.81
a = 11.79/1000
b = 1.99/1000
l = 41/100

E = g*l**3 / (4*k*a*b**3)

sigma_l = 1/100
sigma_k = 0.2110174297466528/1000
sigma_a = 0.01/1000
sigma_b = sigma_a

El = 3*g*l**2/(4*k*a*b**3)
Eb = -3*g*l**3/(4*k*a*b**4)
Ek = -g*l**3/(4*k**2 *a*b**3)
Ea = -g*l**3/(4*k*a**2 *b**3)

sigma_E = (El*sigma_l)**2 + (Ek*sigma_k)**2 + (Ea*sigma_a)**2 + (Eb*sigma_b)**2

print("E = " + str(E))
print("sigma_E: " + str(sigma_E**(1/2)))
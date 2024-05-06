# n = int(input("Input number of numbers: "))
# n = len(data)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


data = [432.236842105281, 434.210526315807, 451.973684210544, 442.105263157912, 432.23684210528, 424.342105263175, 463.815789473702, 422.368421052649, 420.394736842123, 418.421052631597]
# n = len(data)
# print(n)

# for i in range (n):
#     number = float(input("Input a number: "))
#     data.append(number)

def average_data(data):

    n = len(data)

    sum_average = 0

    for i in range (len(data)):
        sum_average += data[i]

    average = sum_average * 1/n

    print("The average is: " + str(average))

    sum_deviasion = 0
    for i in range (len(data)):
        sum_deviasion += (data[i] - average) ** 2 

    deviation = 1/(n-1) * sum_deviasion
    standard_deviation = deviation ** 0.5

    print("The standard deviation is: " + str(standard_deviation))

    average_error = standard_deviation * 1/(n**0.5)
    print("The error of average is: " + str(average_error))

    return average

average = average_data(data)



R = 8.31446261815324
T = 298.15
pi = 3.14
eta = (1+2.5*4.7*10**(-4))*0.0010518
print(eta)
r = (average/2)*10**(-9)
print(r)
t=5
t_2=10
t_3=15
t_4=20



# A = R*T/(3*pi*eta*r*Na)


S_t = 23.7*10**(-12)
S_2t = 49.1*10**(-12)
S_3t = 70*10**(-12)
S_4t = 81.5**(-12)

S_t = 11.6*10**(-12)
S_2t = 21.8*10**(-12)
S_3t = 34.6*10**(-12)
S_4t = 47.5**(-12)

# A_1 = S_t/(2*t)
# A_2 = S_2t/(2*t_2)
# A_3 = S_3t/(2*t_3)
# A_4 = S_4t/(2*t_4)

# print(A_1)


# NA = (R*T)/(A_1*3*pi*eta*r)
# NA_2 = (R*T)/(A_2*3*pi*eta*r)
# NA_3 = (R*T)/(A_3*3*pi*eta*r)

# data = [NA, NA_2, NA_3]

# print(data)

# print(average_data(data))

data = [23.7, 49.1, 70.1, 81.5]
x = [t, t_2, t_3, t_4]
error_data_x = [0.01, 0.02, 0.03, 0.04]
error_data_y = [0.40, 0.73, 0.95, 0.99]



# def fit(x, data):
#     # model,V=np.polyfit(x,data,1,w=1.0/error_data_x,cov=True)
#     model,V=np.polyfit(x,data,1,cov=True)
#     y_fit=np.polyval(model,x)
#     fig,ax=plt.subplots()
#     # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
#     ax.plot(x,y_fit,c="red")
#     ax.set_xlabel("x", fontsize=15)
#     ax.set_ylabel("y", fontsize=15)
#     plt.show()

#     print("y=ax+b")
#     print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
#     print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
#     print("cov(a,b) = ",V[0,1])
#     print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

#     N_A = (R*T)/(model[0]*3*pi*eta*r)

#     print("N_A is equal to " + str(N_A))

def  fit(x, data, error_data_x, error_data_y):

    # Linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, data)

    # Predicted values
    predicted = slope * x + intercept


    plt.errorbar(x, data, yerr=error_data_y, xerr=error_data_x, fmt='o', elinewidth=2)
    plt.plot(x, predicted, color='red', label='Závislosť stredného kvadratického posunutia od času')
    # plt.plot(x, predicted_2)
    plt.ylabel('Stredné kvadratické posunutie [μm²]')
    plt.xlabel('t [s]')
    plt.title('Závislosť stredného kvadratického posunutia od času')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Slope:", slope)
    print("Intercept:", intercept)

    model,V=np.polyfit(x,data,1,cov=True)
    y_fit=np.polyval(model,x)
    fig,ax=plt.subplots()
    # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    ax.plot(x,y_fit,c="red")
    ax.set_xlabel("x", fontsize=15)
    ax.set_ylabel("y", fontsize=15)
    plt.show()

    print("y=ax+b")
    print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    print("cov(a,b) = ",V[0,1])
    print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

    return model[0], np.sqrt(V[0,0])

# fit(x, data)
A, delta_A = fit(np.array(x), np.array(data), np.array(error_data_x), np.array(error_data_y))
A_1 = A*10**(-12)
delta_A_1 = delta_A*10**(-12)

# data = [S_t, S_2t, S_3t, S_4t]
# fit(np.array(x), np.array(data), np.array(error_data_x), np.array(error_data_y))

NA_1 = (R*T)/(A_1*3*pi*eta*r)

print(NA_1)

data = [
    11.6,
    21.8,
    34.6,
    47.5

]

A, delta_A = fit(np.array(x), np.array(data), np.array(error_data_x), np.array(error_data_y))
A_2 = A*10**(-12)
delta_A_2 = delta_A*10**(-12)

NA_2 = (R*T)/(A_2*3*pi*eta*r)

print(NA_2)

def delta_N_A(R, T, A, eta, r, delta_R, delta_T, delta_A, delta_eta, delta_r):
    dN_dR = T / (3 * A * np.pi * eta * r)
    dN_dT = R / (3 * A * np.pi * eta * r)
    dN_dA = - R * T / (3 * A**2 * np.pi * eta * r)
    dN_deta = - R * T / (3 * A * np.pi * eta**2 * r)
    dN_dr = - R * T / (3 * A * np.pi * eta * r**2)

    delta_N_A = np.sqrt((dN_dR * delta_R)**2 + (dN_dT * delta_T)**2 + (dN_dA * delta_A)**2 + (dN_deta * delta_eta)**2 + (dN_dr * delta_r)**2)
    
    return delta_N_A


R = 8.31446261815324
T = 298.15
pi = 3.14
eta = (1+2.5*4.7*10**(-4))*0.0010518
A = A_1
r = r

delta_R = 0  # Chyba R
delta_T = 2     # Chyba T
delta_A = delta_A_1  # Chyba A
delta_eta = 0# Chyba eta
delta_r = 4.64/2 * 10**(-9)  # Chyba r

delta_N_A_value_1 = delta_N_A(R, T, A, eta, r, delta_R, delta_T, delta_A, delta_eta, delta_r)
print("Chyba N_A:", delta_N_A_value_1)

delta_A = delta_A_2
A = A_2

delta_N_A_value_2 = delta_N_A(R, T, A, eta, r, delta_R, delta_T, delta_A, delta_eta, delta_r)
print("Chyba N_A:", delta_N_A_value_2)



data = [NA_1, NA_2]

def average_data_2(data):

    n = len(data)

    sum_average = 0

    for i in range (len(data)):
        sum_average += data[i]

    average = sum_average * 1/n

    print("The average is: " + str(average))

    sum_deviasion = 0
    for i in range (len(data)):
        sum_deviasion += (data[i] - average) ** 2 

    deviation = 1/(n-1) * sum_deviasion
    standard_deviation = deviation ** 0.5

    print("The standard deviation is: " + str(standard_deviation))

    average_error = standard_deviation * 1/(n**0.5)
    print("The error of average is: " + str(average_error))

    return average, average_error

average, err = average_data_2(data)

print(average)
print(err)
print(delta_N_A_value_1)
print(delta_N_A_value_2)

print(np.sqrt(err**2 + delta_N_A_value_1**2 + delta_N_A_value_2**2))

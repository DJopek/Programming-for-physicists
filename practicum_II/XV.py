import numpy as np
import matplotlib.pyplot as plt
from math import log10

U_g = [0, 0.5, 1]
U_a = [0.053, 10.1, 19.95, 30.05, 40.03, 50.12, 60, 70, 80.1, 90.1, 100, 110.1, 118.4]
I_a_120 = [1.67, 1.2, 0.46]
I_a_110 = [1.5, 1.05, 0.35]
I_a_100 = [1.29, 0.87, 0.25]
I_a_90 = [1.1, 0.7, 0.17]
I_a_80 = [0.92, 0.55,0.1]
I_a_70 = [0.74, 0.4, 0.06]
I_a_60 = [0.56, 0.28, 0.04]
I_a_50 = [0.41, 0.18, 0.02]
I_a_40 = [0.27, 0.11, 0.01]
I_a_30 = [0.16, 0.06, 0]
I_a_20 = [0.08, 0.03, 0]
I_a_10 = [0.04, 0.01, 0]
I_a_0 = [0.01, 0, 0]

I_0 = [0.01, 0.04, 0.08, 0.16, 0.27, 0.41, 0.56, 0.74, 0.92, 1.1, 1.29, 1.5, 1.67]
I_1 = [0, 0.01, 0.03, 0.06, 0.11, 0.18, 0.28, 0.4, 0.55, 0.7, 0.87, 1.05, 1.2]
I_2 = [0, 0, 0, 0, 0.01, 0.02, 0.04, 0.06, 0.1, 0.17, 0.25, 0.35, 0.46]

P_0 = []
P_1 = []
P_2 = []

for i in range(len(I_0)):
    P_0.append(I_0[i]*U_a[i]*10**(-3))
    P_1.append(I_1[i]*U_a[i]*10**(-3))
    P_2.append(I_2[i]*U_a[i]*10**(-3))

print("P_0: ")
print(P_0)
print("P_1: ")
print(P_1)
print("P_2: ")
print(P_2)

def plot_3(x,y_1, y_2, y_3):

    # Create a scatter plot
    plt.scatter(x, y_1, color='blue', marker='o', s=35, label='Ug = 0V')
    plt.scatter(x, y_2, color='green', marker='o', s=35, label='Ug = 0.5V')
    plt.scatter(x, y_3, color='red', marker='o', s=35, label='Ug = 1V')


    # Define the custom function for y, using absolute value of the square root
    def custom_function(x):
        return 1.2-1.2*x/120

    # Generate x-values for the custom function
    x_func = np.linspace(0, 120, 1000)

    # Calculate y-values using the custom function
    y_func = custom_function(x_func)

    # Plot the custom function
    plt.plot(x_func, y_func, color='orange', linestyle=':', zorder=1, label='Záťažová priamka R = 100kΩ')

        # Define the custom function for y, using absolute value of the square root
    def custom_function_2(x):
        return 200/x

    # Generate x-values for the custom function
    x_func = np.linspace(80, 140, 100)

    # Calculate y-values using the custom function
    y_func = custom_function_2(x_func)

    # Plot the custom function
    plt.plot(x_func, y_func, color='black', linestyle=':', zorder=1, label='Pa = 0.2W')

    def custom_function_3(x):
        return 24*(1-x/120)

    # Generate x-values for the custom function
    x_func = np.linspace(110, 120, 1000)

    # Calculate y-values using the custom function
    y_func = custom_function_3(x_func)

    # Plot the custom function
    plt.plot(x_func, y_func, color='green', linestyle=':', zorder=1, label='Záťažová priamka R = 5kΩ')

    # def custom_function_4(x):
    #     return 1000*(0-x/(-8635.378530717315))**(3/2)

    #     # Generate x-values for the custom function
    # x_func = np.linspace(0, 120, 1000)

    # # Calculate y-values using the custom function
    # y_func = custom_function_4(x_func)

    # # Plot the custom function
    # plt.plot(x_func, y_func, color='black', linestyle='-', zorder=1)

    # def custom_function_5(x):
    #     return 1000*(0.5+x/(0.106))**(3/2)

    # # Generate x-values for the custom function
    # x_func = np.linspace(0, 120, 1000)

    # # Calculate y-values using the custom function
    # y_func = custom_function_5(x_func)

    # # Plot the custom function
    # plt.plot(x_func, y_func, color='black', linestyle='-', zorder=1)

    # def custom_function_6(x):
    #     return 1000*(1.5+x/(0.053))**(3/2)

    # # Generate x-values for the custom function
    # x_func = np.linspace(0, 120, 1000)

    # # Calculate y-values using the custom function
    # y_func = custom_function_6(x_func)

    # Plot the custom function
    # plt.plot(x_func, y_func, color='black', linestyle='-', zorder=1)

    # Add labels and title
    plt.xlabel('U [V]')
    plt.ylabel('I [mA]')
    plt.title('')

    # Show the legend
    plt.legend()

    plt.show()

plot_3(U_a, I_0, I_1, I_2)

def plot_2(x,y_1, y_2):

    # Create a scatter plot
    plt.scatter(x, y_1, color='blue', marker='o', s=35, label='Zosilnenie pri R = 100kΩ')
    plt.scatter(x, y_2, color='green', marker='o', s=35, label='Zosilnenie pri R = 5kΩ')

    # Add labels and title
    plt.xlabel('log10(f)[kHz]')
    plt.ylabel('A')
    plt.title('')

    # Show the legend
    plt.legend()

    plt.show()

def plot_1(x,y_1):

    # Create a scatter plot
    plt.scatter(x, y_1, color='blue', marker='o', s=35, label='A od R')

    # Add labels and title
    plt.xlabel('R[Ω]')
    plt.ylabel('A')
    plt.title('')

    # Show the legend
    plt.legend()

    plt.show()


R_1 = 10**5
R_2 = 5*10**3
err_U_1 = 0.1
err_U_2 = 0.05
f = [0.03, 0.05, 0.07, 0.09, 0.3, 0.5, 0.7, 0.9, 3, 5, 7, 9, 30, 50, 70, 90, 1000]
U_1 = [6.1, 7.2, 7.7, 7.9, 8.3, 8.4, 8.4, 8.4, 8.2, 8.0, 7.8, 7.6, 4.4, 3.0, 2.2, 1.6, 1.5]
U_2 = [0.85, 1, 1.1, 1.1, 1.1, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.15, 1.1, 1.1, 1.05, 1]
A_1 = []
A_2 = []

R = [5*10**3, 6*10**3, 7*10**3, 8*10**3, 9*10**3, 10**4, 2*10**4, 3*10**4, 4*10**4, 5*10**4, 6*10**4, 7*10**4, 8*10**4, 9*10**4, 10**5]
U = [1.15, 1.4, 1.6, 1.8, 2, 2.3, 3.6, 4.6, 5.6, 6.2, 6.8, 7.2, 7.6, 8, 8.2]
A = []

def A_vals (U, A):
    for i in range(len(U)):
        A.append(U[i]/0.2)

A_vals(U_1, A_1)
A_vals(U_2, A_2)
A_vals(U, A)

print(A_1)
print(A_2)
print(A)

for i in range(len(f)):
    f[i] = log10(f[i]*10**3)

plot_2(f, A_1, A_2)
plot_1(R, A)

# def mu(U_1, U_2, I):
#     mu = U_1/(U_2-I**(2/3))
#     print(mu)

# for i in range(3):
#     mu(U_a[0], U_g[i], I_a_0[i]/1000)
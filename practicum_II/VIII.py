import numpy as np
import matplotlib.pyplot as plt
from linear_fit import fit
from average import statistics


# Data and processing the data
y_A = []
f_A = []
f_12_A = [500, 526, 454, 477, 565, 594, 390, 409, 331, 345]
C_A = [400, 500, 300, 700, 1000] 

y_B = []
f_B = []
f_12_B = [427, 459, 543, 581, 359, 388, 306, 326]
C_B = [500, 300, 700, 1000] 

y_AB_I = []
f_AB_I = []
f_12_AB_I = [346, 394, 302, 343, 272, 310, 264, 229, 192, 222]
C_AB_I = [300, 400, 500, 700, 1000] 

y_AB_II = []
f_AB_II = []
f_12_AB_II = [569, 459, 496, 402, 363, 442, 310, 377, 261, 314]
C_AB_II = [300, 400, 500, 700, 1000] 


def average(f_12, y, f):
    for i in range(10):
        if i % 2 != 1:
            f.append((f_12[i]+f_12[i+1])/2)

    print(f)

    for i in range(5):
        y.append(1/((f[i]*2*3.1415)**2))

    print(y)

def average_alternative(f_12, y, f):
    for i in range(8):
        if i % 2 != 1:
            f.append((f_12[i]+f_12[i+1])/2)

    print(f)

    for i in range(4):
        y.append(1/((f[i]*2*3.1415)**2))

    print(y)

average(f_12_A, y_A, f_A)
L_A, err_L_A, LC_0_A, err_LC_0_A = fit(y_A, C_A)

average_alternative(f_12_B, y_B, f_B)
L_B, err_L_B, LC_0_B, err_LC_0_B  = fit(y_B, C_B)

average(f_12_AB_I, y_AB_I, f_AB_I)
L_AB_I, err_L_AB_I, q_AB_I, err_q_AB_I = fit(y_AB_I, C_AB_I)

average(f_12_AB_II, y_AB_II, f_AB_II)
L_AB_II, err_L_AB_II, q_AB_II, err_q_AB_II = fit(y_AB_II, C_AB_II)

U_10 = [5, 10, 20, 25, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15]
f_10 = [382, 390, 397, 399, 401, 404, 407, 465, 470, 478, 487, 503, 520, 588]
U_100 = [21, 25, 27, 25]
f_100 = [417, 421, 423, 427]

x = []  # X-coordinates
y = [] # Y-coordinates

for i in range(14):
    y.append(np.sqrt(U_10[i]/100))
    x.append(f_10[i]/449)

for i in range(4):
    y.append(np.sqrt(U_100[i]/30))
    x.append(f_100[i]/449)

print("x: ")
print(x)
print("y: ")
print(y)


def plot(x,y):

    # Create a scatter plot
    plt.scatter(x, y, color='blue', marker='o', s=35, label='Points')

    # Set y-axis limits
    # plt.ylim(0, 2)

    # Add labels and title
    plt.xlabel('')
    plt.ylabel('')
    plt.title('')

    # Show the legend
    plt.legend()

    # Display the plot
    # plt.show()

# Define the constant d for the custom function
d = 0.231

# Define the custom function for y, using absolute value of the square root
def custom_function(x):
    return d**2 / (d**2 + (x - 1/x)**2)

# Generate x-values for the custom function
x_func = np.linspace(0.1, 3, 400)  # From 0.1 to 5, avoiding x = 0

# Calculate y-values using the custom function
y_func = custom_function(x_func)

# Create the plot
plt.figure(figsize=(8, 6))  # Create a figure with a specific size

# Plot the scatter data points
plot(x, y)

# Plot the custom function
plt.plot(x_func, y_func, label=r'$y^2 = {\frac{d^2}{d^2 + \left(x - \frac{1}{x}\right)^2}}$', color='orange', linestyle=':', zorder=1)

# Set labels and title
plt.xlabel('')
plt.ylabel('')
plt.title('')

# Add a legend
plt.legend()

# Display the plot
plt.show()

# Formulas and errors
C_0_A = LC_0_A/L_A
err_LC_0_A = np.sqrt((err_LC_0_A/L_A)**2 + (err_L_A*LC_0_A/(L_A**2))**2)

print("C_0_A: " + str(C_0_A))
print("err_C_0_A: " + str(err_LC_0_A))

C_0_B = LC_0_B/L_B
err_LC_0_B = np.sqrt((err_LC_0_B/L_B)**2 + (err_L_B*LC_0_B/(L_B**2))**2)

print("C_0_B: " + str(C_0_B))
print("err_C_0_B: " + str(err_LC_0_B))

M_I = (L_AB_I - L_A - L_B)/2
M_II = -(L_AB_II - L_A - L_B)/2

err_M_I = np.sqrt((err_L_AB_I**2 + err_L_A**2 + err_L_B**2)/4)
err_M_II = np.sqrt((err_L_AB_II**2 + err_L_A**2 + err_L_B**2)/4)

print("M_I: " + str(M_I))
print("M_II: " + str(M_II))
print("err_M_I: " + str(err_M_I))
print("err_M_II: " + str(err_M_II))

M = (L_AB_I - L_AB_II)/4
err_M = np.sqrt((err_L_AB_I**2 + err_L_AB_II**2)/16)

print("M: " + str(M))
print("err_M: " + str(err_M))

data = [61.27, 78.72]

M = statistics(data)

print("M average: " + str(M))

data = [402, 496]

average = statistics(data)

print("average: " + str(average))

err_d = 0.025

Q = 1/d

print("Q: " + str(Q))

err_Q = np.sqrt((err_d/d**2)**2)
print("err_Q: " + str(err_Q))

R = d*np.sqrt(L_AB_II/400)
err_R = np.sqrt((np.sqrt(L_AB_II/400)*err_d)**2 + (0.5*d/np.sqrt(L_AB_II*400)*err_L_AB_II)**2)

print("R: " + str(R))
print("err_R: " + str(err_R))
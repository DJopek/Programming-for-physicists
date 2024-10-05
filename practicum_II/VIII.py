import numpy as np
import matplotlib.pyplot as plt
from linear_fit import fit


y_A = []
f_A = []
f_12_A = [500, 526, 454, 477, 565, 594, 390, 409, 331, 345]
C_A = [400, 500, 300, 700, 1000] 

y_B = []
f_B = []
f_12_B = [501, 530, 427, 459, 543, 581, 359, 388, 306, 326]
C_B = [400, 500, 300, 700, 1000] 

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

average(f_12_A, y_A, f_A)
fit(y_A, C_A)

# average(f_12_B, y_B, f_B)
# fit(y_B, C_B)

# average(f_12_AB_I, y_AB_I, f_12_AB_I)
# fit(y_AB_I, C_AB_I)

# average(f_12_AB_II, y_AB_II, f_12_AB_II)
# fit(y_AB_II, C_AB_II)

# Sample data points
U_10 = [5, 10, 20, 25, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15]
f_10 = [382, 390, 397, 399, 401, 404, 407, 465, 470, 478, 487, 503, 520, 588]
U_100 = [21, 25, 27, 25]
f_100 = [417, 421, 423, 427]

x = []  # X-coordinates
y = [] # Y-coordinates

for i in range(14):
    y.append(U_10[i]/100)
    x.append(f_10[i]/449)

for i in range(4):
    y.append(U_100[i]/30)
    x.append(f_100[i]/449)


def plot(x,y):

    # Create a scatter plot
    plt.scatter(x, y, color='blue', label='Points')

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
d = 0.13

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
plt.plot(x_func, y_func, label=r'$y = |\sqrt{\frac{d^2}{d^2 + \left(x - \frac{1}{x}\right)^2}}|$', color='red', zorder=1)

# Set labels and title
plt.xlabel('')
plt.ylabel('')
plt.title('')

# Add a legend
plt.legend()

# Display the plot
# plt.show()


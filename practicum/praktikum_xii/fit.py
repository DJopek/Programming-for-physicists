import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.array([
    [20, 332.083],
    [20, 332.035],
    [21, 329.051],
    [30, 267.055],
    [40, 226.045],
    [50, 193.031],
    [60, 165.049]
])

x_values = data[:, 0]
y_values = data[:, 1]

# Perform exponential fit
popt, pcov = np.polyfit(x_values, np.log(y_values), 1, cov=True)
a = np.exp(popt[1])
b = popt[0]

# Calculate fitted values
y_fit = a * np.exp(b * x_values)

# Plot data and fitted curve
plt.scatter(x_values, y_values, label='Data')
plt.plot(x_values, y_fit, color='red', label='Exponential Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Fit')
plt.legend()
plt.show()

# Print fit parameters
print("y = a * exp(bx)")
print("a =", a)
print("b =", b)

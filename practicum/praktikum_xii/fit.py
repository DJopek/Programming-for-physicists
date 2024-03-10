import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.array([
    [20, 0.0009954502075518001],
    [20, 0.0009953063230110002], 
    [21, 0.000986163872694], 
    [30, 0.0007984375138740001], 
    [40, 0.000673518392547], 
    [50, 0.000572716027884], 
    [60, 0.0004873153589304001],
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

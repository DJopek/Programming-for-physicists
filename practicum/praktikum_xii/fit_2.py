import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.array([
    [20, 0.997101105],
    [21, 0.988140153],
    [30, 0.8019661650000001],
    [40, 0.678813135],
    [50, 0.579672093],
    [60, 0.4956421470000001],
])

x_values = data[:, 0] + 273.15
print(x_values)
y_values = data[:, 1]

# Perform exponential fit
popt, pcov = np.polyfit(x_values, np.log(y_values), 1, cov=True)
a = np.exp(popt[1])
b = popt[0]

# Calculate fitted values
y_fit_exp = a * np.exp(b * x_values)

# Plot data and exponential fit
plt.scatter(x_values, y_values, label='Data')
plt.plot(x_values, y_fit_exp, color='red', label='Exponential Fit')
plt.xlabel('T [K]')
plt.ylabel('Viscosity [mm2 s-1]')
plt.title('Exponential Fit')
plt.legend()
plt.savefig("fit_exp.png",dpi=600)
plt.show()

# Print exponential fit parameters
print("Exponential Fit Parameters:")
print("a =", a)
print("b =", b)

# Convert exponential fit to linear fit
log_y_values = np.log(y_values)
linear_model, linear_cov = np.polyfit(x_values, log_y_values, 1, cov=True)

# Calculate fitted values for linear fit
linear_y_fit = np.polyval(linear_model, x_values)

# Plot data and linear fit
plt.scatter(x_values, log_y_values, label='Data (log scale)')
plt.plot(x_values, linear_y_fit, color='green', label='Linear Fit (log scale)')
plt.xlabel('x')
plt.ylabel('ln(y)')
plt.title('Linear Fit (log scale)')
plt.legend()
plt.savefig("fit_ln.png",dpi=600)
plt.show()

# Print linear fit parameters
print("\nLinear Fit Parameters (log scale):")
print("slope =", linear_model[0])
print("intercept =", linear_model[1])
print("covariance matrix:\n", linear_cov)

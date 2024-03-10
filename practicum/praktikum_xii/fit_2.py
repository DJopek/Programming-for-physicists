import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

# data = np.array([
#     [20, 0.997101105],
#     [21, 0.988140153],
#     [30, 0.8019661650000001],
#     [40, 0.678813135],
#     [50, 0.579672093],
#     [60, 0.4956421470000001],
# ])

x_values = data[:, 0] + 273.15
y_values = data[:, 1]

# Define the fitting function
def exponential_function(x, a, b):
    return a * np.exp(b / x)

# Perform curve fitting
popt, pcov = curve_fit(exponential_function, x_values, y_values)

# Calculate fitted values
y_fit_exp = exponential_function(x_values, *popt)

# Extract standard deviations (errors) of parameters
perr = np.sqrt(np.diag(pcov))

# Plot data and exponential fit
plt.scatter(x_values, y_values, label='Data')
plt.plot(x_values, y_fit_exp, color='red', label='Exponential Fit')
plt.xlabel('T [K]')
plt.ylabel('Viscosity [mm2 s-1]')
plt.title('Exponential Fit')
plt.legend()
plt.savefig("fit_exponential.png",dpi=600)
plt.show()

# Print exponential fit parameters
print("Exponential Fit Parameters:")
print("a =", popt[0])
print("b =", popt[1])

# Print standard deviations of parameters
print("Standard deviations (errors) of parameters:")
print("Error of a:", perr[0])
print("Error of b:", perr[1])


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

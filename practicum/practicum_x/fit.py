import numpy as np
import matplotlib.pyplot as plt

# Input data
# data = np.array([214, 314, 432, 645, 853, 968, 1064, 1279, 1496, 1655])
# data = np.array([214, 432, 645, 853, 1064, 1279, 1496, 1655, 1919, 2134])
data = np.array([168, 342, 510, 676, 846, 1018, 1211, 1366, 1544, 1711])


# # Independent variable (x values)
# x = np.arange(1, len(data) + 1)

# # Perform linear regression
# slope, intercept = np.polyfit(x, data, 1)

# # Predicted values using the linear model
# predicted = slope * x + intercept

# # Plotting the data and the linear fit
# plt.scatter(x, data, label='Data')
# plt.plot(x, predicted, color='red', label='Linear Fit')
# plt.xlabel('k')
# plt.ylabel('f [Hz]')
# plt.title('Závislosť frekvencie od počtu polvĺn')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Print the slope and intercept
# print("Slope:", slope)
# print("Intercept:", intercept)
# Independent variable (x values)
x = np.arange(1, len(data) + 1)

# Perform linear regression
slope, intercept = np.polyfit(x, data, 1)

# Predicted values using the linear model
predicted = slope * x + intercept

# Plotting the data and the linear fit
plt.scatter(x, data, label='Data')
plt.plot(x, predicted, color='red', label='Linear Fit')
plt.xlabel('k')
plt.ylabel('f [Hz]')
plt.title('Závislosť frekvencie od počtu polvĺn')
plt.legend()
plt.grid(True)
plt.show()

# Print the slope and intercept
print("Slope:", slope)
print("Intercept:", intercept)

# Compute errors of coefficients
residuals = data - predicted
variance = np.var(residuals)
slope_error = np.sqrt(variance / np.sum((x - np.mean(x))**2))
intercept_error = slope_error * np.sqrt(np.mean(x**2))
print("Slope Error:", slope_error)
print("Intercept Error:", intercept_error)
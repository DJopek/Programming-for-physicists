import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 1: Define the custom function
def custom_function(x, a):
    return a * np.sqrt(x)

# Step 2: Generate some example data
# True parameter value for a
true_a = 2
# Generate x values
x_data = np.linspace(1, 10, 50)
# Generate y values with some added noise
y_data = true_a * np.sqrt(x_data) + np.random.normal(0, 0.5, size=x_data.size)

# Step 3: Perform the curve fitting
# Initial guess for parameter a
initial_guess = [1]
params, covariance = curve_fit(custom_function, x_data, y_data, p0=initial_guess)

# Extract the fitted parameter
fitted_a = params[0]
# Calculate the standard deviation errors from the covariance matrix
errors = np.sqrt(np.diag(covariance))

# Print the fitted parameter and its error
print(f"Fitted parameter a: {fitted_a} ± {errors[0]}")

# Step 4: Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data', color='red')
plt.plot(x_data, custom_function(x_data, fitted_a), label='Fitted function', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

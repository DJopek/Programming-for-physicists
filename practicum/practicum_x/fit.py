import numpy as np
import matplotlib.pyplot as plt

# Input data

data = np.array([0.0, 0.013999999999999985, 0.016000000000000014, 0.018999999999999986, 0.021999999999999992, 0.025, 0.026999999999999993, 0.03, 0.03300000000000001, 0.036, 0.038000000000000006, 0.040999999999999995, 0.044000000000000004, 0.04599999999999999, 0.049, 0.05199999999999999])
data = np.array([1.3, 2.2, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9, 10])
data = np.array([4.5, 4.9, 5.4, 6.3, 8.2])


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
x = np.array([1, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])

# x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
# x = np.array([0.01, 0.03, 0.06, 0.11, 0.21])

# Perform linear regression
slope, intercept = np.polyfit(x, data, 1)

# Predicted values using the linear model
predicted = slope * x + intercept

# Plotting the data and the linear fit
plt.scatter(x, data, label='Data')
plt.plot(x, predicted, color='red', label='Linear Fit')
plt.xlabel('m [kg]')
plt.ylabel('y [mm]')
plt.title('Závislosť prehybu od hmotnosti závaží mosadz')
plt.legend()
plt.grid(True)
plt.show()

# Print the slope and intercept
print("Slope:", slope)
print("Intercept:", intercept)

model,V=np.polyfit(x,data,1,cov=True)
y_fit=np.polyval(model,x)
fig,ax=plt.subplots()
# ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
ax.plot(x,y_fit,c="red")
ax.set_xlabel("x", fontsize=15)
ax.set_ylabel("y", fontsize=15)
# plt.show()

print("y=ax+b")
print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
print("cov(a,b) = ",V[0,1])
print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

# Compute errors of coefficients
# residuals = data - predicted
# variance = np.var(residuals)
# slope_error = np.sqrt(variance / np.sum((x - np.mean(x))**2))
# intercept_error = slope_error * np.sqrt(np.mean(x**2))
# print("Slope Error:", slope_error)
# print("Intercept Error:", intercept_error)
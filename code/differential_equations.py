import numpy as np
import matplotlib.pyplot as plt

a = 9.81

steps = int(input("Input number of steps: "))
x_0 = float(input("Input a boundary condition for x: "))
v_0 = float(input("Input a boundary condition for v: "))

x_values = []
v_values = []

plot_vals = np.linspace(0, 10000, steps).tolist()

x_i_minus_1 = x_0
v_i_minus_1 = v_0
dt = 0.001

v_fin = 0
x_fin = 0

for i in range (0, steps):

    x_i = x_i_minus_1 + v_i_minus_1 * dt
    v_i = v_i_minus_1 + a * dt

    x_fin += x_i
    v_fin += v_i

    x_values.append(x_fin)
    v_values.append(v_fin)

    x_i_minus_1 = x_i
    v_i_minus_1 = v_i


plt.plot(plot_vals, x_values)
plt.plot(plot_vals, v_values)
plt.grid(True)
plt.show()


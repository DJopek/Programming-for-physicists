import os
import numpy as np
import matplotlib.pyplot as plt

# Adresár so všetkými .txt súbormi
directory = "/Users/davidjopek/Downloads/koto_Data/"

kombinacia = []

epsilon = []

# Prechádzanie všetkých súborov v adresári
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as file:
            next(file)
            data = np.loadtxt(file)
            x = data[:, 0]
            y = data[:, 1]
            model = np.polyfit(x, y, 1)
            slope, intercept = model

            # print("File:", filename)
            kombinacia.append(filename)
            # print("Linear model coefficients:")
            # print("Slope (m):", slope)
            epsilon.append(slope)
            # print("Intercept (b):", intercept)

            plt.plot(x, y, label=filename)

plt.xlabel('t[s]')
plt.ylabel('ω[1/s]')
plt.title('Lineárne regresie pre závažia')
plt.grid(True)
plt.legend()
plt.show()

print(kombinacia)
print(epsilon)

epsilon_values = [
    0.0552, 0.0905, 0.1492, 0.2155, 0.2907,
    0.1063, 0.1789, 0.2586, 0.3649, 0.5325,
    0.1703, 0.2507, 0.3754, 0.5293, 0.7401,
    0.2273, 0.3339, 0.4902, 0.6926, 0.9844
]


m = [11.9, 16.9, 24.7, 34.4, 49.1, 11.9, 16.9, 24.7, 34.4, 49.1, 11.9, 16.9, 24.7, 34.4, 49.1, 11.9, 16.9, 24.7, 34.4, 49.1, 11.9, 16.9, 24.7, 34.4, 49.1]
r = [60/1000, 60/1000, 60/1000, 60/1000, 60/1000, 100/1000, 100/1000, 100/1000, 100/1000, 100/1000, 140/1000, 140/1000, 140/1000, 140/1000, 140/1000, 180/1000, 180/1000, 180/1000, 180/1000, 180/1000]
g = 9.81

alfa = []
I = []


for i in range(len(epsilon_values)):
    alfa.append(1/epsilon_values[i])
    I.append(m[i]/1000 * (r[i]/2) **2 * (g/((r[i]/2)*epsilon_values[i])-1))


print(alfa)
print(I)
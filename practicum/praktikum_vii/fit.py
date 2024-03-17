import numpy as np
import matplotlib.pyplot as plt

# Zadané dáta
h = np.array([15, 25, 31, 40, 49])
kappa = np.array([0.00533329540767697, 0.03792673078334903, 0.065503355704698, 0.08871365204534265, 0.10200598898798968])
# kappa = np.array([0.03242390605830483, 0.07680945347119635, 0.08920728858433248, 0.1425350824171333, 0.1917525773195878])

# Fitovanie polynómu druhého stupňa
model = np.polyfit(h, kappa, 2)

# Generovanie hodnôt pre vykreslenie fitovaného polynómu
x_fit = np.linspace(min(h), max(h), 100)
y_fit = np.polyval(model, x_fit)

# Vykreslenie dát a fitovaného polynómu
plt.figure()
plt.errorbar(h, kappa, fmt='o', yerr=0.01, label='Dáta s chybami')
plt.plot(x_fit, y_fit, 'r-', label='Fitovaný polynóm 2. stupňa')
plt.xlabel('h (cm)')
plt.ylabel('$\kappa$')
plt.legend()
plt.title('Fitovanie polynómu 2. stupňa')
plt.grid(True)
plt.show()

# Výpis koeficientov fitovaného polynómu
print("Koeficienty fitovaného polynómu druhého stupňa:")
print("a0 =", model[2])
print("a1 =", model[1])
print("a2 =", model[0])
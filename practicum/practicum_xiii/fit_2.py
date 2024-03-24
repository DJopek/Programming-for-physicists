import numpy as np
import matplotlib.pyplot as plt

# Dané dáta
alpha = [18.115942028985508, 11.049723756906078, 6.702412868632708, 4.640371229698376, 3.439972480220158, 9.40733772342427, 5.589714924538848, 3.8669760247486464, 2.740476842970677, 1.8779342723004695, 5.871990604815032, 3.988831272437176, 2.663825253063399, 1.889287738522577, 1.3511687609782461, 4.399472063352397, 2.994908655286014, 2.039983680130559, 1.443834825295986, 1.0158472165786265]
I_star = [0.06343439869565219, 0.05494246955801105, 0.04869901664879357, 0.04694778709976799, 0.049663859535603726, 0.05488040992474131, 0.04629341238121856, 0.04678801798143852, 0.04615461386681284, 0.045104573943661984, 0.047926011785085154, 0.0462084943478261, 0.045061415391582316, 0.04446110181749481, 0.045316726578840706, 0.046126707228332606, 0.04455017199460916, 0.044287139302325584, 0.04357316479353162, 0.04363966301909793]

# Lineárny fit
model, cov = np.polyfit(alpha, I_star, 1, cov=True)
alpha_fit = np.linspace(min(alpha), max(alpha), 100)
I_star_fit = np.polyval(model, alpha_fit)

# Výpočet chýb koeficientov
slope_error = np.sqrt(cov[0, 0])
intercept_error = np.sqrt(cov[1, 1])

# Vypísanie koeficientov a chýb
print("Koeficienty lineárneho fitu:")
print("Sklon: {:.4f} ± {:.4f}".format(model[0], slope_error))
print("Posun: {:.4f} ± {:.4f}".format(model[1], intercept_error))

# Vykreslenie dát a lineárneho fitu
plt.scatter(alpha, I_star, label='Dáta')
plt.plot(alpha_fit, I_star_fit, 'r', label='Lineárny fit')
plt.xlabel('α [s2]')
plt.ylabel('I* [kgm2]')
plt.title('Závislosť I* od α')
plt.legend()
plt.grid(True)
plt.show()

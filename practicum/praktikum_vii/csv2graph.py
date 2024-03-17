import pandas as pd
import matplotlib.pyplot as plt

# Načítanie dát zo súboru CSV
data = pd.read_csv('/Users/davidjopek/Downloads/druha_pruzina.csv')

# Rozdelenie dát na hodnoty osi x a osi y
x = data['čas']
y = data['Poloha']

# Vykreslenie grafu
plt.plot(x, y, linestyle='-')
plt.xlabel('čas')
plt.ylabel('poloha')
plt.title('Rázy druhá pružina pružina')
plt.grid(True)
plt.show()

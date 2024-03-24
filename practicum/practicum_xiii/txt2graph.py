# import matplotlib.pyplot as plt

# # Načítanie dát zo súboru
# with open("/Users/davidjopek/Downloads/koto_Data/TO 180 mm & E.txt", "r") as file:
#     next(file)
#     data = file.readlines()

# # Oddelenie x a y hodnôt
# x = []
# y = []
# for line in data:
#     line = line.strip().split()
#     x.append(float(line[0]))
#     y.append(float(line[1]))

# # Vytvorenie grafu
# plt.plot(x, y)
# plt.xlabel('t[s]')
# plt.ylabel('ω[1/s]')
# plt.title('Závažie E, polomer kladky 180mm')
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt

# Pre prvého súboru
with open("/Users/davidjopek/Downloads/koto_Data/TO 100 mm & A.txt", "r") as file:
    next(file)
    data = file.readlines()

x1 = []
y1 = []
for line in data:
    line = line.strip().split()
    x1.append(float(line[0]))
    y1.append(float(line[1]))

# Pre druhý súbor
with open("/Users/davidjopek/Downloads/koto_Data/TO 140 mm & C.txt", "r") as file:
    next(file)
    data = file.readlines()

x2 = []
y2 = []
for line in data:
    line = line.strip().split()
    x2.append(float(line[0]))
    y2.append(float(line[1]))

# Pre tretí súbor
with open("/Users/davidjopek/Downloads/koto_Data/TO 180 mm & E.txt", "r") as file:
    next(file)
    data = file.readlines()

x3 = []
y3 = []
for line in data:
    line = line.strip().split()
    x3.append(float(line[0]))
    y3.append(float(line[1]))

# Vytvorenie grafu pre všetky súbory
plt.plot(x1, y1, label='180 mm')
plt.plot(x2, y2, label='200 mm')
plt.plot(x3, y3, label='250 mm')
plt.xlabel('t[s]')
plt.ylabel('ω[1/s]')
plt.title('Závažia A,C,E')
plt.grid(True)
plt.legend()
plt.show()

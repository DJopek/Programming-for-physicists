m = [1, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]
n_zatazovanie = [19, 17.6, 17.4, 17.1, 16.8, 16.5, 16.3, 16, 15.7, 15.4, 15.2, 14.9, 14.6, 14.4, 14.1, 13.8]
n_odoberanie = [19, 17.6, 17.3, 17.0, 16.8, 16.5, 16.2, 16.0, 15.7, 15.4, 15.1, 14.8, 14.6, 14.3, 14.1, 13.8]
L = 96
r = 3.84/2
g = 9.81
delta_l = []
alpha = []
F = []

for i in range(len(n_zatazovanie)):
    alpha.append(abs((n_zatazovanie[i] - 19)/(2*L)))

for i in range(len(alpha)):
    delta_l.append(r*alpha[i])

for i in range(len(m)):
    F.append(m[i]*g)

print(alpha)
print(delta_l)
print(F)
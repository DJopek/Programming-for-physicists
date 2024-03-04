# s = 5/100
# t=6.41
# r = ((1.85 + 3.05)/2)/1000

# rho = 965
# rho_t = 2200
# g=9.81

# v=s/t

# n = (2*r**2*(rho_t-rho)*g)/(9*v)

# Re = (2*r*rho_t*v)/(n)

# print(str(Re))

# Read d_values_biels from .dat file
with open('measurement.dat', 'r') as file:
    d_values_biels = file.readlines()

# Parse d_values_biels
d_values_biels = [line.strip().split() for line in d_values_biels]

# Extract column names
column_names = d_values_biels[0]

# Skip the header line
d_values_biels = d_values_biels[1:]

# Convert d_values_biels to appropriate types
d_values_biels = [[float(value) for value in line] for line in d_values_biels]

print(d_values_biels)

# Extract values
d_values_žltá = [(line[0] + line[1]) / 4000 for line in d_values_biels]
d_values_zelena = [(line[3] + line[4]) / 4000 for line in d_values_biels]
d_values_biela = [(line[6] + line[7]) / 4000 for line in d_values_biels]

l_values = [line[-2] for line in d_values_biels]
rho_values = [line[-1] for line in d_values_biels]

t_values_žltá = [line[2] for line in d_values_biels]
t_values_zelená = [line[5] for line in d_values_biels]
t_values_biela = [line[8] for line in d_values_biels]


print(d_values_biela)
print(t_values_biela)
print(l_values)
print(rho_values)

# Constants
rho_t = 2200
g = 9.81

# Calculate v and n for each d_values_biels point
for r, t, l, rho in zip(d_values_žltá, t_values_žltá, l_values, rho_values):
    v = l / t
    n = (2 * r ** 2 * (rho_t - rho) * g) / (9 * v)
    Re = (2 * r * rho_t * v) / n
    print("Viscosity =", n)

for r, t, l, rho in zip(d_values_zelena, t_values_zelená, l_values, rho_values):
    v = l / t
    n = (2 * r ** 2 * (rho_t - rho) * g) / (9 * v)
    Re = (2 * r * rho_t * v) / n
    print("Viscosity =", n)

for r, t, l, rho in zip(d_values_biela, t_values_biela, l_values, rho_values):
    v = l / t
    n = (2 * r ** 2 * (rho_t - rho) * g) / (9 * v)
    Re = (2 * r * rho_t * v) / n
    print("Viscosity biela =", n)



sum_average = 0

for i in range (len(d_values_žltá)):
    sum_average += d_values_žltá[i]

average = sum_average * 1/len(d_values_žltá)

print("The average is: " + str(average))

sum_deviasion = 0
for i in range (len(d_values_žltá)):
    sum_deviasion += (d_values_žltá[i] - average) ** 2 

deviation = 1/(len(d_values_žltá)-1) * sum_deviasion
standard_deviation = deviation ** 0.5

print("The standard deviation is: " + str(standard_deviation))

average_error = standard_deviation * 1/(len(d_values_žltá)**0.5)
print("The error of average is: " + str(average_error))
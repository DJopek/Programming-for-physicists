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

# Read data from .dat file
with open('laminar_test.dat', 'r') as file:
    data = file.readlines()

# Parse data
data = [line.strip().split() for line in data]

# Extract column names
column_names = data[0]

# Skip the header line
data = data[1:]

# Convert data to appropriate types
data = [[float(value) for value in line] for line in data]

print(data)

# Extract values
d_values_žltá = [(line[0] + line[1]) / 4000 for line in data]
d_values_zelena = [(line[3] + line[4]) / 4000 for line in data]
d_values_biela = [(line[6] + line[7]) / 4000 for line in data]

l_values = [line[-2] for line in data]
rho_values = [line[-1] for line in data]

t_values_žltá = [line[2] for line in data]
t_values_zelená = [line[5] for line in data]
t_values_biela = [line[8] for line in data]



print(d_values_biela)
print(t_values_biela)
print(l_values)
print(rho_values)

# Constants
rho_t = 2200
g = 9.81

# Calculate v and n for each data point
for r, t, l, rho in zip(d_values_žltá, t_values_žltá, l_values, rho_values):
    v = l / t
    n = (2 * r ** 2 * (rho_t - rho) * g) / (9 * v)
    Re = (2 * r * rho_t * v) / n
    print("Reynolds number (Re) =", Re)

for r, t, l, rho in zip(d_values_zelena, t_values_zelená, l_values, rho_values):
    v = l / t
    n = (2 * r ** 2 * (rho_t - rho) * g) / (9 * v)
    Re = (2 * r * rho_t * v) / n
    print("Reynolds number (Re) =", Re)

for r, t, l, rho in zip(d_values_biela, t_values_biela, l_values, rho_values):
    v = l / t
    n = (2 * r ** 2 * (rho_t - rho) * g) / (9 * v)
    Re = (2 * r * rho_t * v) / n
    print("Reynolds number (Re) =", Re)
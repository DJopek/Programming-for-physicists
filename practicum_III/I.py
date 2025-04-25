from average import statistics
from table import table
from fit import fit
from fit import fit_err

a = [12.122, 12.055, 12.060, 12.154, 12.077]

avg, stddev, erravg =  statistics(a)

sigma_a = 0.01
error_a = []

for i in range(len(a)):
    error_a.append(sigma_a)
sigma_a = (erravg**2 + sigma_a**2)**0.5

print("Error of a is: " + str(sigma_a))

table(values=[a], errors=[error_a])

def x_vals(x, x_0):

    x_values = []

    for i in range(len(x)):
        x_values.append(x[i]-x_0)

    return x_values

def linfit(x,A,B):
    return A*x+B

def speed(ratio):
    return 8*3.1415*(f+2*a)*f/ratio

f = 5.00
a = avg

#1
x_0 = 8/1000 #m
sigma_x_0 = 0.5/1000 #m
nu = [0.0, 898.0, 789.0, 685.0, 573.0, 479.0]
sigma_nu_1 = [0.0, 0.2, 2.0, 2.0, 3.0, 3.0]
x = [8/1000, 14/1000, 13/1000, 12.5/1000, 12/1000, 11/1000]
nu_1 = nu

for i in range(len(nu)):
    nu[i] = nu[i]/2
    sigma_nu_1[i] = sigma_nu_1[i]/2

x_1 = x_vals(x, x_0)
# fit(nu, x_1, linfit)

ratio_1 = 1.3166457714211944*10**(-5)
# sigma_ratio_1 = 

c_1 = speed(ratio_1)
print(c_1)

#2
x_0 = 8/1000 #m
sigma_x_0 = 0.5/1000 #m
nu = [float(0), 898.3, 860.0, 800.0, 775.0, 720.0, 696.0, 673.0, 644.0, 600.0, 552.0, 530.0, 522.0, 481.0, 441.0]
sigma_nu_2 = [float(0), 0.2, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0]
x = [8.0, 14.0, 13.75, 13.5, 13.0, 12.75, 12.5, 12.25, 12.25, 12.0, 11.75, 11.75, 11.5, 11.25, 10.75]
nu_2 = nu

for i in range(len(nu)):
    nu[i] = nu[i]/2
    sigma_nu_2[i] = sigma_nu_2[i]/2

for i in range(len(x)):
    x[i] = x[i]/1000

x_2 = x_vals(x, x_0)
# fit(nu, x_2, linfit)

ratio_2 = 1.3278983520033001*10**(-5)

c_2 = speed(ratio_2)
print(c_2)

#3
x_0 = 8.5/1000 #m
sigma_x_0 = 0.5/1000 #m
nu = [float(0), 898.0, 856.0, 798.0, 740.0, 706.0, 655.0, 596.0, 542.0, 504.0, 457.0]
sigma_nu_3 = [float(0), 0.3, float(1), float(2), float(2), float(1), float(2), float(2), float(2), float(2), float(3)]
x = [8.5, 14.0, 13.75, 13.25, 13.0, 12.5, 12.25, 12.0, 11.75, 11.5, 11.0]
nu_3 = nu

for i in range(len(nu)):
    nu[i] = nu[i]/2
    sigma_nu_3[i] = sigma_nu_3[i]/2

for i in range(len(x)):
    x[i] = x[i]/1000

x_3 = x_vals(x, x_0)
# fit(nu, x_3, linfit)

ratio_3 = 1.2235869491303959*10**(-5)

c_3 = speed(ratio_3)
print(c_3)

sigma_x_1 = []
sigma_x_2 = []
sigma_x_3 = []

for i in range(len(x_1)):
    sigma_x_1.append(2**0.5*sigma_x_0)

for i in range(len(x_2)):
    sigma_x_2.append(2**0.5*sigma_x_0)

for i in range(len(x_3)):
    sigma_x_3.append(2**0.5*sigma_x_0)

# table(values=[x_1, nu_1], errors=[sigma_x_1, sigma_nu_1])
# table(values=[x_2, nu_2], errors=[sigma_x_2, sigma_nu_2])
# table(values=[x_3, nu_3], errors=[sigma_x_3, sigma_nu_3])

# fit_err(nu_1, x_1, sigma_nu_1, sigma_x_1, linfit)
# fit_err(nu_2, x_2, sigma_nu_2, sigma_x_2, linfit)
# fit_err(nu_3, x_3, sigma_nu_3, sigma_x_3, linfit)

c = [c_1, c_2, c_3]

statistics(c)
from fit import fit
import numpy as np
import matplotlib.pyplot as plt
from table import table
from scipy.special import erf

def linfit(x,A,B):
    return A*x+B

def quandraticfit(x,A,B,C):
    return A*x**2+B*x+C

def gaussian(x, A, mu, sigma):
    return A * np.exp(-((x+2500 - mu) ** 2) / (2 * sigma ** 2))

# x_1 = []
# x_2 = []
# d_1 = []
# d_2 = []

# deltaX = []
# deltaD = []

# for i in range(len(x_1)):
#     deltaX.append(abs(x_1[i]-x_2[i]))
#     deltaD.append(abs(d_1[i]-d_2[i]))

# fit(deltaX, deltaD, linfit)
# fit(deltaX, deltaD, quandraticfit)

x = [2, 10, 102, 150, 243.5]
d_fotak = [1.5, 2, 2.5, 3, 5]
d_oko = [1,2,3,4,6]

def txt_2_graph(file_path):

    X = []
    Y = []
    
    with open(file_path, "r") as file:
        for line in file:
            values = line.split()  # Splits by whitespace (tab or space)
            X.append(float(values[0].replace(',', '.')))  # Convert to float
            Y.append(float(values[1].replace(',', '.')))  # Convert to float

    plt.plot(X, Y, color="orange", marker='o', markersize=1, label="", linestyle="-")
    plt.xlabel(r'X [$\mu$m]')
    plt.ylabel(r'X values [%]')
    plt.legend()
    plt.grid(False)
    plt.show()

    fit(X,Y,gaussian)

file_paths = ["./Data_XX/Data_102cm_#001.txt",  "./Data_XX/Data_10cm_#001.txt" ,   "./Data_XX/Data_150cm_#001.txt" , "./Data_XX/Data_2435cm_#001.txt" , "./Data_XX/Data_2cm_#001.txt"]

for i in range(len(file_paths)):
    txt_2_graph(file_paths[i])


print("")
fit(x, d_oko, linfit)
fit(x, d_fotak, linfit)
fit(x_data=[102, 150, 243.5, 10, 2], y_data=[0.3741359714209133*4, 0.5222841525924692*4, 0.8260486971687681*4, 163.21541437472246*4/1000, 160.18234664699318*4/1000], custom_function=linfit)
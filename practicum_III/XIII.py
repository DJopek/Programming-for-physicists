import numpy as np
import matplotlib.pyplot as plt
from fit import fit
from average import statistics
from table import table
from table import table_justvalues

def txt_2_graph(file_path):

    X = []
    Y = []
    
    with open(file_path, "r") as file:
        for line in file:
            values = line.split()
            X.append(float(values[0].replace(',', '.')))
            Y.append(float(values[1].replace(',', '.')))

    plt.plot(X, Y, color="orange", marker='o', markersize=1, label="", linestyle="-")
    plt.xlabel(r'2$\vartheta$ [deg]')
    plt.ylabel(r'R [Imp/s]')
    plt.legend()
    plt.grid(False)
    plt.show()


def txt_2_data(file_path):

    X = []
    Y = []
    
    with open(file_path, "r") as file:
        for line in file:
            values = line.split()
            X.append(float(values[0].replace(',', '.')))
            Y.append(float(values[1].replace(',', '.')))
    return X, Y

def linfit(x,k,q):
    return k*x+q

# txt_2_graph(file_path="./data_XIII/05s")
# txt_2_graph(file_path="./data_XIII/1s")
# txt_2_graph(file_path="./data_XIII/2s")
# txt_2_graph(file_path="./data_XIII/4s")
# # txt_2_graph(file_path="./data_XIII/05s2")
# # txt_2_graph(file_path="./data_XIII/1s2")
# # txt_2_graph(file_path="./data_XIII/2s2")
# # txt_2_graph(file_path="./data_XIII/2s2")
# txt_2_graph(file_path="./data_XIII/14")
# txt_2_graph(file_path="./data_XIII/16")
# txt_2_graph(file_path="./data_XIII/18")
# txt_2_graph(file_path="./data_XIII/20")
# txt_2_graph(file_path="./data_XIII/22")
# txt_2_graph(file_path="./data_XIII/14kV")
# txt_2_graph(file_path="./data_XIII/16kV")
# txt_2_graph(file_path="./data_XIII/18kV")
# txt_2_graph(file_path="./data_XIII/20kV")
# txt_2_graph(file_path="./data_XIII/22kV")



# def data_fit(a,b,file_path):
#     X,Y = txt_2_data(file_path=file_path)
#     X_fit = []
#     Y_fit = []
#     for i in range(len(X)):
#         if b>= X[i] >= a:
#             X_fit.append(X[i])
#             Y_fit.append(Y[i])

#     fit(X_fit,Y_fit,linfit)

# # data_fit(25, 27, file_path="./data_XIII/14")
# # data_fit(21, 23, file_path="./data_XIII/16")
# # data_fit(20, 22, file_path="./data_XIII/18")
# # data_fit(17, 19, file_path="./data_XIII/20")
# # data_fit(16, 18, file_path="./data_XIII/22")

# data_fit(25, 30, file_path="./data_XIII/14kV")
# data_fit(21, 25, file_path="./data_XIII/16kV")
# data_fit(18, 20, file_path="./data_XIII/18kV")
# data_fit(17, 20, file_path="./data_XIII/20kV")
# data_fit(15, 20, file_path="./data_XIII/22kV")


k = [7.335164861695176, 14.11316045470843, 17.857143358345137, 25.744047429257797, 24.607364352274665]
q = [-173.0659347749325, -291.0615589787832, -324.9523904752367, -416.714282184195, -346.59263287424744]
theta = []

for i in range(len(k)):
    theta.append(-q[i]/(2*k[i]))

h = []
e = 1.602*10**(-19)
U = [14, 16, 18, 20, 22]
c = 299792458
d = 2.023*10**(-10)

for i in range(len(theta)):
    h.append(e*U[i]*1000*2*d*np.sin(theta[i]*2*3.1415/360)/c)

print(h)
statistics(h)

k = [7.335164861695176,  14.11316045470843, 17.857143358345137, 25.744047429257797, 24.607364352274665]
sigma_k = [1.5885117380654217, 1.3274033639764293, 3.3604339395787046, 3.6226891187518, 2.022192334050084]
q = [-173.0659347749325, -291.0615589787832, -324.9523904752367, -416.714282184195, -346.59263287424744]
sigma_q = [43.907337787694566, 30.55407499024374, 63.889500506211085, 67.46377077109213, 35.704284413454]


sigma_theta = []

for i in range(len(k)):
    sigma_theta.append(
        (
            (sigma_q[i]/(2*k[i]))**2
            +(q[i]*sigma_k[i]/(2*k[i]**2))**2
        )**0.5
    )

sigma_h = []

for i in range(len(h)):
    sigma_h.append(
        e*U[i]*1000*2*np.cos(theta[i]*2*3.1415/360)*sigma_theta[i]/c
    )

print(sigma_h)

# table(values=[k, q, theta, h], errors=[sigma_k, sigma_q, sigma_theta, sigma_h])
table_justvalues(values=[k, sigma_k, q, sigma_q, theta, sigma_theta, h])

X, Y = txt_2_data(file_path="./data_XIII/14")

max_Y = max(Y)

for i in range(len(Y)):
    if Y[i] == max_Y:
        index = i
        max_X = X[i]

sigma_theta = 0.01745277778

print("max:")
# print(max_X)
# print(max_Y)
print(2*d*np.sin(2*3.1415*max_X/(720)))
lambda_1 = 2*d*np.sin(2*3.1415*max_X/(720))
sigma_l_1 = 2*d*np.cos(2*3.1415*max_X/(720))*sigma_theta
print("s_l_1")
print(sigma_l_1)

X_2 = []
Y_2 = []

for i in range(len(Y)):
    if X[i] <= 41 :
        X_2.append(X[i])
        Y_2.append(Y[i])


max_Y = max(Y_2)

for i in range(len(Y_2)):
    if Y_2[i] == max_Y:
        index = i
        max_X = X_2[i]

print("max:")
# print(max_X)
# print(max_Y)

print(2*d*np.sin(2*3.1415*max_X/720))
lambda_2 = 2*d*np.sin(2*3.1415*max_X/(720))
sigma_l_2 = 2*d*np.cos(2*3.1415*max_X/(720))*sigma_theta
print("s_l_2")
print(sigma_l_2)


h = 6.62607015*10**(-34)

E_1 = h*c/lambda_1
E_2 = h*c/lambda_2

sigma_E_1 = sigma_l_1 *h*c/lambda_1**2
sigma_E_2 = sigma_l_2 *h*c/lambda_2**2

print(E_1/(1.602177*10**(-16)))
print(sigma_E_1/(1.602177*10**(-16)))
print(E_2/(1.602177*10**(-16)))
print(sigma_E_2/(1.602177*10**(-16)))

R = 10973731.568157

print(((1/lambda_1 * 1/R * 4/3)**0.5 - 29 )*(-1))
print(((1/lambda_2 * 1/R * 9/8)**0.5 - 29 )*(-1))

print(((sigma_l_1/lambda_1**2 * 1/R * 4/3)**0.5 - 29 )*(-1))


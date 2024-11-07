import numpy as np
import matplotlib.pyplot as plt

def fit(data, x):
    data = np.array(data)
    x = np.array(x)

    # Perform linear regression
    slope, intercept = np.polyfit(x, data, 1)

    # Predicted values using the linear model
    predicted = slope * x + intercept

    # Plotting the data and the linear fit
    plt.scatter(x, data, marker='^', s=100, label='')
    plt.errorbar(x, data, fmt='^', capsize=7)
    plt.plot(x, predicted, color='orange', linestyle=':', label='')
    plt.xlabel('C [μF]')
    plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
    # plt.title('')
    # plt.legend()
    plt.grid(False)
    plt.show()

    print("Slope:", slope)
    print("Intercept:", intercept)


    # This is for errors of the fit
    model,V=np.polyfit(x,data,1,cov=True)
    y_fit=np.polyval(model,x)
    fig,ax=plt.subplots()
    # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    # ax.plot(x,y_fit,c="red")
    ax.set_xlabel("x", fontsize=15)
    ax.set_ylabel("y", fontsize=15)
    # plt.show()

    print("y=ax+b")
    print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    print("cov(a,b) = ",V[0,1])
    print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

    return model[0], np.sqrt(V[0,0]), model[1], np.sqrt(V[1,1])

def fit_2(data_1, data_2, x):
    
    x = np.array(x)

    # Perform linear regression
    slope, intercept = np.polyfit(x, data_1, 1)

    # Predicted values using the linear model
    predicted = slope * x + intercept

    # Plotting the data and the linear fit
    # plt.scatter(x, data_1, marker='o', s=10, label='')
    # plt.errorbar(x, data_1, fmt='o', capsize=7)
    plt.plot(x, predicted, color='orange', linestyle=':', label='teoretická predikcia')
    plt.xlabel('C []')
    # plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
    plt.ylabel('')
    # plt.title('')
    # plt.legend()
    plt.grid(False)

    print("Slope:", slope)
    print("Intercept:", intercept)

    # Perform linear regression
    slope, intercept = np.polyfit(x, data_2, 1)

    # Predicted values using the linear model
    predicted = slope * x + intercept

    # Plotting the data and the linear fit
    plt.scatter(x, data_2, marker='o', s=10, label='namerané hodnoty')
    plt.errorbar(x, data_2, fmt='o', capsize=7)
    plt.plot(x, predicted, color='orange', linestyle='-', label='')
    plt.xlabel('C [μF]')
    # plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
    plt.ylabel('τ [s]')
    # plt.title('')
    plt.legend()
    plt.grid(False)
    plt.show()

    print("Slope:", slope)
    print("Intercept:", intercept)


    # This is for errors of the fit
    model,V=np.polyfit(x,data_1,1,cov=True)
    y_fit=np.polyval(model,x)
    fig,ax=plt.subplots()
    # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    # ax.plot(x,y_fit,c="red")
    ax.set_xlabel("x", fontsize=15)
    ax.set_ylabel("y", fontsize=15)
    # plt.show()

    print("y=ax+b")
    print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    print("cov(a,b) = ",V[0,1])
    print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

    # return model[0], np.sqrt(V[0,0]), model[1], np.sqrt(V[1,1])


    # This is for errors of the fit
    model,V=np.polyfit(x,data_2,1,cov=True)
    y_fit=np.polyval(model,x)
    fig,ax=plt.subplots()
    # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    # ax.plot(x,y_fit,c="red")
    ax.set_xlabel("x", fontsize=15)
    ax.set_ylabel("y", fontsize=15)
    # plt.show()

    print("y=ax+b")
    print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    print("cov(a,b) = ",V[0,1])
    print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

    # return model[0], np.sqrt(V[0,0]), model[1], np.sqrt(V[1,1])
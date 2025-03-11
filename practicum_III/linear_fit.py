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
    plt.xlabel("U[V]")
    plt.ylabel("ln(I)[ln(A)]")
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

def fit_4(data_1, data_2, data_3, data_4, x_1, x_2, x_3, x_4):
    
    # x = np.array(x_1)

    # # Perform linear regression
    # slope, intercept = np.polyfit(x, data_1, 1)

    # # Predicted values using the linear model
    # predicted = slope * x + intercept

    # # Plotting the data and the linear fit
    # plt.scatter(x, data_1, marker='o', s=10, label='')
    # # plt.errorbar(x, data_1, fmt='o', capsize=7)
    # plt.plot(x, predicted, color='orange', linestyle=':', label='')
    # plt.xlabel('')
    # # plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
    # plt.ylabel('')
    # # plt.title('')
    # # plt.legend()
    # plt.grid(False)

    # # print("Slope:", slope)
    # # print("Intercept:", intercept)

    # x = np.array(x_2)

    # # Perform linear regression
    # slope, intercept = np.polyfit(x, data_2, 1)

    # # Predicted values using the linear model
    # predicted = slope * x + intercept

    # # Plotting the data and the linear fit
    # plt.scatter(x, data_2, marker='o', s=10, label='')
    # # plt.errorbar(x, data_2, fmt='o', capsize=7)
    # plt.plot(x, predicted, color='red', linestyle=':', label='')
    # plt.xlabel('C [μF]')
    # # plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
    # plt.ylabel(' [s]')
    # # plt.title('')
    # plt.legend()
    # plt.grid(False)

    # # print("Slope:", slope)
    # # print("Intercept:", intercept)

    # x = np.array(x_3)

    # # Perform linear regression
    # slope, intercept = np.polyfit(x, data_3, 1)

    # # Predicted values using the linear model
    # predicted = slope * x + intercept

    # # Plotting the data and the linear fit
    # plt.scatter(x, data_3, marker='o', s=10, label='')
    # # plt.errorbar(x, data_1, fmt='o', capsize=7)
    # plt.plot(x, predicted, color='green', linestyle=':', label='')
    # plt.xlabel('')
    # # plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
    # plt.ylabel('')
    # # plt.title('')
    # # plt.legend()
    # plt.grid(False)

    # # print("Slope:", slope)
    # # print("Intercept:", intercept)

    # x = np.array(x_4)

    # # Perform linear regression
    # slope, intercept = np.polyfit(x, data_4, 1)

    # # Predicted values using the linear model
    # predicted = slope * x + intercept

    # # Plotting the data and the linear fit
    # plt.scatter(x, data_4, marker='o', s=10, label='')
    # # plt.errorbar(x, data_1, fmt='o', capsize=7)
    # plt.plot(x, predicted, color='blue', linestyle=':', label='')
    # plt.xlabel('')
    # # plt.ylabel(r'$\frac{1}{\omega_r^2}\ [s^{2}]$')
    # plt.ylabel('')
    # # plt.title('')
    # # plt.legend()
    # plt.grid(False)
    # plt.show()

    # # print("Slope:", slope)
    # # print("Intercept:", intercept)


    # # This is for errors of the fit
    # model,V=np.polyfit(x_1,data_1,1,cov=True)
    # y_fit=np.polyval(model,x_1)
    # fig,ax=plt.subplots()
    # # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    # # ax.plot(x,y_fit,c="red")
    # ax.set_xlabel("x", fontsize=15)
    # ax.set_ylabel("y", fontsize=15)
    # # plt.show()

    # a = []
    # sigma_a = []

    # print("y=ax+b")
    # print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    # print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    # print("cov(a,b) = ",V[0,1])
    # print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))
    # a.append(model[0])
    # sigma_a.append(np.sqrt(V[0,0]))
    # # return model[0], np.sqrt(V[0,0]), model[1], np.sqrt(V[1,1])


    # # This is for errors of the fit
    # model,V=np.polyfit(x_2,data_2,1,cov=True)
    # y_fit=np.polyval(model,x_2)
    # fig,ax=plt.subplots()
    # # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    # # ax.plot(x,y_fit,c="red")
    # ax.set_xlabel("x", fontsize=15)
    # ax.set_ylabel("y", fontsize=15)
    # # plt.show()

    # print("y=ax+b")
    # print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    # print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    # print("cov(a,b) = ",V[0,1])
    # print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))
    # a.append(model[0])
    # sigma_a.append(np.sqrt(V[0,0]))

    # # return model[0], np.sqrt(V[0,0]), model[1], np.sqrt(V[1,1])

    #     # This is for errors of the fit
    # model,V=np.polyfit(x_3,data_3,1,cov=True)
    # y_fit=np.polyval(model,x_3)
    # fig,ax=plt.subplots()
    # # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    # # ax.plot(x,y_fit,c="red")
    # ax.set_xlabel("x", fontsize=15)
    # ax.set_ylabel("y", fontsize=15)
    # # plt.show()

    # print("y=ax+b")
    # print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    # print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    # print("cov(a,b) = ",V[0,1])
    # print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))
    # a.append(model[0])
    # sigma_a.append(np.sqrt(V[0,0]))

    # # return model[0], np.sqrt(V[0,0]), model[1], np.sqrt(V[1,1])

    #     # This is for errors of the fit
    # model,V=np.polyfit(x_4,data_4,1,cov=True)
    # y_fit=np.polyval(model,x_4)
    # fig,ax=plt.subplots()
    # # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    # # ax.plot(x,y_fit,c="red")
    # ax.set_xlabel("x", fontsize=15)
    # ax.set_ylabel("y", fontsize=15)
    # # plt.show()

    # print("y=ax+b")
    # print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    # print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    # print("cov(a,b) = ",V[0,1])
    # print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))
    # a.append(model[0])
    # sigma_a.append(np.sqrt(V[0,0]))

    # return(a, sigma_a)
    
    colors = ['orange', 'red', 'green', 'blue']
    data_list = [data_1, data_2, data_3, data_4]
    x_list = [x_1, x_2, x_3, x_4]
    custom_labels = ['N=10, r=12.5cm', 'N=5, r=12.5cm', 'N=10, r=19.5cm', 'N=5, r=19.5cm']
    a = []
    sigma_a = []
    
    for i, (data, x, color, label) in enumerate(zip(data_list, x_list, colors, custom_labels)):
        x = np.array(x)
        
        slope, intercept = np.polyfit(x, data, 1)
        predicted = slope * x + intercept

        plt.scatter(x, data, marker='o', s=10, label=f'{label}')
        plt.plot(x, predicted, color=color, linestyle=':', label=f' ')
        
        # print(f"{label} - Slope:", slope)
        # print(f"{label} - Intercept:", intercept)
    
    plt.ylabel(r'$\alpha$[rad]')
    plt.xlabel('I[A]')
    plt.legend()
    plt.grid(False)
    plt.show()
    
    # Error calculations
    for i, (data, x) in enumerate(zip(data_list, x_list)):
        model, V = np.polyfit(x, data, 1, cov=True)
        y_fit = np.polyval(model, x)

        print(f"Data {i+1} - Fit with Errors")
        # print("y=ax+b")
        print("a = ", model[0], "+/-", np.sqrt(V[0, 0]))
        print("b = ", model[1], "+/-", np.sqrt(V[1, 1]))
        # print("cov(a,b) = ", V[0, 1])
        # print("corr(a,b) = ", V[0, 1] / (np.sqrt(V[0, 0] * V[1, 1])))
        a.append(model[0])
        sigma_a.append(np.sqrt(V[0,0]))

    return(a, sigma_a)

def fit_n(data_list, x_list, colors, labels, x_label, y_label):
    
    a = []
    sigma_a = []
    b = []
    sigma_b = []

    for i, (data, x, color, label) in enumerate(zip(data_list, x_list, colors, labels)):

        x = np.array(x)
        
        slope, intercept = np.polyfit(x, data, 1)
        predicted = slope * x + intercept

        plt.scatter(x, data, marker='o', s=10, label=f'{label}')
        plt.plot(x, predicted, color=color, linestyle=':', label=f'fit')
        
        # print(f"{label} - Slope:", slope)
        # print(f"{label} - Intercept:", intercept)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(False)
    plt.show()
    
    # Error calculations
    for i, (data, x) in enumerate(zip(data_list, x_list)):
        model, V = np.polyfit(x, data, 1, cov=True)
        y_fit = np.polyval(model, x)

        print(f"Data {i+1} - Fit with Errors")
        # print("y=ax+b")
        print("a = ", model[0], "+/-", np.sqrt(V[0, 0]))
        print("b = ", model[1], "+/-", np.sqrt(V[1, 1]))
        # print("cov(a,b) = ", V[0, 1])
        # print("corr(a,b) = ", V[0, 1] / (np.sqrt(V[0, 0] * V[1, 1])))
        a.append(model[0])
        sigma_a.append(np.sqrt(V[0,0]))
        b.append(model[1])
        sigma_b.append(np.sqrt(V[1,1]))

    return(a, sigma_a, b, sigma_b)
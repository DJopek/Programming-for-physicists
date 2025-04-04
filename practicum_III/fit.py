import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit(x_data, y_data, custom_function):

    params, covariance = curve_fit(custom_function, x_data, y_data)

    fitted_params = params

    errors = np.sqrt(np.diag(covariance))

    for i, (param, error) in enumerate(zip(fitted_params, errors)):
        print(f"Fitted parameter {i}: {param} ± {error}")

    plt.scatter(x_data, y_data, marker='o', s=10, label='hodnoty')
    # plt.errorbar(x_data, y_data, fmt='o', capsize=7)

    x = np.linspace(np.min(x_data), np.max(x_data), 100)
    # x = np.linspace(0, np.max(x_data), 100)

    plt.plot(x, custom_function(x, *fitted_params), color='orange', linestyle=':', label='fit')
    plt.xlabel(r'$\Delta X$ [cm]')
    plt.ylabel(r'D [mm]')
    plt.legend()
    plt.show()

def fit_multi(x_data, y_data, x_data_2, y_data_2, custom_function):

    params, covariance = curve_fit(custom_function, x_data, y_data)

    fitted_params = params

    errors = np.sqrt(np.diag(covariance))

    for i, (param, error) in enumerate(zip(fitted_params, errors)):
        print(f"Fitted parameter {i}: {param} ± {error}")

    plt.scatter(x_data, y_data, marker='o', s=5, label='namerané hodnoty', color='red')
    plt.errorbar(x_data, y_data, fmt='o', capsize=7, color='red')

    x = np.linspace(np.min(x_data), np.max(x_data), 100)

    plt.plot(x, custom_function(x, *fitted_params), color='red', linestyle=':', label='fit pre P')

    params, covariance = curve_fit(custom_function, x_data_2, y_data_2)

    fitted_params = params

    errors = np.sqrt(np.diag(covariance))

    for i, (param, error) in enumerate(zip(fitted_params, errors)):
        print(f"Fitted parameter {i}: {param} ± {error}")

    plt.scatter(x_data_2, y_data_2, marker='o', s=5, label='namerané hodnoty', color='green')
    plt.errorbar(x_data_2, y_data_2, fmt='o', capsize=7, color='green')

    x = np.linspace(np.min(x_data_2), np.max(x_data_2), 100)

    plt.plot(x, custom_function(x, *fitted_params), color='green', linestyle=':', label='fit pre I')
    plt.ylabel(r'$P$ [W]')
    # plt.ylabel('T [s]')
    plt.xlabel(r'$U$ [V]')

    plt.legend()
    plt.show()

def fit_dx(x_data, y_data, custom_function, derivation):

    params, covariance = curve_fit(custom_function, x_data, y_data)

    fitted_params = params

    errors = np.sqrt(np.diag(covariance))

    for i, (param, error) in enumerate(zip(fitted_params, errors)):
        print(f"Fitted parameter {i}: {param} ± {error}")

    # plt.scatter(x_data, y_data, marker='o', s=10, label='namerané hodnoty')
    # plt.errorbar(x_data, y_data, fmt='o', capsize=7)

    x = np.linspace(np.min(x_data), np.max(x_data), 100)

    def const(x):
        return 0*x

    # plt.plot(x, custom_function(x, *fitted_params), color='orange', linestyle=':', label='fit')
    plt.plot(x , derivation(x, *fitted_params), color='blue', linestyle=':', label='derivácia')
    print("")
    print("")
    print("")
    # print(derivation(x, *fitted_params))
    # print(x)
    # print(np.where(np.isclose(derivation(x, *fitted_params), 4.07515644e-03)))
    # print(x[np.where(np.isclose(derivation(x, *fitted_params), 4.07515644e-03))])
    # print(custom_function(0.35836364, *fitted_params))
    print("")
    print("")
    print("")
    plt.plot(x, const(x), color='red', linestyle=':')
    plt.ylabel(r'$P$ [W]')
    # plt.ylabel('T [s]')
    plt.xlabel(r'$U$ [V]')
    plt.legend()
    plt.show()
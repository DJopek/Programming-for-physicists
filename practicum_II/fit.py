import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit(x_data, y_data, custom_function):

    params, covariance = curve_fit(custom_function, x_data, y_data)

    fitted_params = params

    errors = np.sqrt(np.diag(covariance))

    for i, (param, error) in enumerate(zip(fitted_params, errors)):
        print(f"Fitted parameter {i}: {param} ± {error}")

    plt.scatter(x_data, y_data, marker='o', s=10, label='namerané hodnoty')
    plt.errorbar(x_data, y_data, fmt='o', capsize=7)

    x = np.linspace(np.min(x_data), np.max(x_data), 100)

    plt.plot(x, custom_function(x, *fitted_params), color='orange', linestyle=':', label='fit')
    plt.xlabel(r'$U_{BE}$ [V]')
    # plt.ylabel('T [s]')
    plt.ylabel(r'$I_{B}$ [mA]')
    plt.legend()
    plt.show()
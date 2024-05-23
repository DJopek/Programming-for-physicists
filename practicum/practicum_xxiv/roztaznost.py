import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

l_0  = 600

data_ocel = [0,1,5,9,13,16,20,23]
teplota_ocel = [28,30,35,40,45,50,55,60]

data_med = [0,6,11,16,22,27,30,31]
teplota_med = [25,30,35,40,45,50,55,60]

data_Al = [0,5,12,12.5,24,30,31,31]
teplota_Al = [27,30,35,40,45,50,55,60]

data_mosadz = [0,5,12,17,24,27,28,28]
teplota_mosadz = [26,30,35,40,45,50,55,60]

error_data_x = [1,1,1,1,1,1,1,1]
error_data_y = [0,0,0,0,0,0,0,0]


def  fit(x, data, error_data_x, error_data_y):

    # Linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, data)

    # Predicted values
    predicted = slope * x + intercept


    plt.errorbar(x, data, yerr=error_data_y, xerr=error_data_x, fmt='o', elinewidth=2)
    plt.plot(x, predicted, color='red')
    # plt.plot(x, predicted_2)
    plt.ylabel('Δl [10⁻² mm]')
    plt.xlabel('T [°C]')
    plt.title('Závislosť predĺženia od teploty')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Slope:", slope)
    print("Intercept:", intercept)

    model,V=np.polyfit(x,data,1,cov=True)
    y_fit=np.polyval(model,x)
    fig,ax=plt.subplots()
    # ax.errorbar(x,data,error_data,marker="o",linewidth=0,elinewidth=2,capsize=5)
    ax.plot(x,y_fit,c="red")
    ax.set_xlabel("x", fontsize=15)
    ax.set_ylabel("y", fontsize=15)
    plt.show()

    print("y=ax+b")
    print("a = ",model[0], "+/-", np.sqrt(V[0,0]))
    print("b = ",model[1], "+/-", np.sqrt(V[1,1]))
    print("cov(a,b) = ",V[0,1])
    print("corr(a,b) = ",V[0,1]/(np.sqrt(V[0,0]*V[1,1])))

    return model[0], np.sqrt(V[0,0])


A_ocel, sigma_ocel = fit(np.array(teplota_ocel), np.array(data_ocel), np.array(error_data_x), np.array(error_data_y))
A_med, sigma_med = fit(np.array(teplota_med), np.array(data_med), np.array(error_data_x), np.array(error_data_y))
A_Al, sigma_Al = fit(np.array(teplota_Al), np.array(data_Al), np.array(error_data_x), np.array(error_data_y))
A_mosadz, sigma_mosadz = fit(np.array(teplota_mosadz), np.array(data_mosadz), np.array(error_data_x), np.array(error_data_y))

def chyba(sigma_A, sigma_deltal, l_0, A):
    return ((sigma_A/(l_0))**2 + (A/(l_0**2) * sigma_deltal)**2)**0.5

s_ocel = chyba(sigma_ocel, 0.5, 600, A_ocel)
s_med = chyba(sigma_med, 0.5, 600, A_med)
s_hlinik = chyba(sigma_Al, 0.5, 600, A_Al)
s_mosadz = chyba(sigma_mosadz, 0.5, 600, A_mosadz)

print("alfa_ocel")
print(A_ocel/(100*l_0))
print("chyba_ocel")
print(s_ocel)
print("alfa_med")
print(A_med/(100*l_0))
print("chyba_med")
print(s_med)
print("alfa_Al")
print(A_Al/(100*l_0))
print("chyba_Al")
print(s_hlinik)
print("alfa_mosadz")
print(A_mosadz/(100*l_0))
print("chyba_mosadz")
print(s_mosadz)

#vidime, že niektore hodnoty vyzeraju, ze nesplnaju linearny vztah, tak ich skusime vylucit
data_Al = [0,5,12,24,30]
teplota_Al = [27,30,40,45,50]

A_Al, sigma_Al = fit(np.array(teplota_Al), np.array(data_Al), error_data_x = np.array([1,1,1,1,1]), error_data_y=np.array([0,0,0,0,0]))
s_Al = chyba(sigma_Al, 0.5, 600, A_Al)

print("Al better")
print(A_Al/(100*l_0))
print(s_Al)


# dame prec tie, kedy sa hodnota neposunula, co je nefyzikalne spravanie, taky udaj pre nas nema zmysel, je asi zatazeny hrubou chybou, preto ho vylucime
data_mosadz = [0,5,12,17,24,27]
teplota_mosadz = [26,30,35,40,45,50]

A_mosadz, sigma_mosadz = fit(np.array(teplota_mosadz), np.array(data_mosadz), np.array([1,1,1,1,1,1]), np.array([0,0,0,0,0,0]))
s_mosadz = chyba(sigma_mosadz, 0.5, 600, A_mosadz)

print("Mosadz better")
print(A_mosadz/(100*l_0))
print(s_mosadz)

# podobne posledny udaj pre med
data_med = [0,6,11,16,22,27,30]
teplota_med = [25,30,35,40,45,50,55]

A_med, sigma_med = fit(np.array(teplota_med), np.array(data_med), np.array([1,1,1,1,1,1,1]), np.array([0,0,0,0,0,0, 0]))
s_med = chyba(sigma_med, 0.5, 600, A_med)

print(A_med)
print(sigma_med)

print("med better")
print(A_med/(100*l_0))
print(s_med)
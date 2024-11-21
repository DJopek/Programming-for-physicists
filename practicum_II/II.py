import matplotlib.pyplot as plt
import numpy as np

vnutorny_odpor_A = [110.3,110.3,82.9,82.9,11.4,11.4,4.7,4.7, 40.1, 40.1, 21.8, 21.8]
vnutorny_odpor_V = [0.75*1000,0.75*1000,0.75*1000,0.75*1000, 15*1000, 15*1000, 37.5*1000, 37.5*1000, 0.75*1000, 0.75*1000, 3.75*1000, 3.75*1000]

rozsah_A_a = [1.5,1.5,3,3,30,30,75,75, 7.5, 7.5, 15, 15]
rozsah_V_a = [1.5,1.5,1.5,1.5,75,75,75,75, 3, 3, 7.5, 7.5]
dieliky_A_a = [20,35,50,100,130,141,66,71, 110, 120, 110, 134]
dieliky_V_a = [4,8,20,40,40,50,60,68, 48, 54, 77, 114]
A_a = []
V_a = []
R_a = []
R_a_correct = []

rozsah_A_b = [1.5, 1.5, 3,3, 30, 30, 75, 75, 7.5, 7.5, 15, 15]
rozsah_V_b = [1.5,1.5,1.5,1.5,30,30,75,75, 1.5, 1.5, 3, 3]
dieliky_A_b = [40,100,90,110,110,120,70,78, 101, 120, 88, 110]
dieliky_V_b = [4,10,19,23,75,82,66,80, 54, 66, 71, 114]
A_b = []
V_b = []
R_b = []
R_b_correct = []
I_r = []


def valuesAV(rozsah_A, rozsah_V, dieliky_A, dieliky_V, A, V):
    for i in range(len(dieliky_A)):
        A.append(rozsah_A[i]*dieliky_A[i]/150)
    for i in range(len(dieliky_V)):
        V.append(rozsah_V[i]*dieliky_V[i]/150)

    # print(A)
    # print(V)

valuesAV(rozsah_A_a, rozsah_V_a, dieliky_A_a, dieliky_V_a, A_a, V_a)
valuesAV(rozsah_A_b, rozsah_V_b, dieliky_A_b, dieliky_V_b, A_b, V_b)

print("A_a: ")
print(A_a)
print("")
print("")

print("V_a: ")
print(V_a)
print("")
print("")

print("A_b: ")
print(A_b)
print("")
print("")

print("V_b: ")
print(V_b)
print("")
print("")

for i in range(len(A_a)):
    R_a.append(V_a[i]/(A_a[i]/1000))
for i in range(len(A_a)):
    R_a_correct.append(R_a[i]-vnutorny_odpor_A[i])

for i in range(len(A_b)):
    R_b.append(V_b[i]*vnutorny_odpor_V[i]/((A_b[i]/1000)*vnutorny_odpor_V[i]-V_b[i]))
    I_r.append((A_b[i]/1000)-V_b[i]/vnutorny_odpor_V[i])
for i in range(len(A_b)):
    R_b_correct.append(V_b[i]*vnutorny_odpor_V[i]/((I_r[i])*vnutorny_odpor_V[i]-V_b[i]))

print("R_a: ")
print(R_a)
print("")
print("")

print("R_a_correct: ")
print(R_a_correct)
print("")
print("")

print("R_b: ")
print(R_b)
print("")
print("")

print("R_b_correct: ")
print(R_b_correct)
print("")
print("")

print("I_r: ")
print(I_r)
print("")
print("")


plt.scatter(A_a, R_a, color='orange', marker='o', s=25, label='Odpor')
plt.scatter(A_a, R_a_correct, color='blue', marker='o', s=25, label='Odpor s korekciou')

plt.ylabel('R[Ω]')
plt.xlabel('I[mA]')
plt.title('')

# Show the legend
plt.legend()

plt.show()


plt.scatter(I_r, R_b, color='orange', marker='o', s=25, label='Odpor')
plt.scatter(I_r, R_b_correct, color='blue', marker='o', s=25, label='Odpor s korekciou')

plt.ylabel('R[Ω]')
plt.xlabel('I[mA]')
plt.title('')

plt.legend()

plt.show()

rozsah_A = [1.5, 3, 7.5, 15, 30, 75]
dieliky_A = [106,100,99,100,110, 70]
R = [114, 116, 134, 293, 710, 940]
U = [0.02,0.03,0.08,3,15.2,34.1]
A = []
R_i = []

for i in range(len(rozsah_A)):
    A.append(rozsah_A[i]*dieliky_A[i]/150)
for i in range(len(A)):
    R_i.append(U[i]/(A[i]/1000))

plt.scatter(A, R, color='orange', marker='o', s=25, label='Odpor na dekáde')
plt.scatter(A, R_i, color='blue', marker='o', s=25, label='Vypočítaný odpor')

plt.ylabel('R[Ω]')
plt.xlabel('I[mA]')
plt.title('')

plt.legend()

plt.show()

#chyby
sigma_A_a = []
sigma_V_a = []
sigma_A_b = []
sigma_V_b = []
sigma_RA = []
sigma_RV = []
sigma_I_r = []
sigma_A_subst = []
sigma_U = []
sigma_R = []
sigma_R_i = []

def error(rozsah_A,rozsah_V, sigma_A, sigma_V):
    for i in range(len(rozsah_A)):
        sigma_A.append((3)**(-0.5)*rozsah_A[i]*0.2/100)
    for i in range(len(rozsah_V)):
        sigma_V.append((3)**(-0.5)*rozsah_V[i]*0.2/100)

for i in range(len(vnutorny_odpor_A)):
    sigma_RA.append((3)**(-0.5)*(vnutorny_odpor_A[i]*0.9/100+0.2))

for i in range(len(vnutorny_odpor_V)):
    sigma_RV.append((3)**(-0.5)*(vnutorny_odpor_V[i]*0.9/100+0.02))

error(rozsah_A_a, rozsah_V_a, sigma_A_a, sigma_V_a)
error(rozsah_A_b, rozsah_V_b, sigma_A_b, sigma_V_b)

for i in range(len(A_b)):
    sigma_I_r.append(np.sqrt(
        (sigma_A_b[i])**2
        + (-sigma_A_b[i]/vnutorny_odpor_V[i])**2
        + (V_b[i]*vnutorny_odpor_V[i]/vnutorny_odpor_V[i]**2)**2
        )/1000
    )

sigma_R_a = []
sigma_R_a_correct = []

sigma_R_b = []
sigma_R_b_correct = []

for i in range(len(V_a)):
    sigma_R_a.append(np.sqrt(
        (sigma_V_a[i]/A_a[i])**2 
        + (-V_a[i]*sigma_A_a[i]/A_a[i]**2)**2
        )
    )
    sigma_R_a_correct.append(np.sqrt(
        (sigma_V_a[i]/A_a[i])**2 
        + (-V_a[i]*sigma_A_a[i]/A_a[i]**2)**2 
        + (-sigma_RA[i])**2
        )
    )

for i in range(len(V_b)):
    sigma_R_b.append(np.sqrt(
        (sigma_V_b[i]*(vnutorny_odpor_V[i]*(A_b[i]*vnutorny_odpor_V[i]-V_b[i])+V_b[i]*vnutorny_odpor_V[i])/(A_b[i]*vnutorny_odpor_V[i]-V_b[i])**2)**2
        + (-V_b[i]*vnutorny_odpor_V[i]**2*sigma_A_b[i]/(A_b[i]*vnutorny_odpor_V[i]-V_b[i])**2)**2
        + (sigma_RV[i]*(V_b[i]*(A_b[i]*vnutorny_odpor_V[i]-V_b[i])-V_b[i]*vnutorny_odpor_V[i]*A_b[i])/(A_b[i]*vnutorny_odpor_V[i]-V_b[i])**2)**2
        )

    )
    sigma_R_b_correct.append(np.sqrt(
        (sigma_V_b[i]*(vnutorny_odpor_V[i]*(I_r[i]*vnutorny_odpor_V[i]-V_b[i])+V_b[i]*vnutorny_odpor_V[i])/(I_r[i]*vnutorny_odpor_V[i]-V_b[i])**2)**2
        + (-V_b[i]*vnutorny_odpor_V[i]**2*sigma_I_r[i]/(I_r[i]*vnutorny_odpor_V[i]-V_b[i])**2)**2
        + (sigma_RV[i]*(V_b[i]*(I_r[i]*vnutorny_odpor_V[i]-V_b[i])-V_b[i]*vnutorny_odpor_V[i]*I_r[i])/(I_r[i]*vnutorny_odpor_V[i]-V_b[i])**2)**2
        )

    )

for i in range(len(A)):
    sigma_A_subst.append((3)**(-0.5)*rozsah_A[i]*0.2/100)
for i in range(len(U)):
    sigma_U.append(0.005*U[i])
for i in range(len(R)):
    sigma_R.append(0.01*R[i])
for i in range(len(A)):
    sigma_R_i.append(np.sqrt(
        (sigma_A_subst[i]/A[i]**2)**2
        + (sigma_U[i]/A[i])**2
        )
    )

print("sigma_I_r: ")
print(np.array(sigma_I_r))
print("")
print("")

print("sigma_A_a: ")
print(np.array(sigma_A_a))
print("")
print("")

print("sigma_V_a: ")
print(np.array(sigma_V_a))
print("")
print("")

print("sigma_A_b: ")
print(np.array(sigma_A_b))
print("")
print("")

print("sigma_V_b: ")
print(np.array(sigma_V_b))
print("")
print("")

print("sigma_RA: ")
print(np.array(sigma_RA))
print("")
print("")

print("sigma_RV: ")
print(np.array(sigma_RV))
print("")
print("")

print("sigma_R_a: ")
print(np.array(sigma_R_a))
print("")
print("")

print("sigma_R_a_correct: ")
print(np.array(sigma_R_a_correct))
print("")
print("")

print("sigma_R_b: ")
print(np.array(sigma_R_b))
print("")
print("")

print("sigma_R_b_correct: ")
print(np.array(sigma_R_b_correct))
print("")
print("")

print("SUBSTITUČNÁ METÓDA")

print("I: ")
print(A)
print("")
print("")

print("R_i")
print(R_i)
print("")
print("")

print("sigma_U")
print(sigma_U)
print("")
print("")

print("sigma_I")
print(sigma_A_subst)
print("")
print("")

print("sigma_R")
print(sigma_R)
print("")
print("")

print("sigma_R_i")
print(np.array(sigma_R_i))
print("")
print("")


plt.scatter(A_a, R_a, color='orange', marker='o', s=25, label='Odpor')
plt.errorbar(A_a, R_a, yerr=sigma_R_a , xerr=sigma_A_a , fmt='o', capsize=7, color="orange")

plt.scatter(A_a, R_a_correct, color='blue', marker='o', s=25, label='Odpor s korekciou')
plt.errorbar(A_a, R_a_correct, yerr=sigma_R_a_correct, xerr=sigma_A_a, fmt='o', capsize=7, color="blue")


plt.ylabel('R[Ω]')
plt.xlabel('I[mA]')
plt.title('')

# Show the legend
plt.legend()

plt.show()


plt.scatter(I_r, R_b, color='orange', marker='o', s=25, label='Odpor')
plt.errorbar(I_r, R_b, yerr=sigma_R_b, xerr=sigma_I_r, fmt='o', capsize=7, color="orange")

plt.scatter(I_r, R_b_correct, color='blue', marker='o', s=25, label='Odpor s korekciou')
plt.errorbar(I_r, R_b_correct, yerr=sigma_R_b_correct, xerr=sigma_I_r, fmt='o', capsize=7, color="blue")


plt.ylabel('R[Ω]')
plt.xlabel('I[A]')
plt.title('')

plt.legend()

plt.show()


plt.scatter(A, R, color='orange', marker='o', s=25, label='Odpor na dekáde')
plt.errorbar(A, R, yerr=sigma_R, xerr=sigma_A_subst, fmt='o', capsize=7, color="orange")

plt.scatter(A, R_i, color='blue', marker='o', s=25, label='Vypočítaný odpor')
plt.errorbar(A, R_i, yerr=sigma_R_i, xerr=sigma_A_subst, fmt='o', capsize=7, color="blue")


plt.ylabel('R[Ω]')
plt.xlabel('I[mA]')
plt.title('')

plt.legend()

plt.show()


I_r = np.array(I_r)
I_r = I_r*1000

plt.scatter(A_a, R_a, color='orange', marker='o', s=25, label='Odpor z priamej metódy a)')
plt.errorbar(A_a, R_a, yerr=sigma_R_a , xerr=sigma_A_a , fmt='o', capsize=7, color="orange")

plt.scatter(A_a, R_a_correct, color='blue', marker='o', s=25, label='Odpor z priamej metódy a) - korekcia')
plt.errorbar(A_a, R_a_correct, yerr=sigma_R_a_correct, xerr=sigma_A_a, fmt='o', capsize=7, color="blue")

plt.scatter(I_r, R_b, color='black', marker='o', s=25, label='Odpor z priamej metódy b)')
plt.errorbar(I_r, R_b, yerr=sigma_R_b, xerr=sigma_I_r, fmt='o', capsize=7, color="black")

plt.scatter(I_r, R_b_correct, color='yellow', marker='o', s=25, label='Odpor z priamej metódy b) - korekcia')
plt.errorbar(I_r, R_b_correct, yerr=sigma_R_b_correct, xerr=sigma_I_r, fmt='o', capsize=7, color="yellow")


plt.scatter(A, R, color='red', marker='o', s=25, label='Odpor na dekáde')
plt.errorbar(A, R, yerr=sigma_R, xerr=sigma_A_subst, fmt='o', capsize=7, color="red")

plt.scatter(A, R_i, color='purple', marker='o', s=25, label='Vypočítaný odpor')
plt.errorbar(A, R_i, yerr=sigma_R_i, xerr=sigma_A_subst, fmt='o', capsize=7, color="purple")


plt.ylabel('R[Ω]')
plt.xlabel('I[mA]')
plt.title('')

plt.legend()

plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# cara1 = np.array([[[6, 6], [10, 5]],   [[6, 4], [5, 0]],
#                   [[4, 6], [5, 10]],   [[10,5], [6, 4]],
#                   [[4, 6], [0,  5]],   [[5,10], [6, 6]],
#                   [[4, 4], [0,  5]],   [[4, 4], [5, 0]]])

# # for usecka in cara1:
# #   plt.plot(usecka[:,0], usecka[:,1],'o-c')

# # plt.grid()
# # plt.axis('equal')
# # plt.show()

# points = []

# for matrix in cara1:
#     for row in matrix:
#         # print(row)
#         points.append(row.tolist())

#     # for column in matrix:
#     #     print(column)
#     #     points.append(column.tolist())

# # print(points)

# # for i in range(0,16):
# #     print(points[i])

# is_true = []

# for i in range(0, 16):
#     for j in range(0,16):
#         while i < j :
#             if points[i] == points[j]:
#                 is_true.append(True)
#                 break
#             else:
#                 break

# counter = 0
# for i in range(0, len(is_true)):
#     if is_true[i] == True :
#         counter += 1

# # print(len(is_true))
# # print(counter)

# if counter == 8 :
#     print("Je uzavrety")
# else:
#     print("Neni")

# print(is_true)
# is_true[2:] = [2,2]
# print(is_true)

# from math import sin, cos, pi

# def integral(m, p, q, a, b):
#     if m == 0:
#         return p * (cos(a) - cos(b)) + q * (sin(b) - sin(a))

#     return m * integral(m - 1, -q, p, a, b) + a ** m * (p * cos(a) - q * sin(a)) - b ** m * (p * cos(b) - q * sin(b))

# print(integral(6, 1, -2, 0, pi/2))


# import numpy as np

# def priprav_vzorky(n):
#   "Má připravit hodnoty v proměnné vzorky. Nějak nefunguje."
#   global vzorky
#   vzorky = np.cos( np.linspace(1, n, n) )

# def prumer():
#   "Vrátí průměr hodnot v proměnné vzorky."
#   return sum(vzorky)/len(vzorky)  


# priprav_vzorky(10)
# print(prumer())

# from math import ceil

# def egypt(p,q):
#     a = ceil(q/p)
#     print(a)
#     denom = a
    
#     while 1/q < 1/a :
#         p = p*a - q
#         # print("p: "+str(p))
#         if p == 0:
#             break
#         a = ceil(q/p)
#         # print("a: "+str(a))
#         denom *= a
#         print(denom)

# egypt(99,100)

n = int(input("Input an integer: "))

while n != 1:

    if n % 2 != 0 :
        n = 3*n + 1
        print(n)
    
    else :
        n = n/2
        print(n)

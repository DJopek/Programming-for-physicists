p = 19

a = 2

seed = 2

I = seed

for i in range (20):
    I = (I*a % p)
    print(str(i) + "number is: " + str(I))
    print (str(i) + "number is: " + str(I/p))
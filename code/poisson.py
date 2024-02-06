data = [26, 29, 20, 25, 21, 17, 31, 20, 22, 22, 17]
n = len(data)

# average
sum_average = 0

for i in range (len(data)):
    sum_average += data[i]

average = sum_average * 1/n

print("The average is: " + str(average))

# factorial

def factorial(k):

    f = 1

    for i in range (1, k+1):
        f *= i

    return f

k = 20

sum_p = 0

for i in range(k) :
    sum_p += ((average**i) * (1/2.71828182846)**(average))/factorial(i)
    print(sum_p)

print("The p is: " + str(sum_p))
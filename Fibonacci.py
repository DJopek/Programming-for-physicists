n = int(input("Input a number: "))

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
value = fibonacci(n)
print("n-th term of Fibonacci is: " + str(value))

for i in range(0,n):
    value = fibonacci(i)
    print(value)

def fibonacci_2(n):
    a_n_1 = [0,0]
    a_n = [1]

    for i in range (0, n):
        x = a_n_1[i] + a_n[i]
        a_n.append(x)
        a_n_1.append(x)
        print(x)

    print("n-th term of Fibb is: " + str(x))

fibonacci_2(n)
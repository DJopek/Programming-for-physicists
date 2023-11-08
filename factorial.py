n = int(input("Input a number: "))

f = 1

for i in range (1, n+1):
    f *= i

print("n! = " + str(f))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

value = factorial(n)
print("Value of n! is: " + str(value))
def factorial(k):

    f = 1

    for i in range (1, k+1):
        f *= i

    return f

def binomial(n,k):
    c = factorial(n)/(factorial(k)*factorial(n-k))
    return c

def binomial_p(n,k,p):
    p = binomial(n,k) * p**k * (1-p)**(n-k)
    return p

sum_p = 0

for i in range(8,11):
    sum_p += binomial_p(10,i,0.904)

print(sum_p)

print(binomial_p(6,1,0.002))
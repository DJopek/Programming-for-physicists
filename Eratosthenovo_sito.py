import time
import matplotlib.pyplot as plt

number = int(input("Input a whole number greater than 1: "))

primes = []

def first_prime_alg(number):

    start_time = time.time()

    assert number>1, "n must be greater than 1"

    for n in range (2, number):
        Prime = True
        for i in range (2, n):

            y = n%i

            if y == 0:
                Prime = False
                break
        if Prime:
            primes.append(n)
    
    end_time = time.time()

    t = end_time - start_time

    return t
    

t = first_prime_alg(number)

print(primes)

print(t)  




prime_num = []

def eratosthenes(number):

    start_time = time.time()


    is_prime = [True] * (number)

    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p < number**0.5:
        if is_prime[p]:
            for i in range (2, number):
                if i*p < number:
                    is_prime[i*p] = False
        p += 1

    for i in range (2, number):
        if is_prime[i]:
                prime_num.append(i)

    end_time = time.time()

    t = end_time - start_time

    return t

time_ = eratosthenes(number)

print(prime_num)

i_values_1 = []
time_values_1 = []

i_values_2 = []
time_values_2 = []

for i in range (3, 10000):
    print(i)
    i_values_1.append(i)
    t = first_prime_alg(i)
    time_values_1.append(t)

    i_values_2.append(i)
    time_ = eratosthenes(i)
    time_values_2.append(time_)

# print(i_values_1)
# print(time_values_1) 

# Create a figure and axes
fig, ax = plt.subplots()

# Create a line plot
ax.plot(i_values_1, time_values_1)
ax.plot(i_values_2, time_values_2)

# Customize the plot
ax.set_xlabel("N")
ax.set_ylabel("Time")
ax.set_title("Time consumption")
ax.legend()

# Display the plot
plt.show()
 
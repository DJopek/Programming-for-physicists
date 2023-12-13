import random

def function(x):
    return x**3 + 2

def monte_carlo_integration(a, b, n, epsilon) :

    # y_vals = []
    # x_vals = []
    n_down = 0

    check_vals = []

    for i in range (0, n):
        x = random.random()
        x_ab = x * (b - a) + a
        # x_vals.append(x_ab)

        y = random.random()
        y_ab = y * function(b)
        # y_vals.append(y_ab)

        if function(x_ab) > y_ab :
            n_down = n_down + 1 

        integral = n_down * function(b)*(b-a)/n

        print("iteration " + str(i) + ": " + str(integral))

        if i % 1000 == 0 :
            check_vals.append(integral)

            if i >= 1000:
                
                q = int(i/1000)
                p = q - 1

                diff = check_vals[q] - check_vals[p]
                
                if diff < epsilon :
                    break

monte_carlo_integration(0,1,10000, 0.1)

def monte_carlo_volume(n, epsilon):
    n_down = 0

    check_vals = []

    for i in range(0, 10000):
        numbers = []
        for j in range (0, n):
            random_val = random.random()
            numbers.append(random_val)

        sum = 0

        for k in range (0, n):
            sum += numbers[k] ** 2

        if 1 > sum:
            n_down = n_down + 1 

        integral = 2 ** n * n_down * 1*(1-0)/10000

        print("iteration " + str(i) + ": " + "volume = " + str(integral))


        if i % 1000 == 0 :
            check_vals.append(integral)

            if i >= 1000:
                
                q = int(i/1000)
                p = q - 1

                diff = check_vals[q] - check_vals[p]
                
                if diff < epsilon :
                    break

monte_carlo_volume(2, 0.002)
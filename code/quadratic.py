answer = "y"

while answer == "y":

    a = float(input("Input the coefficient a: "))
    b = float(input("Input the coefficient b: "))
    c = float(input("Input the coefficient c: "))

    determinant = b**2-4*a*c

    if a == 0:
        print("The a coefficient can't be 0!")
    
    else:

        if determinant > 0:
            x_1 = (-b+determinant**0.5)/(2*a)
            print("The first solution is: " + str(x_1))
            x_2 = (-b-determinant**0.5)/(2*a)
            print("The second solution is: " + str(x_2))
        elif determinant == 0:
            x = -b/(2*a)
            print("The solution is: " + str(x))

        else:
            print("The equation does not have a solution in real numbers!")

    answer = ""

    answer = input("Do you want to enter another year? (y/n) ")
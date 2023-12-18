answer = "y"

while answer == "y":

    n = int(input("input a natural number: "))

    for y in range(0,n):

        if y == 0:
            # print("     ", end="")
            print("\t", end="")

            for i in range (1, n+1):
                # print(str(i) + "    ", end="")
                print(str(i)+"\t", end="")

        print("\n")
        # print(str(y) + ":   ", end="")
        print(str(y+1) + ":\t", end="")


        for x in range(1,n+1):
            # print(f'{((x)*(y+1))}' + "    ", end="")
            print(f'{((x)*(y+1))}\t', end="")



    answer = ""

    answer = input("\nDo you want to enter another year? (y/n) ")
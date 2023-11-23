n = int(input("Input a number of discs: "))

def Hanoi (n, input, auxiliary, output):
    if n == 1 :
        print(f"moving from {input} -> {output}")
        return
    Hanoi(n-1, input, output, auxiliary)
    print(f"moving from {input} -> {output}")
    Hanoi(n-1, auxiliary, input, output)

Hanoi (n, "A", "C", "B")
import math
from math import log10, floor

def round_to_1(x):
    num_list = list(str(x))
    if num_list[0] == "0" and num_list[1] == "." and len(num_list) == 3:
        if int(num_list[2]) >= 5:
            return float(1)
        elif x == float(0):
            return float(0)
        else:
            return round(x, -int(floor(log10(abs(x)))))
    else:
        return round(x, -int(floor(log10(abs(x)))))
    
def round_values(y, x):
    num_list = list(str(x))

    if num_list[0] == "0":
        p = len(num_list)-2
        number = list(str(round(y,p)))
        if (x == float(0) and y == 0):
            return float(0)
        elif len(num_list) > len(number):
            for i in range(len(num_list)):
                if len(num_list) != len(number):
                    number.append("0")
            return "".join(number)
        else:
            return round(y, p)

    elif num_list[0] != "0":
        for i in range(len(num_list)):
            if num_list[i] == ".":
                j = i - 1
        p = (-1)*j

        number = list(str(round(y,p)))

        if len(list(str(abs(round(y,p))))) == len(num_list):
            return round(y, p)
        else:
            return float(round(y, p))


def round_values_errors(values, errors):
    errors_rounded = []
    values_rounded = []
    for i in range(len(errors)):
        errors_rounded.append(round_to_1(errors[i]))
    for i in range(len(values)):
        values_rounded.append(round_values(values[i], errors_rounded[i]))
    return values_rounded, errors_rounded

def table(values, errors):

    for i in range(len(values)):
        values[i], errors[i] = round_values_errors(values[i], errors[i])

    num_rows = len(values[0])

    for i in range(num_rows):
        row = " & ".join(f"{values[j][i]} $\\pm$ {errors[j][i]}" for j in range(len(values)))
        print(row + " \\\\ \\hline")

def table_justvalues(values):

    num_rows = len(values[0])

    for i in range(num_rows):
        row = " & ".join(f"{values[j][i]}" for j in range(len(values)))
        print(row + " \\\\ \\hline")
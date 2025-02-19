import math
from math import log10, floor

def round_to_1(x):
    num_list = list(str(x))
    if num_list[0] == "0" and num_list[1] == "." and len(num_list) == 3:
        if int(num_list[2]) >= 5:
            return float(1)
    return round(x, -int(floor(log10(abs(x)))))
    
def round_values(y, x):
    num_list = list(str(x))
    if num_list[0] == "0":
        p = len(num_list)-2
    elif num_list[0] != "0":
        for i in range(len(num_list)):
            if num_list[i] == ".":
                j = i
        p = (-1)*j
    return round(y, p)

def round_values_errors(values, errors):
    errors_rounded = []
    values_rounded = []
    for i in range(len(errors)):
        errors_rounded.append(round_to_1(errors[i]))
    for i in range(len(values)):
        values_rounded.append(round_values(values[i], errors_rounded[i]))
    return values_rounded, errors_rounded

def table(values, errors):
    num_rows = len(values[0])

    for i in range(num_rows):
        row = " & ".join(f"{values[j][i]}\\pm{errors[j][i]}" for j in range(len(values)))
        print(row)

table(values=[P,I,R], errors=[sigma_P,sigma_I,sigma_R])
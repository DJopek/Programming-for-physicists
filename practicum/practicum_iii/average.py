# n = int(input("Input number of numbers: "))
# n = len(data)

# data_10 = []

# data = [2.5, 2.4, 2.6]
# data = [3.6, 2.7, 3]
data = [4.4, 4.2, 4]

# n = len(data_10)
n = len(data)
# print(n)

# for i in range (n):
#     data.append(data_10[i]/10)

# for i in range (n):
#     number = float(input("Input a number: "))
#     data.append(number)

sum_average = 0

for i in range (len(data)):
    sum_average += data[i]

average = sum_average * 1/n

print("The average is: " + str(average))

sum_deviasion = 0
for i in range (len(data)):
    sum_deviasion += (data[i] - average) ** 2 

deviation = 1/(n-1) * sum_deviasion
standard_deviation = deviation ** 0.5

print("The standard deviation is: " + str(standard_deviation))

average_error = standard_deviation * 1/(n**0.5)
print("The error of average is: " + str(average_error))
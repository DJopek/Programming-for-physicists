# n = int(input("Input number of numbers: "))
# n = len(data)

data = [11.94, 11.95, 11.95]
data = [1.98, 1.97, 1.98]

n = len(data)

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
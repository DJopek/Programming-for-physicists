import math

# Define data
T1_4p_A = [0.9, 1.3, 0.95]
T2_4p_A = [8.45, 8.85, 8.45]

T1_4p_B = [1.2, 1.15, 1.10]
T2_4p_B = [8.7, 8.7, 8.6]

L5p_A = 36.5
L5p_B = 36.5

T1_1_A = [1.10, 1.10, 1.10]
T1_2_A = [10.5, 10.5, 10.5]

T2_1_A = [1.8, 1.95, 2.10]
T2_2_A = [9.95, 10.15, 10.25]

T3_1_A = [0.85, 14.00]
T3_2_A = [9.7, 22.85]

TS_1_A = [11.65, 24.15]
TS_2_A = [24.15, 36.00]

T1_1 = [1.95, 1.05, 1.25]
T1_2 = [11.35, 10.45, 10.65]

T2_1 = [0.85, 0.6, 0.7]
T2_2 = [9.55, 9.3, 9.45]

T3_1 = [1.3, 25.8]
T3_2 = [10.25, 34.8]

TS_1 = [23.05, 46.35]
TS_2 = [46.35, 70.00]

# T4_A = [val * 2 for val in TS_2]
# T4_B = [val * 2 for val in TS_2]

# Function to calculate differences
def calculate_differences(arr1, arr2):
    differences = []
    for i in range(len(arr1)):
        differences.append(arr2[i] - arr1[i])
    return differences

# Calculate differences for each pair
diff_T_4p = calculate_differences(T2_4p_A, T1_4p_A)
diff_T_4p_2 = calculate_differences(T2_4p_B, T1_4p_B)

print("5T of the first at 36 lenght is:", diff_T_4p)
print("5T of the first at 36 lenght is:", diff_T_4p_2)


diff_T1_A = calculate_differences(T1_1_A, T1_2_A)
diff_T2_A = calculate_differences(T2_1_A, T2_2_A)
diff_T3_A = calculate_differences(T3_1_A, T3_2_A)
diff_TS_A = calculate_differences(TS_1_A, TS_2_A)

diff_T1 = calculate_differences(T1_1, T1_2)
diff_T2 = calculate_differences(T2_1, T2_2)
diff_T3 = calculate_differences(T3_1, T3_2)
diff_TS = calculate_differences(TS_1, TS_2)

# Print differences
print("Differences for T1_A:", diff_T1_A)
print("Differences for T2_A:", diff_T2_A)
print("Differences for T3_A:", diff_T3_A)
print("Differences for TS_A:", diff_TS_A)

print("Differences for T1_B:", diff_T1)
print("Differences for T2_B:", diff_T2)
print("Differences for T3_B:", diff_T3)
print("Differences for TS_B:", diff_TS)


T5p_A_data = [
    ([0.4], [9.8]),
    ([0.4], [9.5]),
    ([0.75], [10.20]),
    ([0.45], [9.20]),
    ([1.75], [11.10]),
    ([0.45], [9.00]),
    ([1.6], [10.95]),
    ([0.45], [8.55]),
    ( [1.20], [10.55]),
    ([0.55], [8.25])
]


T5p_B_data = [
    ([0.7], [10.1]),
    ([0.45], [9.8]),
    ([1.55], [10.95]),
    ([0.5], [9.55]),
    ([1.45], [10.90]),
    ([1.35], [10.20]),
    ([1.20], [10.60]),
    ([0.55], [9.15]),
    ([1.6], [10.85]),
    ([0.7], [9.05])
]

# Function to calculate differences
def calculate_differences(data):
    differences = []
    for pair in data:
        difference = pair[1][0] - pair[0][0]
        differences.append(difference)
    return differences

# Calculate differences
diff_T5p_A = calculate_differences(T5p_A_data)
diff_T5p_B = calculate_differences(T5p_B_data)

differences = []

for idx, diff in enumerate(diff_T5p_A, start=1):
    print(f" {diff}")
    differences.append(diff)

# Print differences
for idx, diff in enumerate(diff_T5p_B, start=1):
    print(f" {diff}")
    differences.append(diff)


def calculate_omega(differences):
    omegas = []
    for diff in differences:
        omega = 2 * math.pi / abs(diff/5)
        omegas.append(omega)
    return omegas

# Calculate omega
omega_T1_4p_A = calculate_omega(diff_T_4p)
omega_T1_4p_B = calculate_omega(diff_T_4p_2)

omega_T1_A = calculate_omega(diff_T1_A)
omega_T2_A = calculate_omega(diff_T2_A)
omega_T3_A = calculate_omega(diff_T3_A)
omega_TS_A = calculate_omega(diff_TS_A)

omega_T1_B = calculate_omega(diff_T1)
omega_T2_B = calculate_omega(diff_T2)
omega_T3_B = calculate_omega(diff_T3)
omega_TS_B = calculate_omega(diff_TS)

omega_T5p_A = calculate_omega(diff_T5p_A)
omega_T5p_B = calculate_omega(diff_T5p_B)

# Print omega
print("\nAngular frequency for T1_4p_A:", omega_T1_4p_A)
print("Angular frequency for T1_4p_B:", omega_T1_4p_B)
print("Angular frequency for T1_A:", omega_T1_A)
print("Angular frequency for T2_A:", omega_T2_A)
print("Angular frequency for T3_A:", omega_T3_A)
print("Angular frequency for TS_A:", omega_TS_A)
print("Angular frequency for T1_B:", omega_T1_B)
print("Angular frequency for T2_B:", omega_T2_B)
print("Angular frequency for T3_B:", omega_T3_B)
print("Angular frequency for TS_B:", omega_TS_B)
print("Angular frequency for T5p_A:", omega_T5p_A)
print("Angular frequency for T5p_B:", omega_T5p_B)


kappa_A = []
kappa_B = []

for i in range (len(omega_T5p_A)-1):
    if i % 2 == 0:
        k = ((omega_T5p_A[i+1])**2 - (omega_T5p_A[i])**2 )/((omega_T5p_A[i+1])**2 + (omega_T5p_A[i])**2)
        kappa_A.append(k)

print(kappa_A)

for i in range (len(omega_T5p_B)-1):
    if i % 2 == 0:
        k = ((omega_T5p_B[i+1])**2 - (omega_T5p_B[i])**2 )/((omega_T5p_B[i+1])**2 + (omega_T5p_B[i])**2)
        kappa_B.append(k)

print(kappa_B)
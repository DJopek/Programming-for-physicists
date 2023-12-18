import numpy as np
import matplotlib.pyplot as plt

def calculate_trajectory(initial_velocity, angle, g=9.81):

    angle_rad = np.radians(angle)

    v0x = initial_velocity * np.cos(angle_rad)
    v0y = initial_velocity * np.sin(angle_rad)

    flight_time = (2 * v0y) / g

    time_value = [0]

    step = 0

    while step < flight_time :
        step += flight_time/1000
        time_value.append(step)
    
    time_value.append(flight_time)

    x_points = []
    y_points = []

    for i in range (0, len(time_value)):

        x = v0x * time_value[i]
        x_points.append(x)

        y = v0y * time_value[i] - 0.5 * g * time_value[i]**2
        y_points.append(y)

    return x_points, y_points

def plot_trajectory(x_points, y_points):
    plt.plot(x_points, y_points)
    plt.title('Trajectory of Projectile Motion')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.grid(True)
    plt.show()

initial_velocity = float(input("Zadejte počáteční rychlost (m/s): "))
angle = float(input("Zadejte úhel vrhu (stupeň): "))

x_points, y_points = calculate_trajectory(initial_velocity, angle)

plot_trajectory(x_points, y_points)
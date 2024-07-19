import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

initial_temp = 500.0  # high initial temperature
cooling_factor = 0.85  # cooling factor (decrease by 1% each iteration)
num_iterations = 350
0
def objective_function(x, y):
    return -200 * math.exp(-0.02 * math.sqrt(x**2 + y**2))

# Generate random numbers for states i
current_x = random.uniform(-30, 0)
current_y = random.uniform(0, 30)

def accepted_States_plot(current_x, current_y, initial_temp, cooling_factor, num_iterations):
    temperatures = [initial_temp * (cooling_factor ** i) for i in range(num_iterations)]
    acceptance_rates = []
    current_xs = []  # store current_x values in each iteration
    current_ys = []  # store current_y values in each iteration
    current_zs = []

    for temp in temperatures:
        # initial guess
        current_z = objective_function(current_x, current_y)

        for _ in range(1):  # only one iteration per temperature step
            new_x = random.uniform(-30, 0)  # generate a new solution
            new_y = random.uniform(0, 30)
            new_z = objective_function(new_x, new_y)

            delta_z = new_z - current_z

            if delta_z < 0 or random.random() < math.exp(-delta_z / temp):
                current_x = new_x
                current_y = new_y
                current_z = new_z

            current_xs.append(current_x)  # store current_x value
            current_ys.append(current_y)  # store current_y value
            current_zs.append(current_z)

    return current_xs, current_ys, current_zs, temperatures

current_xs, current_ys, current_zs, temperatures = accepted_States_plot(current_x, current_y, initial_temp, cooling_factor, num_iterations)

# Creating a 3D scatter plot
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(current_xs, current_ys, current_zs, c=range(num_iterations), cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
ax.set_title('3D Scatter Plot of Accepted States')
plt.savefig('3d_scatter_plot.png')
plt.show()

# Temperature vs Iteration Number graph
plt.figure(figsize=(12, 6))
plt.plot(range(1, num_iterations + 1), temperatures)
plt.xlabel('Iteration Number')
plt.ylabel('Temperature')
plt.title('Temperature vs Iteration Number')
plt.savefig('temperature_vs_iteration.png')
plt.show()

# Iteration Number vs Function Value graph
plt.figure(figsize=(12, 6))
plt.plot(range(1, num_iterations + 1), current_zs)
plt.xlabel('Iteration Number')
plt.ylabel('Function Value')
plt.title('Iteration Number vs Function Value')
plt.savefig('function_value_vs_iteration.png')
plt.show()
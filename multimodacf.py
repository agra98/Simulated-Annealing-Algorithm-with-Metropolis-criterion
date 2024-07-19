import numpy as np
import random
import matplotlib.pyplot as plt
import math

initial_temp = 500.0  # high initial temperature
num_iterations = 2000
n = 350  # number of transition states
a = -5
b = 5
cooling_factor = 0.85
min_temp = 1e-8  # minimum temperature to avoid division by zero

def objective_function(x, y):
    return 2*(x**2) -1.05*(x**4) + (x**6)/6 + x*y+ y**2

# Generate random numbers for states i
current_x = random.uniform(a,b)
current_y = random.uniform(a, b)

def cooling_schedule(cooling_factor, initial_temp, current_iteration):
    return max(initial_temp * (cooling_factor**current_iteration), min_temp)

def simulated_annealing(current_x, current_y, initial_temp, num_iterations, n):
    temperatures = []

    equilibrium_xs = []  # store equilibrium_x values in each transition state
    equilibrium_ys = []  # store equilibrium_y values in each transition state
    equilibrium_zs = []

    all_states = []

    for j in range(n):
        # initial guess
        current_z = objective_function(current_x, current_y)

        for i in range(num_iterations):
            new_x = random.uniform(a,b)  # generate a new solution
            new_y = random.uniform(a, b)
            new_z = objective_function(new_x, new_y)

            delta_z = new_z - current_z

            if delta_z < 0 or random.random() < math.exp(-delta_z / initial_temp):
                current_x = new_x
                current_y = new_y
                current_z = new_z

        # Store the function value for the current iteration of the inner loop
        all_states.append([current_x, current_y, current_z])

        equilibrium_xs.append(current_x)
        equilibrium_ys.append(current_y)
        equilibrium_zs.append(current_z)

        temperatures.append(initial_temp)
        initial_temp = cooling_schedule(cooling_factor, initial_temp, j)

    return temperatures, equilibrium_zs, equilibrium_ys, equilibrium_xs, all_states

temperatures, equilibrium_zs, equilibrium_ys, equilibrium_xs, all_states = simulated_annealing(current_x, current_y, initial_temp, num_iterations, n)

# Convert all_states to numpy array for easier slicing
all_states = np.array(all_states)
states_x = all_states[:, 0]
states_y = all_states[:, 1]
states_z = all_states[:, 2]

# Create color gradient based on the iteration order
colors = np.linspace(0, 1, len(all_states))

# Create 3D scatter plot of states
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(states_x, states_y, states_z, c=colors, cmap='viridis', marker='o', label='Data Points', s=4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Function Value')
ax.set_title('3D Scatter Plot for Equilibrium States of Multimodal Function')

# Add color bar as legend
cbar = plt.colorbar(sc)
cbar.set_label('Iteration Order')

# Create tick positions corresponding to iteration numbers
num_ticks = 5  # Number of ticks on the color bar
tick_positions = np.linspace(0, 1, num_ticks)
tick_labels = np.linspace(1, len(all_states), num_ticks, dtype=int)

cbar.set_ticks(tick_positions)
cbar.set_ticklabels(tick_labels)

# Set the viewpoint from below
ax.view_init(elev=50, azim=50)
plt.show()


# Plot accepted states vs. iteration
plt.plot(range(len(equilibrium_xs)), equilibrium_xs, label='X')
plt.plot(range(len(equilibrium_ys)), equilibrium_ys, label='Y')
plt.xlabel('Transition State')
plt.ylabel('Equilibrium X and Y')
plt.title('Equilibrium States vs. Iteration')
plt.legend()
plt.show()

# Plot function value vs. iteration
plt.plot(range(len(equilibrium_zs)), equilibrium_zs)
plt.xlabel('Transition State')
plt.ylabel('Function Value')
plt.title('Function Value vs. Transition State')
plt.show()

# Plot temperature vs. iteration
plt.plot(range(len(temperatures)), temperatures)
plt.xlabel('Transition State')
plt.ylabel('Temperature')
plt.title('Temperature vs. Transition State')
plt.text(0.95, 0.9, 'Starting Temperature = 500K', fontsize=10, verticalalignment='top', horizontalalignment='right', transform=plt.gca().transAxes)
plt.show()

print('Final X:', equilibrium_xs[-1])
print('Final Y:', equilibrium_ys[-1])
print('Final Function Value:', equilibrium_zs[-1])
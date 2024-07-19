import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as math

initial_temp = 500.0  # high initial temperature
num_iterations = 2000
Tmax = initial_temp
Tmin = 400  # minimum temperature
n = 200  # number of transition state
a = -30
b = 0
c = 30

def objective_function(x, y):
    return -200 * math.exp(-0.02 * math.sqrt(x**2 + y**2))

# Generate random numbers for states i
current_x = random.uniform(b,c)
current_y = random.uniform(a, b)

def cooling_schedule(Tmax, Tmin, n, current_temp,current_iteration):
    alpha = (Tmin/Tmax)**(1/(n-1))
    return ((alpha)**current_iteration) * current_temp

def simulated_annealing(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n):

    temperatures = []

    current_xs = []  # store current_x values in each iteration
    current_ys = []  # store current_y values in each iteration
    current_zs = []

    equilibrium_xs = []  # store equilibrium_x values in each transition state
    equilibrium_ys = []  # store equilibrium_y values in each transition state
    equilibrium_zs = []

    inner_loop_xs = []
    inner_loop_ys = []
    inner_loop_zs = []  # store function values for each iteration of inner loop

    for j in range(2, n+1):
        # initial guess
        current_z = objective_function(current_x, current_y)

        for i in range(num_iterations):
            new_x = random.uniform(b,c)  # generate a new solution
            new_y = random.uniform(a, c)
            new_z = objective_function(new_x, new_y)

            delta_z = new_z - current_z

            if delta_z < 0 or random.random() < math.exp(-delta_z / initial_temp):
                current_x = new_x
                current_y = new_y
                current_z = new_z

            # Store the function value for the current iteration of the inner loop
            inner_loop_xs.append(current_x)
            inner_loop_ys.append(current_y)
            inner_loop_zs.append(current_z)

        equilibrium_xs.append(current_x)
        equilibrium_ys.append(current_y)
        equilibrium_zs.append(current_z)

        temperatures.append(initial_temp)
        initial_temp = cooling_schedule(Tmax, Tmin, n, initial_temp, j)

    return temperatures, equilibrium_zs, equilibrium_ys, equilibrium_xs, current_xs, current_ys, current_zs,inner_loop_ys,inner_loop_xs,inner_loop_zs

temperatures, equilibrium_zs, equilibrium_ys, equilibrium_xs, current_xs, current_ys, current_zs,inner_loop_ys,inner_loop_xs,inner_loop_zs = simulated_annealing(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n)

# Create color gradient based on the iteration order
colors = np.linspace(0, 1, len(inner_loop_xs))

# Create 3D scatter plot of states
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(inner_loop_xs, inner_loop_ys,inner_loop_zs, c=colors, cmap='viridis', marker='o', label='Data Points', s=4)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Energy')
ax.set_title('3D Scatter Plot of States (Energy Function: y = 0.26(X1^2 + X2^2) - 0.48X1X2)')

# Add color bar as legend
cbar = plt.colorbar(sc)
cbar.set_label('Iteration Order')

# Create tick positions corresponding to iteration numbers
num_ticks = 5  # Number of ticks on the color bar
tick_positions = np.linspace(0, 1, num_ticks)
tick_labels = np.linspace(1, len(inner_loop_xs), num_ticks, dtype=int)

cbar.set_ticks(tick_positions)
cbar.set_ticklabels(tick_labels)
ax.view_init(elev=50, azim=10)  # set the viewpoint from below
plt.show()

'''
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

#Create a surface plot of the objective function
x_range = np.linspace(-32, 32, 100)
y_range = np.linspace(-32, 32, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = -200 * np.exp(-0.02 * np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('F(X,Y')
plt.title('Benchmark Function Surface Plot')
plt.show()


# Create 3D scatter plot of states
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(equilibrium_xs, equilibrium_ys, equilibrium_zs, c=equilibrium_zs, cmap='plasma', marker='o', label='Data Points', s=8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
ax.set_title('3D Scatter Plot for States of Cost Function: Z = (x-5)**2 + y**2-3*y+2')
plt.show()
'''

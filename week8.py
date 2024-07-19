import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as math

initial_temp = 500.0  # high initial temperature
num_iterations = 2000
Tmax = initial_temp
Tmin = 400  # minimum temperature
n = 350   # number of  transition state
a= 0
b= 6

def objective_function(x, y):
    return (x-5)**2 + y**2-3*y+2

# Generate random numbers for states i
current_x = random.uniform(a, b)
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
            new_x = random.uniform(a, b)  # generate a new solution
            new_y = random.uniform(a, b)
            new_z = objective_function(new_x, new_y)

            delta_z = new_z - current_z

            if delta_z < 0 or random.random() < math.exp(-delta_z / initial_temp):
                current_x = new_x
                current_y = new_y
                current_z = new_z

            current_xs.append(current_x)  # store current_x value
            current_ys.append(current_y)  # store current_y value
            current_zs.append(current_z)

            # Store the function value for the current iteration of the inner loop
            inner_loop_xs.append(current_x)
            inner_loop_ys.append(current_y)
            inner_loop_zs.append(current_z)


        equilibrium_xs.append(current_x)
        equilibrium_ys.append(current_y)
        equilibrium_zs.append(current_z)

        temperatures.append(initial_temp)
        initial_temp = cooling_schedule(Tmax, Tmin, n, initial_temp, j)

        # Plot the function values for the current iteration of the inner loop
        if j == 90:
            plt.plot(range(len(inner_loop_xs)), inner_loop_xs)
            plt.xlabel('Iteration')
            plt.ylabel('X Value')
            plt.title(
                f'X Value vs. Iteration Temperature: {temperatures[-1]:.2f}K')
            plt.show()

            plt.hist(inner_loop_xs, bins=20, edgecolor='black')
            plt.xlabel('Current X Value')
            plt.ylabel('Frequency')
            plt.title(
                f'Frequency of X: {temperatures[-1]:.2f}K')
            plt.show()
            inner_loop_xs.clear()

            plt.plot(range(len(inner_loop_ys)), inner_loop_ys)
            plt.xlabel('Iteration')
            plt.ylabel('Y Value')
            plt.title(
                f'Y Value vs. Iteration Temperature: {temperatures[-1]:.2f}K')
            plt.show()

            plt.hist(inner_loop_ys, bins=20, edgecolor='black')
            plt.xlabel('Current Y Value')
            plt.ylabel('Frequency')
            plt.title(
                f'Frequency of Y: {temperatures[-1]:.2f}K')
            plt.show()
            inner_loop_ys.clear()

            plt.plot(range(len(inner_loop_zs)), inner_loop_zs)
            plt.xlabel('Iteration')
            plt.ylabel('Function Value')
            plt.title(
                f'Function Value vs. Iteration Temperature: {temperatures[-1]:.2f}K')
            plt.show()

            plt.hist(inner_loop_zs, bins=20, edgecolor='black')
            plt.xlabel('Current Function Value')
            plt.ylabel('Frequency')
            plt.title(
                f'Frequency of F(x,y) : {temperatures[-1]:.2f}K')
            plt.show()
            inner_loop_zs.clear()
        else:
            inner_loop_xs.clear()
            inner_loop_ys.clear()
            inner_loop_zs.clear()



    return temperatures, equilibrium_zs, equilibrium_ys, equilibrium_xs, current_xs, current_ys, current_zs

temperatures, equilibrium_zs, equilibrium_ys, equilibrium_xs, current_xs, current_ys, current_zs = simulated_annealing(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n)


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
plt.text(0.95, 0.9, 'Starting Temperature = 1000K', fontsize=10, verticalalignment='top', horizontalalignment='right', transform=plt.gca().transAxes)
plt.show()

print('Final X:', equilibrium_xs[-1])
print('Final Y:', equilibrium_ys[-1])
print('Final Function Value:', equilibrium_zs[-1])

# Create 3D scatter plot of states
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(current_xs, current_ys, current_zs, c=current_zs, cmap='plasma', marker='o', label='Data Points', s=8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
ax.set_title('3D Scatter Plot for States of Cost Function: Z = (x-5)**2 + y**2-3*y+2')
plt.show()

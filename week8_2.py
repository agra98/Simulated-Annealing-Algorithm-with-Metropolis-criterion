import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as math

initial_temp = 500.0  # high initial temperature
num_iterations = 3000
Tmax = initial_temp
Tmin = 400  # minimum temperature
n = 120  # number of iterations per transition state
a= -32
b= 32

equilibrium_iterations = 2000  # number of iterations to wait for equilibrium
equilibrium_counter = 0

def objective_function(x, y):
    return -200 * math.exp(-0.02 * math.sqrt(x**2 + y**2))


def cooling_schedule(Tmax, Tmin, n, current_temp,current_iteration):
    alpha = (Tmin/Tmax)**(1/(n-1))
    return ((alpha)**current_iteration) * current_temp


def simulated_annealing( initial_temp, num_iterations, Tmax, Tmin, n):

    temperatures = []
    current_xs = []  # store current_x values in each iteration
    current_ys = []  # store current_y values in each iteration
    current_zs=[]

    equilibrium_xs = []  # store equilibrium_x values in each transition state
    equilibrium_ys = []  # store equilibrium_y values in each transition state
    equilibrium_zs = []

    transition_State_iterations=[] #iterations_in_each_transition_State
    iteration = 0

    inner_loop_xs = []
    inner_loop_ys = []
    inner_loop_zs = []  # store function values for each iteration of inner loop

    equilibrium_reached = False

    # Generate random numbers for states i
    current_x = random.uniform(a, b)
    current_y = random.uniform(a, b)

    for j in range(2,n):

        # initial guess
        current_z = objective_function(current_x, current_y)
        prev_z= current_z

        while iteration < num_iterations and not equilibrium_reached:
            new_x = random.uniform(a, b)  # generate a new solution
            new_y = random.uniform(a, b)
            new_z = objective_function(new_x, new_y)

            delta_z = new_z - current_z

            if delta_z < 0 or random.random() < math.exp(-delta_z / initial_temp):
                current_x = new_x
                current_y = new_y
                current_z = new_z

            # Store the function value for the current iteration of the inner loop
            inner_loop_xs.append(current_x)
            inner_loop_zs.append(current_z)

            if abs(prev_z - current_z) < 1e-3:
                equilibrium_counter += 1
                if equilibrium_counter >= equilibrium_iterations:
                    equilibrium_reached = True
            else:
                equilibrium_counter = 0

            iteration += 1

            prev_z=current_z

        transition_State_iterations.append(iteration)
        iteration=0

        temperatures.append(initial_temp)
        initial_temp = cooling_schedule(Tmax, Tmin, n, initial_temp, j)

        # Plot the function values for the current iteration of the inner loop
        if j == 40:
            plt.plot(range(len(inner_loop_xs)), inner_loop_xs)
            plt.xlabel('Iteration')
            plt.ylabel('X Value')
            plt.title(
                f'X Value vs. Iteration Temperature: {temperatures[-1]:.2f}K')
            plt.show()

            plt.hist(inner_loop_xs, bins=10, edgecolor='black')
            plt.xlabel('Current X Value')
            plt.ylabel('Frequency')
            plt.title(
                f'Frequency of X: {temperatures[-1]:.2f}K')
            plt.show()

            plt.plot(range(len(inner_loop_zs)), inner_loop_zs)
            plt.xlabel('Iteration')
            plt.ylabel('X Value')
            plt.title(
                f'Function Value vs. Iteration Temperature: {temperatures[-1]:.2f}K')
            plt.show()

            plt.hist(inner_loop_zs, bins=10, edgecolor='black')
            plt.xlabel('Function Value')
            plt.ylabel('Frequency')
            plt.title(
                f'Frequency of Function: {temperatures[-1]:.2f}K')
            plt.show()

            inner_loop_xs.clear()
            inner_loop_zs.clear()

        else:
            inner_loop_xs.clear()
            inner_loop_zs.clear()

        equilibrium_xs.append(current_x)
        equilibrium_ys.append(current_y)
        equilibrium_zs.append(current_z)

        temperatures.append(initial_temp)
        initial_temp = cooling_schedule(Tmax, Tmin, n, initial_temp,j)

    return current_xs, current_ys,current_zs,temperatures,equilibrium_zs,equilibrium_ys,equilibrium_xs,transition_State_iterations

current_xs, current_ys,current_zs,temperatures,equilibrium_zs,equilibrium_ys,equilibrium_xs,transition_State_iterations = simulated_annealing( initial_temp, num_iterations, Tmax, Tmin, n)


# Plot accepted states vs. iteration
plt.plot(range(len(equilibrium_xs)), equilibrium_xs, label='X')
plt.plot(range(len(equilibrium_ys)), equilibrium_ys, label='Y')
plt.xlabel('Iteration')
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
plt.text(0.95, 0.9, 'Starting Temperature = 500K', fontsize=10, verticalalignment='top', horizontalalignment='right',
         transform=plt.gca().transAxes)
plt.show()

print('Final X:', equilibrium_xs[-1])
print('Final Y:', equilibrium_ys[-1])
print('Final Function Value:', equilibrium_zs[-1])
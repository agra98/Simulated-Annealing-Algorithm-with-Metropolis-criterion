

import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as math

initial_temp = 1000.0  # high initial temperature
num_iterations = 3000
Tmax = initial_temp
Tmin = 50  # minimum temperature
n = 100  # number of iterations per transition state
a= 0
b= 8

def objective_function(x, y):
    return (x-5)*2 + y*2-3*y+2

# Generate random numbers for states i
current_x = random.uniform(a, b)
current_y = random.uniform(a, b)

def cooling_schedule(Tmax, Tmin, n, current_temp,current_iteration):
    alpha = (Tmin/Tmax)**(1/(n-1))
    return ((alpha)**current_iteration) * current_temp


def accepted_States_plot(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n):

    temperatures = []
    acceptance_rates = []
    current_xs = []  # store current_x values in each iteration
    current_ys = []  # store current_y values in each iteration
    current_zs=[]

    for j in range(n):
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

            temperatures.append(initial_temp)
            initial_temp = cooling_schedule(Tmax, Tmin, j, initial_temp,i)



    return current_xs, current_ys,current_zs,temperatures

current_xs, current_ys,current_zs,temperatures = accepted_States_plot(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n)


# Plot accepted states vs. iteration
plt.plot(range(len(current_xs)), current_xs, label='X')
plt.plot(range(len(current_ys)), current_ys, label='Y')
plt.xlabel('Iteration')
plt.ylabel('Current X and Y')
plt.title('Accepted States vs. Iteration')
plt.legend()
plt.show()

# Plot function value vs. iteration
plt.plot(range(len(current_zs)), current_zs)
plt.xlabel('Iteration')
plt.ylabel('Function Value')
plt.title('Function Value vs. Iteration')
plt.show()

# Plot temperature vs. iteration
plt.plot(range(n), temperatures)
plt.xlabel('Iteration')
plt.ylabel('Temperature')
plt.title('Temperature vs. Iteration')
plt.text(0.95, 0.9, 'Starting Temperature = 500K', fontsize=10, verticalalignment='top', horizontalalignment='right',
         transform=plt.gca().transAxes)
plt.show()

print('Final X:', current_xs[-1])
print('Final Y:', current_ys[-1])
print('Final Function Value:', current_zs[-1])
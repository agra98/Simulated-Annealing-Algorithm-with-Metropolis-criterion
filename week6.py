import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as math

initial_temp = 500.0  # high initial temperature
num_iterations = 2000
Tmax = initial_temp
Tmin = 1  # minimum temperature
n = 5  # number of iterations per transition state
a=-32
b=0
c= 30

def objective_function(x, y):
    return -200 * math.exp(-0.02 * math.sqrt(x**2 + y**2))

# Generate random numbers for states i
current_x = random.uniform(b,c)
current_y = random.uniform(a, b)

def cooling_schedule(Tmax, Tmin, n, current_iteration):
    beta = (Tmax - Tmin) / ((n - 1) * Tmax * Tmin)
    return Tmax / (1 + beta * current_iteration)

def simulated_annealing(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n):
    temperatures = [cooling_schedule(Tmax, Tmin, n, i) for i in range(1, num_iterations + 1)]
    acceptance_rates = []

    for temp in temperatures:
        # initial guess
        current_z = objective_function(current_x, current_y)
        num_accepted = 0

        for _ in range(num_iterations):
            new_x = random.uniform( b,c)  # generate a new solution
            new_y = random.uniform(a, b)
            new_z = objective_function(new_x, new_y)

            delta_z = new_z - current_z

            if delta_z < 0 or random.random() < math.exp(-delta_z / temp):
                current_x = new_x
                current_y = new_y
                current_z = new_z
                num_accepted += 1

        acceptance_rate = (num_accepted / num_iterations) * 100
        acceptance_rates.append(acceptance_rate)

    return temperatures, acceptance_rates

temperatures, acceptance_rates = simulated_annealing(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n)

plt.plot(temperatures, acceptance_rates)
plt.xlabel('Temperature')
plt.ylabel('Acceptance Rate (%)')
plt.title('Acceptance Rate vs. Temperature')
plt.show()

def accepted_States_plot(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n):

    temperatures = [cooling_schedule(Tmax, Tmin, n, i) for i in range(1, num_iterations + 1)]
    acceptance_rates = []
    current_xs = []  # store current_x values in each iteration
    current_ys = []  # store current_y values in each iteration
    current_zs=[]

    for temp in temperatures:
        # initial guess
        current_z = objective_function(current_x, current_y)

        for _ in range(1):  # only one iteration per temperature step
            new_x = random.uniform(a, b)  # generate a new solution
            new_y = random.uniform(a, b)
            new_z = objective_function(new_x, new_y)

            delta_z = new_z - current_z

            if delta_z < 0 or random.random() < math.exp(-delta_z / temp):
                current_x = new_x
                current_y = new_y
                current_z = new_z

            current_xs.append(current_x)  # store current_x value
            current_ys.append(current_y)  # store current_y value
            current_zs.append(current_z)

    return current_xs, current_ys,current_zs

current_xs, current_ys,current_zs = accepted_States_plot(current_x, current_y, initial_temp, num_iterations, Tmax, Tmin, n)

plt.plot(range(num_iterations), current_xs, label='X')
plt.plot(range(num_iterations), current_ys, label='Y')
plt.xlabel('Iteration')
plt.ylabel('Current X and Y')
plt.title('Accepted States vs. Iteration')
plt.legend()
plt.show()

plt.plot(range(num_iterations), current_zs)
plt.xlabel('Iteration')
plt.ylabel('Function Value')
plt.title('Function Value vs. Iteration')
plt.show()

plt.plot(range(num_iterations), temperatures)
plt.xlabel('Iteration')
plt.ylabel('Temperature')
plt.title('Temperature vs. Iteration')
plt.text(0.95,0.9,f'Starting Temerature = 500k', fontsize=10,verticalalignment='top', horizontalalignment='right',
             transform=plt.gca().transAxes)
plt.show()

print('Final X:', current_xs[-1])
print('Final Y:', current_ys[-1])
print('Final Function Value:', current_zs[-1])
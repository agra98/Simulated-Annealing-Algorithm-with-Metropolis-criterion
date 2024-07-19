import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as math

initial_temp = 500.0  # high initial temperature
alpha = 0.5  # cooling factor (decrease by 1% each iteration)
num_iterations = 500

def objective_function(x, y):
    return (x-5)**2 + y**2-3*y+2

# Generate random numbers for states i
current_x = random.uniform(-5, 10)
current_y = random.uniform(-5, 10)

def simulated_annealing(current_x, current_y, initial_temp,alpha, num_iterations):
    temperatures = [(initial_temp *alpha * i) for i in range(num_iterations)]
    acceptance_rates = []

    for temp in temperatures:
        # initial guess
        current_z = objective_function(current_x, current_y)
        num_accepted = 0

        for _ in range(num_iterations):
            new_x = random.uniform(-5, 10)  # generate a new solution
            new_y = random.uniform(-5, 10)
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

temperatures, acceptance_rates = simulated_annealing(current_x, current_y, initial_temp, alpha, num_iterations)

plt.plot(range(num_iterations), temperatures)
plt.xlabel('Iteration')
plt.ylabel('Temperature')
plt.title('Temperature vs. Iteration')
#plt.text(0.95,0.9,f'Starting Temerature = 500k\n Cooling Factor = {cooling_factor}', fontsize=10,verticalalignment='top', horizontalalignment='right',
#             transform=plt.gca().transAxes)
plt.show()

'''
plt.plot(temperatures, acceptance_rates)
plt.xlabel('Temperature')
plt.ylabel('Acceptance Rate (%)')
plt.title('Acceptance Rate vs. Temperature')
plt.show()

def accepted_States_plot(current_x, current_y, initial_temp, cooling_factor, num_iterations):
    temperatures = [initial_temp * (cooling_factor ** i) for i in range(num_iterations)]
    acceptance_rates = []
    current_xs = []  # store current_x values in each iteration
    current_ys = []  # store current_y values in each iteration
    current_zs=[]

    for temp in temperatures:
        # initial guess
        current_z = objective_function(current_x, current_y)

        for _ in range(1):  # only one iteration per temperature step
            new_x = random.uniform(-5, 10)  # generate a new solution
            new_y = random.uniform(-5, 10)
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

current_xs, current_ys,current_zs = accepted_States_plot(current_x, current_y, initial_temp, cooling_factor, num_iterations)

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
#plt.show()



print('Final X:', current_xs[-1])
print('Final Y:', current_ys[-1])
print('Final Function Value:', current_zs[-1])


# Create a 3D plot of the optimization process
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(range(num_iterations), current_xs, current_ys)
ax.set_xlabel('Iteration')
ax.set_ylabel('Current X')
ax.set_zlabel('Current Y')
plt.title('Optimization Process')
plt.show()

#Create a surface plot of the objective function
x_range = np.linspace(-300, 300, 200)
y_range = np.linspace(-300, 300, 200)
X, Y = np.meshgrid(x_range, y_range)
Z = (X-5)**2 + Y**2-3*Y+2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Objective Function Value')
plt.title('Objective Function Surface Plot')
plt.show()
'''
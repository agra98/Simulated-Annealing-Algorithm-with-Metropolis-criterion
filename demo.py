import random
import matplotlib.pyplot as plt
import numpy as np
import math as math

initial_temp = 500.0  # high initial temperature
cooling_factor = 0.85  # cooling factor (decrease by 1% each iteration)
num_iterations = 1000

def objective_function(x):
    return x**2

# Generate random numbers for states i
current_x = random.uniform(-1, 1)

def simulated_annealing(current_x,initial_temp, cooling_factor, num_iterations):
    temperatures = [initial_temp * (cooling_factor ** i) for i in range(1000)]
    acceptance_rates = []

    for temp in temperatures:
        # initial guess
        current_y = objective_function(current_x)
        num_accepted = 0

        for _ in range(num_iterations):
            new_x = random.uniform(-1, 1)  # generate a new solution
            new_y = objective_function(new_x)

            delta_y = new_y - current_y

            if delta_y < 0 or random.random() < math.exp(-delta_y / temp):
                current_x = new_x
                current_y = new_y
                num_accepted += 1

        acceptance_rate = (num_accepted / num_iterations) * 100
        acceptance_rates.append(acceptance_rate)

    return temperatures, acceptance_rates

temperatures, acceptance_rates = simulated_annealing(current_x,initial_temp, cooling_factor, num_iterations)

plt.plot(temperatures, acceptance_rates)
plt.xlabel('Temperature')
plt.ylabel('Acceptance Rate (%)')
plt.title('Acceptance Rate vs. Temperature')
plt.show()

def accepted_States_plot(current_x, initial_temp, cooling_factor, num_iterations):
    temperatures = [initial_temp * (cooling_factor ** i) for i in range(num_iterations)]
    acceptance_rates = []
    current_xs = []  # store current_x values in each iteration

    for temp in temperatures:
        # initial guess
        current_y = objective_function(current_x)

        for _ in range(1):  # only one iteration per temperature step
            new_x = random.uniform(-1, 1)  # generate a new solution
            new_y = objective_function(new_x)

            delta_y = new_y - current_y

            if delta_y < 0 or random.random() < math.exp(-delta_y / temp):
                current_x = new_x
                current_y = new_y

            current_xs.append(current_x)  # store current_x value

    return current_xs

current_xs = accepted_States_plot(current_x, initial_temp, cooling_factor, num_iterations)

plt.plot(range(num_iterations), current_xs)
plt.xlabel('Iteration')
plt.ylabel('Current X')
plt.title('Accepted States vs. Iteration')

plt.show()

'''import math
import random
import matplotlib.pyplot as plt

# Initial temperature and cooling factor
C = 500
cooling_Factor = 0.85

# Number of iterations
total_iteration = 1000

# Define the function to optimize
def f(x):
    return x ** 2

# Initialize the current state
state_i = random.uniform(-1, 1)

# Lists to store the cooling temperature and acceptance rate
cooling_temperature = []
accepted_rates = []

# Simulated annealing loop
for i in range(total_iteration):
    # Calculate the energy of the current state
    energy_i = f(state_i)

    # Generate a new state (proposal)
    state_j = random.uniform(-1, 1)
    energy_j = f(state_j)

    # Calculate the delta energy
    delta_E = energy_j - energy_i

    # Accept or reject the proposal based on Metropolis criteria
    if delta_E <= 0:
        state_i = state_j
        accepted = True
    else:
        boltzmann_factor = math.exp(-delta_E / C)
        r = random.uniform(0, 1)
        if boltzmann_factor > r:
            state_i = state_j
            accepted = True
        else:
            accepted = False

    # Update the cooling temperature and acceptance rate
    cooling_temperature.append(C)
    if accepted:
        accepted_rates.append(1)
    else:
        accepted_rates.append(0)

    # Decrease the temperature
    C *= cooling_Factor

# Calculate the acceptance rate for each iteration
acceptance_rate = [sum(accepted_rates[:i+1]) / (i+1) for i in range(total_iteration)]

# Plot the acceptance rate vs. temperature
plt.plot(cooling_temperature, acceptance_rate, linestyle='-', color="green")
plt.xlabel('Temperature')
plt.ylabel('Acceptance Rate')
plt.title('Acceptance Rate vs. Temperature')
plt.show()'''
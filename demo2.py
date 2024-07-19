import numpy as np
import random
import math
import matplotlib.pyplot as plt

def objective_function(x):
    return x**2

# Generate random numbers for states i
current_x = random.uniform(-1, 1)

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

# Example usage:
initial_temp = 500.0  # high initial temperature
cooling_factor = 0.85  # cooling factor (decrease by 1% each iteration)
num_iterations = 1000

current_xs = accepted_States_plot(current_x, initial_temp, cooling_factor, num_iterations)

#plt.figure(figsize=(12, 6))


#plt.subplot(1, 2, 2)
plt.plot(range(num_iterations), current_xs)
plt.xlabel('Iteration')
plt.ylabel('Current X')
plt.title('Current X vs. Iteration')

#plt.tight_layout()
plt.show()
import random
import matplotlib.pyplot as plt
import numpy as np

def objective_function(x):
    return x**2

def metropolis_hastings(num_iterations, initial_temperature):
    x_current = random.uniform(-1, 1)
    temperature = initial_temperature
    accepted_states = [x_current]
    function_values = [objective_function(x_current)]
    iterations = [0]
    temperatures = [temperature]

    for i in range(1, num_iterations):
        x_proposal = x_current + random.uniform(-1, 1)
        delta_E = objective_function(x_proposal) - objective_function(x_current)

        if delta_E < 0 or random.random() < np.exp(-delta_E / temperature):
            x_current = x_proposal

        temperature *= 0.85
        accepted_states.append(x_current)
        function_values.append(objective_function(x_current))
        iterations.append(i)
        temperatures.append(temperature)

    plt.figure(figsize=(8, 6))
    plt.plot(iterations, accepted_states)
    plt.xlabel('Iteration')
    plt.ylabel('Accepted State')
    plt.title('Accepted States vs. Iteration')
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(iterations, function_values)
    plt.xlabel('Iteration')
    plt.ylabel('Function Value')
    plt.title('Function Value vs. Iteration')
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.plot(iterations, temperatures)
    plt.xlabel('Iteration')
    plt.ylabel('Temperature')
    plt.title('Temperature vs. Iteration')
    plt.show()

metropolis_hastings(1000, 100)
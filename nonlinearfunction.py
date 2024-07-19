import random
import matplotlib.pyplot as plt
import numpy as np

def objective_function(x, y):
    return x**2 + y**2

def metropolis_hastings(num_iterations, initial_temperature):
    x_current = random.uniform(-1, 1)
    y_current = random.uniform(-1, 1)
    temperature = initial_temperature
    accepted_states_x = [x_current]
    accepted_states_y = [y_current]
    function_values = [objective_function(x_current, y_current)]
    iterations = [0]
    temperatures = [temperature]

    for i in range(1, num_iterations):
        x_proposal = x_current + random.uniform(-0.1, 0.1)
        y_proposal = y_current + random.uniform(-0.1, 0.1)
        delta_E = objective_function(x_proposal, y_proposal) - objective_function(x_current, y_current)

        if delta_E < 0 or random.random() < np.exp(-delta_E / temperature):
            x_current = x_proposal
            y_current = y_proposal

        temperature *= 0.85
        accepted_states_x.append(x_current)
        accepted_states_y.append(y_current)
        function_values.append(objective_function(x_current, y_current))
        iterations.append(i)
        temperatures.append(temperature)

    plt.figure(figsize=(8, 6))
    plt.plot(iterations, accepted_states_x, label='X')
    plt.plot(iterations, accepted_states_y, label='Y')
    plt.xlabel('Iteration')
    plt.ylabel('Accepted State')
    plt.title('Accepted States vs. Iteration')
    plt.legend()
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
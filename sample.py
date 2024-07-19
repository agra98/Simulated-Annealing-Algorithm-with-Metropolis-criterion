import math
import random
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 2

def metropolis(energy_i, energy_j, state_i, state_j, C):
    delta_E = energy_j - energy_i
    if delta_E <= 0:
        return state_j
    else:
        boltzmann_factor = math.exp(-delta_E / C)
        r = random.uniform(0, 1)
        if boltzmann_factor > r:
            return state_j
        else:
            return state_i

def simulate_annealing(initial_state, cooling_factor, initial_temperature, iterations):
    accepted_states = []
    C = initial_temperature
    state_i = initial_state

    for _ in range(iterations):
        energy_i = f(state_i)
        state_j = random.uniform(-1, 1)
        energy_j = f(state_j)
        state_i = metropolis(energy_i, energy_j, state_i, state_j, C)
        accepted_states.append(state_i)
        C *= cooling_factor

    mean = np.mean(accepted_states)
    variance = np.var(accepted_states)

    iterations = range(1, iterations + 1)
    plt.plot(iterations, accepted_states, linestyle='-', color="green")
    plt.xlabel('Iteration Number')
    plt.ylabel('Accepted States')
    plt.title('Accepted States in each Iteration')
    plt.text(0.95, 0.9, f'Temperature = {initial_temperature}K\nCooling Factor = {cooling_factor}',
             fontsize=10, verticalalignment='top', horizontalalignment='right',
             transform=plt.gca().transAxes)
    plt.grid(True)
    plt.show()

    return mean, variance

initial_state = random.uniform(-1, 1)
cooling_factor = 0.94
initial_temperature = 500
iterations = 1000

mean, variance = simulate_annealing(initial_state, cooling_factor, initial_temperature, iterations)
print("Mean value of accepted states:", mean)
print("Variance of accepted states:", variance)

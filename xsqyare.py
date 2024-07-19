import math
import random
import matplotlib.pyplot as plt
import numpy as np

C = 1000
cooling_Factor = 0.85

# Function definition
def f(x):
    return x**2

# Generate random numbers for states i
state_i = random.uniform(-1,1)


# Accepted States
Temperature = [200, 100, 1]

def coolingProcess(state_i, temperature, iterations=100):
    accepted_states = []
    for _ in range(iterations):
        new_state_i = random.uniform(-1,1)
        #new_state_j = random.uniform(-1,1)

        energy_1 = f(state_i)
        energy_2 = f(new_state_i)
        delta_E = energy_2 - energy_1
        if delta_E <= 0:
            state_i = new_state_i
        else:
            boltzmann_factor = np.exp(-delta_E / temperature)
            r = random.uniform(0, 1)
            if boltzmann_factor > r:
                state_i = new_state_i

        accepted_states.append(state_i)

    return accepted_states

accepted_states_list = [coolingProcess(state_i, temp) for temp in Temperature]

for i, temp in enumerate(Temperature):
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))
    ax[0].hist(accepted_states_list[i], bins=15, histtype='bar', alpha=0.5, edgecolor='black')
    ax[0].set_ylabel('Frequency')
    ax[0].set_title(f'Histogram for Temperature: {temp} K')
    ax[0].set_xlabel('x')


    iterations = range(1, len(accepted_states_list[i]) + 1)  # Generate iteration numbers
    ax[1].plot(iterations, accepted_states_list[i], linestyle='-', color='blue')
    ax[1].set_xlabel('Iteration Number')
    ax[1].set_ylabel('Value in Accepted States')
    ax[1].set_title(f'Scatter Plot for Temperature: {temp} K')
    ax[1].grid(True)

    plt.tight_layout()
    plt.show()
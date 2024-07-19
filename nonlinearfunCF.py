import random
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (x-5)**2 + y**2-3*y+2

def coolingProcessWithCoolingFactor(state_x,state_y,cooling_Factor,C,total_iteration):
    accepted_states_x = []
    accepted_states_y = []
    accepted_states_z = []
    for _ in range(total_iteration):

        # Calculate energies
        energy_i = f(state_x, state_y)

        state_j_x = random.uniform(0, 6)
        state_j_y = random.uniform(0, 6)
        energy_j = f(state_j_x, state_j_y)

        # Calculate delta_E
        delta_E = energy_j - energy_i

        # Accept or reject based on Metropolis criteria
        if delta_E <= 0:
            state_x = state_j_x
            state_y = state_j_y

        else:
            boltzmann_factor = math.exp(-delta_E / C)
            r = random.uniform(0, 1)
            if boltzmann_factor > r:
                state_x = state_j_x
                state_y = state_j_y

        accepted_states_x.append(state_x)
        accepted_states_y.append(state_y)
        accepted_states_z.append(energy_j)
        C *= cooling_Factor

    mean_x = np.mean(accepted_states_x)
    mean_y = np.mean(accepted_states_y)
    variance_x = np.var(accepted_states_x)
    variance_y = np.var(accepted_states_y)

    print("Final Optimum Values:")
    print("x =", state_x)
    print("y =", state_y)
    print("Optimum minimum value of f(x,y):", f(state_x, state_y))

    iterations = range(1, len(accepted_states_x) + 1)  # Generate iteration numbers
    plt.plot(iterations, accepted_states_x, linestyle='-', label='x',color="green")
    plt.plot(iterations, accepted_states_y, linestyle='-', label='y',color="blue")
    plt.xlabel('Iteration Number')
    plt.ylabel('Accepted States')
    plt.title('Accepted States in each Iterations')
    plt.text(0.95,0.8,f'Temerature = 500k\n Cooling Factor = {cooling_Factor}', fontsize=10,verticalalignment='top', horizontalalignment='right',
             transform=plt.gca().transAxes)
    plt.legend()
    plt.show()

    plt.plot(iterations, accepted_states_z, linestyle='-', color="blue")
    plt.xlabel('Iteration Number')
    plt.ylabel('Function Values')
    plt.title('Function Value in each Iterations')
    plt.text(0.98, 0.95, f'Temerature = 500k\n Cooling Factor = 0.85', fontsize=10, verticalalignment='top',
             horizontalalignment='right',
             transform=plt.gca().transAxes)
    plt.legend()
    plt.show()

state_x = random.uniform(0, 6)
state_y = random.uniform(0, 6)

coolingProcessWithCoolingFactor(state_x, state_y, 0.85, 500, 1000)
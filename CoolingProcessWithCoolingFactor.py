import math
import random
import matplotlib.pyplot as plt
import numpy as np

C = 500
cooling_Factor = 0.85
total_iteration = 1000


# Function definition
def f(x):
    return x ** 2


# Generate random numbers for states i
state_i = random.uniform(-1, 1)

accepted_states = []
energy=[]
rejected_states = []
cooling_temperature = []
accepted_rates = []

for i in range(total_iteration):

    for x in range(total_iteration):
        # Calculate energies
        energy_i = f(state_i)

        state_j = random.uniform(-1, 1)
        energy_j = f(state_j)

        # Calculate delta_E
        delta_E = energy_j - energy_i

        # Accept or reject based on Metropolis criteria
        if delta_E <= 0:
            accepted_states.append(state_j)
            energy.append(energy_j)
            state_i = state_j
        else:
            boltzmann_factor = math.exp(-delta_E / C)
            r = random.uniform(0, 1)
            if boltzmann_factor > r:
                accepted_states.append(state_j)
                energy.append(energy_j)
                state_i = state_j
            else:
                rejected_states.append(state_j)

    cooling_temperature.append(C)
    C *= cooling_Factor

    accepted_rate = len(accepted_states) / total_iteration
    accepted_rates.append(accepted_rate)

plt.plot(cooling_temperature, accepted_rates, linestyle='-', color="green")
plt.xlabel('Temperature')
plt.ylabel('Accepted Rate')
plt.title('Accepted Rate vs. Temperature')
plt.text(0.95,0.9,f'Starting Temerature = 500k\n Cooling Factor = {cooling_Factor}', fontsize=10,verticalalignment='top', horizontalalignment='right',
             transform=plt.gca().transAxes)
plt.grid(True)
plt.show()

def coolingProcessWithCoolingFactor(state_i,cooling_Facotr,C,iteration):
    accepted_states=[]
    for iteration in range(total_iteration):

        # Calculate energies
        energy_i = f(state_i)

        state_j = random.uniform(-1, 1)
        energy_j = f(state_j)

        # Calculate delta_E
        delta_E = energy_j - energy_i

        # Accept or reject based on Metropolis criteria
        if delta_E <= 0:
            #accepted_states.append(state_j)
            state_i = state_j
            energy_i= energy_j

        else:
            boltzmann_factor = math.exp(-delta_E / C)
            r = random.uniform(0, 1)
            if boltzmann_factor > r:
                #accepted_states.append(state_j)
                state_i = state_j
                energy_i = energy_j

        accepted_states.append(state_i)
        energy.append(energy_i)
        C *= cooling_Factor


    iterations = range(1, len(accepted_states) + 1)  # Generate iteration numbers
    plt.plot(iterations, accepted_states, linestyle='-',color="green")

    plt.xlabel('Iteration Number')
    plt.ylabel('Accepted States')
    plt.title('Accepted States in each Iterations')
    plt.text(0.95,0.9,f'Temerature = 500k\n Cooling Factor = {cooling_Factor}', fontsize=10,verticalalignment='top', horizontalalignment='right',
             transform=plt.gca().transAxes)
    plt.show()

    iterations = range(1, len(energy) + 1)  # Generate iteration numbers
    plt.plot(iterations, energy, linestyle='-', color="green")

    plt.xlabel('Iteration Number')
    plt.ylabel('Function Value')
    plt.title('Function Values after each Iterations')
    plt.text(0.95, 0.9, f'Temerature = 500k\n Cooling Factor = {cooling_Factor}', fontsize=10, verticalalignment='top',
             horizontalalignment='right',
             transform=plt.gca().transAxes)
    plt.show()
coolingProcessWithCoolingFactor(state_i,C,cooling_Factor,total_iteration)
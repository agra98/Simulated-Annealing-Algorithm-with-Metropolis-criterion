import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Constants
C = 100  # Temperature in Kelvin


# Function definition
def f(x):
    return x ** 2


# Generate random numbers for states i
state_i = random.uniform(-1, 1)

#Accepted States
accepted_states=[]

# Perform iterations

for iteration in range(100):

        #print(f"Iteration {iteration + 1}")
        #print('State i ', state_i)
        #print("State j:", state_j)

    # Calculate energies
    energy_i = f(state_i)

    state_j=random.uniform(-1,1)

    energy_j = f(state_j)

    # Calculate delta_E
    delta_E = energy_j - energy_i

    # Accept or reject based on Metropolis criteria
    if delta_E <= 0:
        accepted_states.append(state_j)
        state_i = state_j
        #state_j=random.uniform(-1,1)

    else:
        boltzmann_factor = math.exp(-delta_E / C)
        r=random.uniform(0, 1)
        if boltzmann_factor > r:
            accepted_states.append(state_j)
            state_i = state_j
            #state_j=random.uniform(-1,1)

    state_j = random.uniform(-1, 1)

    # Print iteration details
print("State i :", state_i)
print("State j :",state_j)
print("Energy of State j:", energy_j)
print()

# Plotting
x_values = [i for i in accepted_states]
y_values = [f(x) for x in x_values]

# Plot y=x^2
x = np.linspace(-1, 1, 100)
y = x**2
plt.plot(x, y, label='f(x)=x^2')


# Highlight the last point in a different color
plt.scatter(x_values[-1], y_values[-1], color='purple', label='Last Point', zorder=5,s=100)

# Plotting state_i values
plt.scatter(x_values[:-1], y_values[:-1], color='orange', label='Metropolis Samples')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Metropolis Sampling Results')
plt.legend()
plt.grid(True)
plt.show()

#metroplis_Simulation(Initial_state_i, Initial_state_j, C)


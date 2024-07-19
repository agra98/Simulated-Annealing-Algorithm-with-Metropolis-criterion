import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Initializing lists to store data for plotting
temp = []
states = []
function_vals = []
iterations = []

# Define the function to be minimized
def function(x1, x2):
    return x1 ** 2 + x2 ** 2 - 2 * x1 * x2

# Simulated annealing function
def anneal(t, c):
    # Reset lists to store data for plotting
    temp.clear()
    states.clear()
    function_vals.clear()
    iterations.clear()

    # Initializing the current states
    current_x1 = random.uniform(-1, 1)
    current_x2 = random.uniform(-1, 1)
    best_sol = (current_x1, current_x2)
    best_fval = function(current_x1, current_x2)

    # Generating new states
    iteration = 0
    while t > 1e-10:  # Prevent t from becoming zero
        for i in range(1, 1000):
            new_x1 = random.uniform(-1, 1)
            new_x2 = random.uniform(-1, 1)

            # Calculating the energy difference
            delta_e = function(new_x1, new_x2) - function(current_x1, current_x2)

            if delta_e <= 0:
                current_x1 = new_x1
                current_x2 = new_x2

                # Accepting condition
                if function(current_x1, current_x2) < best_fval:
                    best_sol = (current_x1, current_x2)
                    best_fval = function(current_x1, current_x2)
            else:
                Boltzmann_f = math.exp(-1 * delta_e / t)
                new_r = random.uniform(0, 1)

                if Boltzmann_f > new_r:
                    current_x1 = new_x1
                    current_x2 = new_x2

                    if function(current_x1, current_x2) < best_fval:
                        best_sol = (current_x1, current_x2)
                        best_fval = function(current_x1, current_x2)

            # Appending the lists
            temp.append(t)
            states.append((current_x1, current_x2))
            function_vals.append(function(current_x1, current_x2))
            iterations.append(iteration)
            iteration += 1

        # Updating the temperature with cooling schedule
        t = t * (c ** i)

    return best_sol, best_fval

best_sol, best_fval = anneal(1000, 0.99)

print("Optimal solution: ", best_sol)
print("Optimal function values: ", best_fval)

plt.figure(figsize=(10, 8))
plt.plot(iterations, temp, label='Temperature')
plt.title('Iterations vs Temperature')
plt.xlabel('Iterations')
plt.ylabel('Temperature')
plt.grid(True)
plt.legend()
plt.show()

# Recording the data points
x1 = np.linspace(-6, 6, 50)
x2 = np.linspace(-6, 6, 50)
x_1, x_2 = np.meshgrid(x1, x2)

fn = function(x_1, x_2)

# Finding global minimum point
global_Min = np.unravel_index(np.argmin(fn), fn.shape)
g_x1 = 0  # x_1[global_Min]
g_x2 = 0  # x_2[global_Min]
g_fn = function(g_x1, g_x2)  # fn[global_Min]

fig = plt.figure(figsize=(10, 8))
axes = fig.add_subplot(111, projection='3d')
axes.plot_surface(x_1, x_2, fn, cmap='viridis')

axes.scatter(g_x1, g_x2, g_fn, color='red', s=1000, label='Global Optimum')
axes.text(g_x1, g_x2, g_fn, 'Global Optimum', color='red')

axes.set_xlabel('X1')
axes.set_ylabel('X2')
axes.set_zlabel('f(xi)')
axes.set_title('Graph f(x1, x2) = x1^2 + x2^2 - 2*x1*x2')

plt.legend()
plt.show()

# Plotting other graphs
x = [s[0] for s in states]
y = [s[1] for s in states]

plt.figure(figsize=(10, 8))
plt.plot(iterations, x, label='Trajectory', color='blue', alpha=0.5)
plt.title('Iterations vs x1 values')
plt.xlabel('Iterations')
plt.ylabel('Current x1 values')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 8))
plt.plot(iterations, y, label='Trajectory', color='red', alpha=0.6)
plt.title('Iterations vs x2 values')
plt.xlabel('Iterations')
plt.ylabel('Current x2 values')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 8))
plt.plot(iterations, function_vals, label='Function values', color='green')
plt.title('Iterations vs Function values')
plt.xlabel('Iterations')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()
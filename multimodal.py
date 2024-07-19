import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as math
import seaborn as sns

initial_temp = 500.0  # high initial temperature
num_iterations = 2000
Tmax = initial_temp
Tmin = 400  # minimum temperature
n = 350  # number of  transition state
a= -5
b= 5

def objective_function(x, y):
    return 2*(x**2) -1.05*(x**4) + (x**6)/6 + x*y+ y**2
    #return (x - 5) ** 2 + y ** 2 - 3 * y + 2

# Generate random numbers for states i
current_x = random.uniform(a,b)
current_y = random.uniform(a, b)

def cooling_schedule(Tmax, Tmin, n, current_temp,current_iteration):
    alpha = (Tmin/Tmax)**(1/(n-1))
    return ((alpha)**current_iteration) * current_temp

temperatures = []

current_xs = []  # store current_x values in each iteration
current_ys = []  # store current_y values in each iteration
current_zs = []

equilibrium_xs = []  # store equilibrium_x values in each transition state
equilibrium_ys = []  # store equilibrium_y values in each transition state
equilibrium_zs = []

inner_loop_z1 = []
inner_loop_z2 = []
inner_loop_z3 = []  # store function values for each iteration of inner loop

all_xs=[]
all_ys=[]
all_zs=[]

for j in range(2, n+1):
    # initial guess
    current_z = objective_function(current_x, current_y)

    for i in range(num_iterations):
        new_x = random.uniform(a, b)  # generate a new solution
        new_y = random.uniform(a, b)
        new_z = objective_function(new_x, new_y)

        delta_z = new_z - current_z

        if delta_z < 0 or random.random() < math.exp(-delta_z / initial_temp):
            current_x = new_x
            current_y = new_y
            current_z = new_z

            # Store the function value for the current iteration of the inner loop
        if j==50:
            inner_loop_z1.append(current_z)
            temp1= temperatures[-1]
        if j==70:
            inner_loop_z2.append(current_z)
            temp2= temperatures[-1]
        if j==90:
            inner_loop_z3.append(current_z)
            temp3 = temperatures[-1]

        all_xs.append(current_x)
        all_ys.append(current_y)
        all_zs.append(current_z)

    equilibrium_xs.append(current_x)
    equilibrium_ys.append(current_y)
    equilibrium_zs.append(current_z)

    temperatures.append(initial_temp)
    initial_temp = cooling_schedule(Tmax, Tmin, n, initial_temp, j)

print('Final X:', equilibrium_xs[-1])
print('Final Y:', equilibrium_ys[-1])
print('Final Function Value:', equilibrium_zs[-1])

# Plot accepted states vs. iteration
plt.plot(range(len(equilibrium_xs)), equilibrium_xs, label='X')
plt.plot(range(len(equilibrium_ys)), equilibrium_ys, label='Y')
plt.xlabel('Transition State')
plt.ylabel('Equilibrium X and Y')
plt.title('Equilibrium States vs. Transition State')
plt.legend()
plt.show()

# Plot function value vs. iteration
plt.plot(range(len(equilibrium_zs)), equilibrium_zs)
plt.xlabel('Transition State')
plt.ylabel('Function Value')
plt.title('Function Value vs. Transition State')
plt.show()

# Plot temperature vs. iteration
plt.plot(range(len(temperatures)), temperatures)
plt.xlabel('Transition State')
plt.ylabel('Temperature')
plt.title('Temperature vs. Transition State')
plt.text(0.95, 0.9, 'Starting Temperature = 500K', fontsize=10, verticalalignment='top', horizontalalignment='right', transform=plt.gca().transAxes)
plt.show()

#Create a surface plot of the objective function
x_range = np.linspace(-30, 30, 100)
y_range = np.linspace(-30, 30, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = 2*(X**2) -1.05*(X**4) + (X**6)/6 + X*Y+ Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('F(X,Y')
plt.title('Multimodal Benchmark Function Surface Plot')
plt.show()

# Convert lists to numpy arrays for plotting
states_x = np.array(equilibrium_xs)
states_y= np.array(equilibrium_ys)
Energy = np.array(equilibrium_zs)

# Create color gradient based on the iteration order
colors = np.linspace(0, 1, len(states_x))

# Create 3D scatter plot of states
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(states_x, states_y, Energy, c=colors, cmap='viridis', marker='o', label='Data Points', s=4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('F(X,Y)')
ax.set_title('3D Plot of Equilibrium States of Multimodal Function')

# Add color bar as legend
cbar = plt.colorbar(sc)
cbar.set_label('Iteration Order')

# Create tick positions corresponding to iteration numbers
num_ticks = 5  # Number of ticks on the color bar
tick_positions = np.linspace(0, 1, num_ticks)
tick_labels = np.linspace(1, len(states_x), num_ticks, dtype=int)

cbar.set_ticks(tick_positions)
cbar.set_ticklabels(tick_labels)
# Set the viewpoint from below
ax.view_init(elev=50, azim=50)
plt.show()

# Boltzmann distributions for a specific temperature - Energy
plt.hist(inner_loop_z1, density=True)
plt.title(f"Distribution of the Energy at temperature {temp1}")
plt.xlabel("Functional value(energy)")
plt.ylabel("Probability")
plt.show()

# Boltzmann distributions for specific temperatures - Energy
sns.kdeplot(inner_loop_z1, label=f"Temperature : {format(temp1, '.3f')}K", shade=True, color='red')
sns.kdeplot(inner_loop_z2, label=f"Temperature : {format(temp2, '.3f')}K", shade=True, color='green')
sns.kdeplot(inner_loop_z3, label=f"Temperature : {format(temp3, '.3f')}K", shade=True, color='purple')
plt.xlim(-100, 500)
plt.title("Distribution of Function Values at Different Temperatures")
plt.xlabel("Functional values")
plt.ylabel("Density")
plt.legend()
plt.show()
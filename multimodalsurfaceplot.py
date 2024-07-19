import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of x and y values
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Define the function
Z = 2*(X**2) - 1.05*(X**4) + (X**6)/6 + X*Y + Y**2
#Z = (X-5)**2 + Y**2-3*Y+2

# Find the minimum point
min_idx = np.unravel_index(np.argmin(Z, axis=None), Z.shape)
min_x, min_y = X[min_idx], Y[min_idx]

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the surface plot
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Mark the minimum point as a red large dot
ax.scatter(min_x, min_y, np.min(Z), c='red', marker='o', s=100)

# Set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('F(X,Y)')
ax.set_title('Surface Plot of the Function with Global Minimum')

# Show the plot
plt.show()
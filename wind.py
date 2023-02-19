import numpy as np
import matplotlib.pyplot as plt

# Set the size of the figure
plt.figure(figsize=(6,6))

# Set the wind speed and direction
speed = 10
direction = 45

# Generate some random points
x = np.random.rand(100)
y = np.random.rand(100)

# Compute the wind x and y components
wx = speed * np.cos(np.deg2rad(direction))
wy = speed * np.sin(np.deg2rad(direction))

# Plot the wind arrow
plt.arrow(0, 0, wx, wy, head_width=0.2, head_length=0.2, fc='b', ec='b')

# Plot the points
plt.scatter(x, y)

# Set the x and y limits of the plot
plt.xlim(0,1)
plt.ylim(0,1)

# Show the plot
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Number of particles
num_particles = 100

# Generate random initial positions for particles
particle_positions = np.random.rand(num_particles, 2) * 100  # Adjust the range as needed

# Create a figure and axis
fig, ax = plt.subplots()

# Plot particles
ax.scatter(particle_positions[:, 0], particle_positions[:, 1], color='blue', marker='o', label='Particles')

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Particle Swarm Optimization')

# Set axis limits
ax.set_xlim(0, 100)  # Adjust as needed
ax.set_ylim(0, 100)  # Adjust as needed

# Add a legend
ax.legend()

# Show plot
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of particles
num_particles = 100

# Generate random initial positions and speeds for particles
particle_positions = np.random.rand(num_particles, 2) * 100
particle_speeds = np.random.rand(num_particles, 2) * 5  # Adjust speed as needed

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize scatter plot for particles
particles_plot = ax.scatter(particle_positions[:, 0], particle_positions[:, 1], color='blue', marker='o',
                            label='Particles', s=10)

# Initialize target
target = np.random.rand(2) * 100
target_plot = ax.scatter(*target, color='red', marker='x', label="Target", s=100)


# Function to update particle positions
def update(frame):
    global particle_positions, particle_speeds

    # Calculate distances to the target
    distances = np.linalg.norm(particle_positions - target, axis=1)

    # Find the index of the closest particle
    closest_particle_index = np.argmin(distances)
    closest_particle_position = particle_positions[closest_particle_index]

    # Update particle positions based on the speed of the closest particle
    particle_positions += particle_speeds[closest_particle_index]

    # Update scatter plot
    particles_plot.set_offsets(particle_positions)


# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Particle Swarm Optimization')

# Set axis limits
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Add a legend
ax.legend()

# Animate the plot
ani = FuncAnimation(fig, update, frames=range(100), interval=100, repeat=False)

# Show plot
plt.grid(True)
plt.show()

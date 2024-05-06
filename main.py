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
                            label='Particles', s=5)

# Initialize target
target = np.random.rand(2) * 100
target_plot = ax.scatter(*target, color='red', marker='x', label="Target", s=100)

# Initialize text annotation for iteration number
iteration_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=10, color='black', verticalalignment='top')


# Function to update particle positions
def update(frame):
    global particle_positions, particle_speeds

    # Calculate distances to the target
    distances = np.linalg.norm(particle_positions - target, axis=1)

    # Find the index of the closest particle
    closest_particle_index = np.argmin(distances)
    closest_particle_position = particle_positions[closest_particle_index]
    particle_speeds = particle_positions - particle_positions[closest_particle_index]
    for particle_speed in particle_speeds:
        if particle_speed.all() != 0:
            magnitude = np.linalg.norm(particle_speed)
            particle_speed /= magnitude
            particle_speed *= -1
    # Update particle positions based on the speed of the closest particle
    particle_positions += particle_speeds

    # Update scatter plot
    particles_plot.set_offsets(particle_positions)

    # Update iteration number text
    iteration_text.set_text('Iteration: {}'.format(frame))


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
ani = FuncAnimation(fig, update, frames=range(120), interval=100, repeat=False)

# Show plot
plt.grid(True)
plt.show()

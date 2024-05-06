# Particle Swarm Optimization (PSO) Animation

This Python script demonstrates a basic implementation of Particle Swarm Optimization (PSO) using matplotlib for visualization. PSO is a population-based optimization technique inspired by the social behavior of birds flocking or fish schooling.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## Installation
1. Clone or download the repository.
2. Ensure you have Python and the required libraries installed.
3. Run the script `pso_animation.py`.

## Usage
- Upon running the script, a plot will be generated showing particles moving towards a target point using PSO.
- The blue dots represent the particles, and the red 'x' denotes the target position.
- The animation will show the movement of particles towards the target over a number of iterations.

## Parameters
- `num_particles`: Number of particles in the swarm.
- `particle_positions`: Initial positions of particles randomly generated within a 100x100 space.
- `particle_speeds`: Initial speeds of particles randomly generated.
- `target`: Randomly generated target position within the 100x100 space.
- `update`: Function to update particle positions based on PSO algorithm.
- `frames`: Number of frames (iterations) for the animation.
- `interval`: Interval between frames in milliseconds.

## Customization
- You can adjust parameters such as `num_particles`, `particle_speeds`, and `interval` to observe different behaviors.
- Feel free to modify the visualization aspects such as colors, markers, and plot limits.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

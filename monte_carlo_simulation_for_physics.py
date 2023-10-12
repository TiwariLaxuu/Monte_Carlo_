import numpy as np
import matplotlib.pyplot as plt

# Constants
charge = 1.602e-19  # Elementary charge (in coulombs)
mass_proton = 1.673e-27  # Mass of a proton (in kilograms)
magnetic_field_strength = 0.5  # Magnetic field strength (in teslas)
initial_velocity = 1e5  # Initial velocity of the particle (in meters per second)
time_step = 1e-9  # Time step (in seconds)
num_steps = 1000  # Number of time steps

# Initialize particle properties
position = np.zeros(2)  # Initial position (x, y) in meters
velocity = np.array([initial_velocity, 0.0])  # Initial velocity (x, y) in m/s
acceleration = np.array([0.0, 0.0])  # Initial acceleration (x, y) in m/s^2

# Lists to store particle trajectory
x_positions = [position[0]]
y_positions = [position[1]]

# Perform Monte Carlo simulation
for _ in range(num_steps):
    # Calculate the Lorentz force (due to magnetic field)
    lorentz_force = charge * np.cross(velocity, magnetic_field_strength * np.array([0, 0, 1]))
    
    # Calculate acceleration using Newton's second law
    acceleration = lorentz_force / mass_proton
    
    # Update velocity and position using kinematic equations
    velocity += acceleration * time_step
    position += velocity * time_step
    
    # Append current position to trajectory lists
    x_positions.append(position[0])
    y_positions.append(position[1])

# Plot the particle trajectory
plt.figure(figsize=(8, 6))
plt.plot(x_positions, y_positions)
plt.title("Particle Trajectory in Magnetic Field")
plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")
plt.grid(True)
plt.show()

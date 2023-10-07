
'''
Suppose we want to estimate the integral of the function f(x) = x^2 from 0 to 1, i.e., ∫[0, 1] x^2 dx. 
We will use Monte Carlo integration to approximate this integral.
'''

import random
import math
import scipy.special

# Number of random samples
num_samples = 100000

# Initialize a variable to store the sum of function evaluations
sum_of_values = 0

# Perform Monte Carlo sampling
for _ in range(num_samples):
    # Generate a random x value between 0 and 1
    x = random.uniform(0, 1)
    
    # Evaluate the function at the random x value and add to the sum
    sum_of_values += x**2

# Calculate the average value of the function over the samples
average_value = sum_of_values / num_samples

# Calculate the estimated integral by multiplying the average by the interval [0, 1]
estimated_integral = average_value

print(f"Estimated Integral: {estimated_integral:.4f}")

'''
Let's estimate the volume of a high-dimensional hypersphere in 10 dimensions. The volume of an 
n-dimensional hypersphere with radius r is given by the formula: V = (π^(n/2) * r^n) / Γ((n/2) + 1), 
where Γ is the gamma function.
'''

# Number of dimensions
num_dimensions = 10

# Radius of the hypersphere
radius = 1.0

# Initialize a variable to store the count of points inside the hypersphere
points_inside = 0

# Perform Monte Carlo sampling
for _ in range(num_samples):
    # Generate a random point in num_dimensions-dimensional space
    random_point = [random.uniform(-radius, radius) for _ in range(num_dimensions)]
    
    # Calculate the Euclidean distance from the origin
    distance = sum(x**2 for x in random_point) ** 0.5
    
    # Check if the point is inside the hypersphere
    if distance <= radius:
        points_inside += 1

# Calculate the estimated volume of the hypersphere
estimated_volume = (points_inside / num_samples) * ((2 * radius) ** num_dimensions)

# Calculate the exact volume using the formula
exact_volume = (math.pi ** (num_dimensions / 2)) * (radius ** num_dimensions) / scipy.special.gamma((num_dimensions / 2) + 1)

print(f"Estimated Volume: {estimated_volume:.4f}")
print(f"Exact Volume: {exact_volume:.4f}")



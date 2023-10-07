import random

# Number of random points to generate
num_points = 100000

# Initialize a variable to count points inside the quarter-circle
points_inside = 0

# Perform Monte Carlo sampling
for _ in range(num_points):
    # Generate random (x, y) coordinates within a unit square [-1, 1] x [-1, 1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Check if the point is inside the quarter-circle (within the unit circle's upper-right quadrant)
    if x**2 + y**2 <= 1:
        points_inside += 1

# Calculate the estimated value of π
estimated_pi = 4 * (points_inside / num_points)

print(f"Estimated π: {estimated_pi:.6f}")

'''
Algorithm 
We specify the number of random points to generate (num_points). A larger number of points will provide a more accurate estimate of π.

We loop over the specified number of points and, in each iteration:

Generate random (x, y) coordinates within a unit square [-1, 1] x [-1, 1]. This is done by using random.uniform(-1, 1) for both x and y.
We check if each generated point is inside the quarter-circle (the upper-right quadrant of the unit circle) by testing if x^2 + y^2 <= 1. If the point satisfies this condition, it falls inside the quarter-circle.

We count the number of points that fall inside the quarter-circle.

Finally, we estimate the value of π using the formula 4 * (points_inside / num_points). This formula is based on the fact that the ratio of the area of the quarter-circle to the area of the unit square is π/4.
'''

'''
Monte Carlo estimation example, this time for approximating the value of π using a different approach 
called the "Buffon's Needle" experiment. This experiment involves dropping a needle onto a grid of 
parallel lines and calculating the probability that the needle crosses one of the lines. The 
probability is used to estimate π.
'''
num_trials = 1000000
# Length of the needle
needle_length = 1.0

# Width of the gap between parallel lines
line_spacing = 2.0

# Initialize a variable to count the number of crossings
crossings = 0

# Perform Monte Carlo trials
for _ in range(num_trials):
    # Randomly choose the midpoint of the needle (0 to line_spacing)
    midpoint = random.uniform(0, line_spacing)
    
    # Randomly choose the angle of the needle (0 to 90 degrees)
    angle_degrees = random.uniform(0, 90)
    
    # Calculate the distance from the midpoint to the nearest line
    distance_to_line = min(midpoint, line_spacing - midpoint)
    
    # Calculate the projection of the needle on the line
    projection = (needle_length / 2) * (1 / (distance_to_line * 2))
    
    # Check if the needle crosses a line
    if projection >= 1:
        crossings += 1

# Calculate the estimated value of π
estimated_pi = (2 * needle_length * num_trials) / (line_spacing * crossings)

print(f"Estimated π (Buffon's Needle): {estimated_pi:.6f}")

'''
Algorithm 
We specify the number of random trials (num_trials). Similar to the previous example, a larger number of trials will provide a more accurate estimate of π.

We define the length of the needle (needle_length) and the width of the gap between parallel lines (line_spacing).

In each trial, we perform the following steps:

    Randomly choose the midpoint of the needle within the range [0, line_spacing).
    Randomly choose the angle of the needle within the range [0, 90 degrees].
    Calculate the distance from the midpoint to the nearest line.
    Calculate the projection of the needle on the line.
    Check if the projection is greater than or equal to 1, indicating that the needle crosses a line.
    We count the number of crossings in the trials.

Finally, we estimate the value of π using the formula (2 * needle_length * num_trials) / (line_spacing * crossings). This formula is derived from the probability of crossing a line in the Buffon's Needle experiment.

As with the previous example, increasing the number of trials (num_trials) will lead to a more accurate estimate of π. This demonstrates how Monte Carlo methods can be applied in creative ways to approximate mathematical constants.

'''

'''
Monte Carlo estimation example, this time for estimating π using the "Random Dartboard" method. 
In this method, we randomly throw darts at a square target with a quarter-circle inscribed inside, 
and we use the ratio of darts inside the quarter-circle to the total darts thrown to estimate π.
'''

# Number of random darts to throw
num_darts = 100000

# Initialize a variable to count darts inside the quarter-circle
darts_inside = 0

# Perform Monte Carlo dart throwing
for _ in range(num_darts):
    # Generate random (x, y) coordinates within the unit square [-1, 1] x [-1, 1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Check if the point is inside the quarter-circle
    if x**2 + y**2 <= 1:
        darts_inside += 1

# Calculate the estimated value of π
estimated_pi = 4 * (darts_inside / num_darts)

print(f"Estimated π (Random Dartboard): {estimated_pi:.6f}")

'''
Algorithm
We specify the number of random darts to throw (num_darts). Similar to previous examples, a larger number of darts will provide a more accurate estimate of π.

In each dart-throwing trial, we:

Generate random (x, y) coordinates within the unit square [-1, 1] x [-1, 1] using random.uniform(-1, 1) for both x and y.
We check if the point (x, y) falls inside the quarter-circle by testing if x^2 + y^2 <= 1. If it does, we consider the dart to be inside the quarter-circle.

We count the number of darts that fall inside the quarter-circle.

Finally, we estimate the value of π using the formula 4 * (darts_inside / num_darts). This formula is based on the ratio of the area of the quarter-circle to the area of the unit square.
'''



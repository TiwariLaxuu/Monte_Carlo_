import numpy as np
import matplotlib.pyplot as plt

# Parameters of the normal distribution
mu = 2.0  # Mean
sigma = 0.5  # Standard Deviation

# Number of random samples to generate
num_samples = 10000

# Generate random samples from the normal distribution
samples = np.random.normal(mu, sigma, num_samples)

# Calculate the mean and standard deviation of the generated samples
sample_mean = np.mean(samples)
sample_std_deviation = np.std(samples)

# Calculate the theoretical mean and standard deviation of the normal distribution
theoretical_mean = mu
theoretical_std_deviation = sigma

# Plot a histogram of the generated samples
plt.hist(samples, bins=50, density=True, alpha=0.6, color='b', label='Generated Samples')
plt.title('Histogram of Generated Samples vs. Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plot the probability density function of the theoretical normal distribution
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))
plt.plot(x, pdf, 'r', lw=2, label='Theoretical Normal Distribution')

plt.legend()
plt.grid(True)
plt.show()

print(f"Sample Mean: {sample_mean:.4f}")
print(f"Theoretical Mean: {theoretical_mean:.4f}")
print(f"Sample Standard Deviation: {sample_std_deviation:.4f}")
print(f"Theoretical Standard Deviation: {theoretical_std_deviation:.4f}")

'''
We specify the parameters of the normal distribution, such as the mean (mu) and standard deviation (sigma).

We generate num_samples random samples from the normal distribution using np.random.normal.

We calculate the sample mean and sample standard deviation of the generated samples using np.mean and np.std.

We calculate the theoretical mean and theoretical standard deviation of the normal distribution, which should match the specified values (mu and sigma).

We plot a histogram of the generated samples to visualize their distribution and overlay the probability density function (PDF) of the theoretical normal distribution for comparison.

Finally, we display the sample and theoretical mean and standard deviation values.
'''

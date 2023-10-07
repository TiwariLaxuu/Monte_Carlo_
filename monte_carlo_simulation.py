import numpy as np

# Historical prices data
prices = [
    10.1, 10.3, 11, 10.9, 10.9, 10.9, 10.4, 9.84, 10, 10.1, 10.3,
    10.2, 10.1, 11.2, 11.4, 11.5, 11.8, 11.5, 10.7, 10.7, 10.4, 10.5
]

# Number of Monte Carlo simulations
num_simulations = 10000

# Number of months to project into the future
months_to_project = 12

# Calculate daily returns from historical prices
returns = np.diff(prices) / prices[:-1]

# Calculate the mean and standard deviation of daily returns
mean_return = np.mean(returns)
std_deviation = np.std(returns)

# Initialize an array to store future price simulations
future_prices = []

# Perform Monte Carlo simulations
for _ in range(num_simulations):
    # Generate a random set of daily returns based on a normal distribution
    random_returns = np.random.normal(mean_return, std_deviation, months_to_project)
    
    # Calculate future prices based on the random returns
    simulated_prices = [prices[-1]]
    for i in range(months_to_project):
        simulated_prices.append(simulated_prices[-1] * (1 + random_returns[i]))
    
    future_prices.append(simulated_prices)

# Calculate the standard deviation of future prices
future_prices = np.array(future_prices)
std_deviation_future = np.std(future_prices[:, -1])

print(f"Standard Deviation of Historical Returns: {std_deviation:.4f}")
print(f"Standard Deviation of Future Prices: {std_deviation_future:.4f}")

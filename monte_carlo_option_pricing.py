#CALL OPTION
'''
Monte Carlo simulations are commonly used in finance for option pricing. 
In this example, I'll demonstrate a simplified Monte Carlo simulation to estimate 
the value of a European call option using the Black-Scholes-Merton model. Keep in 
mind that real-world option pricing is more complex and may involve additional 
factors, such as dividend yields, interest rates, and volatility models.
'''

import numpy as np

# Option parameters
S0 = 100.0  # Initial stock price
K = 105.0   # Strike price
T = 1.0     # Time to expiration (in years)
r = 0.05    # Risk-free interest rate
sigma = 0.2 # Volatility

# Number of Monte Carlo simulations
num_simulations = 100000

# Generate random samples for stock price paths using geometric Brownian motion
num_time_steps = int(T * 252)  # Assuming 252 trading days in a year
dt = T / num_time_steps # Daily time steps for one year
S = np.zeros((num_simulations, num_time_steps + 1))  # Array to store price paths

for i in range(num_simulations):
    prices = [S0]
    for t in range(1, int(T * 252) + 1):
        z = np.random.standard_normal()
        price = prices[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        prices.append(price)
    S[i, :] = prices

# Calculate option payoffs and discounted expected values
payoffs = np.maximum(S[:, -1] - K, 0)
option_value = np.exp(-r * T) * np.mean(payoffs)

print(f"Monte Carlo Option Value: {option_value:.2f}")

'''
We define the parameters of the European call option, including the initial stock price (S0), strike price (K), time to expiration (T), risk-free interest rate (r), and volatility (sigma).

We specify the number of Monte Carlo simulations to perform (num_simulations).

We generate random samples for stock price paths using the geometric Brownian motion model. Each simulation consists of daily price steps for the specified time to expiration.

For each simulated price path, we calculate the option payoff at the expiration date, which is the maximum of (stock price - strike price) or zero.

We calculate the option value by discounting the expected payoff using the risk-free interest rate.


'''

#PUT OPTION 
'''
Monte Carlo simulation for option pricing, specifically for a European put option 
using the Black-Scholes-Merton model. The process is similar to the previous 
example but tailored for put options.
'''
import numpy as np

# Option parameters
S0 = 100.0  # Initial stock price
K = 105.0   # Strike price
T = 1.0     # Time to expiration (in years)
r = 0.05    # Risk-free interest rate
sigma = 0.2 # Volatility

# Number of Monte Carlo simulations
num_simulations = 100000

# Generate random samples for stock price paths using geometric Brownian motion
num_time_steps = int(T * 252)  # Assuming 252 trading days in a year
dt = T / num_time_steps  # Daily time steps for one year
S = np.zeros((num_simulations, num_time_steps + 1))  # Array to store price paths

for i in range(num_simulations):
    prices = [S0]
    for t in range(1, int(T * 252) + 1):
        z = np.random.standard_normal()
        price = prices[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        prices.append(price)
    S[i, :] = prices

# Calculate option payoffs and discounted expected values for European put option
payoffs = np.maximum(K - S[:, -1], 0)
option_value = np.exp(-r * T) * np.mean(payoffs)

print(f"Monte Carlo Option Value (European Put): {option_value:.2f}")


'''
Algorithm 

We define the same parameters for the European put option, including the initial stock price (S0), strike price (K), time to expiration (T), risk-free interest rate (r), and volatility (sigma).

We specify the number of Monte Carlo simulations to perform (num_simulations).

We generate random samples for stock price paths using the geometric Brownian motion model, just as in the previous example.

For each simulated price path, we calculate the option payoff at the expiration date, which is the maximum of (strike price - stock price) or zero. This is specific to a European put option.

We calculate the option value by discounting the expected payoff using the risk-free interest rate.
'''
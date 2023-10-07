'''
Let's consider a scenario where you want to estimate the potential return and risk
 (measured by standard deviation) of an investment portfolio consisting of two 
 assets: stocks and bonds. You'll use historical data to model the returns and 
 volatility of these assets.
'''

import numpy as np

# Historical annual returns and standard deviations for stocks and bonds (as percentages)
mean_stock_return = 7.0
std_dev_stock = 15.0
mean_bond_return = 3.0
std_dev_bond = 5.0

# Initial investment and investment horizon (in years)
initial_investment = 100000  # Initial investment amount
investment_horizon = 5       # Number of years

# Number of Monte Carlo simulations
num_simulations = 10000

# Generate random samples for future returns of stocks and bonds
np.random.seed(42)  # Set a random seed for reproducibility
random_returns_stock = np.random.normal(mean_stock_return, std_dev_stock, num_simulations)
random_returns_bond = np.random.normal(mean_bond_return, std_dev_bond, num_simulations)

# Calculate the future portfolio values for each simulation
portfolio_values = np.zeros((num_simulations, investment_horizon + 1))
portfolio_values[:, 0] = initial_investment

for t in range(1, investment_horizon + 1):
    portfolio_values[:, t] = portfolio_values[:, t - 1] * (1 + (random_returns_stock / 100) * 0.7 + (random_returns_bond / 100) * 0.3)

# Calculate the mean and standard deviation of portfolio values at the end of the investment horizon
final_portfolio_values = portfolio_values[:, -1]
mean_portfolio_value = np.mean(final_portfolio_values)
std_dev_portfolio_value = np.std(final_portfolio_values)

print(f"Mean Portfolio Value after {investment_horizon} years: ${mean_portfolio_value:.2f}")
print(f"Standard Deviation of Portfolio Value after {investment_horizon} years: ${std_dev_portfolio_value:.2f}")

'''
Algorithm
We specify the historical annual returns and standard deviations for stocks and bonds, representing their past performance.

We set the initial investment amount and investment horizon (number of years).

We specify the number of Monte Carlo simulations (num_simulations) to model future returns.

We use the np.random.normal function to generate random samples for future returns of stocks and bonds based on their historical data.

We calculate the future portfolio values for each simulation by applying the random returns to the initial investment.

Finally, we calculate the mean and standard deviation of portfolio values at the end of the investment horizon to assess the range of possible outcomes and their associated risk.
'''

'''
Suppose you are managing a manufacturing process, and you want to assess the risk 
of exceeding a defect rate of 5%. You have historical data indicating the average 
defect rate and its standard deviation. You'll use Monte Carlo simulation to 
estimate the probability of exceeding the 5% defect rate over a production run.
'''

import numpy as np

# Historical data for the defect rate (as a percentage)
mean_defect_rate = 4.0  # Average defect rate
std_dev_defect_rate = 1.0  # Standard deviation of defect rate

# Number of Monte Carlo simulations
num_simulations = 10000

# Number of production runs in each simulation
num_production_runs = 1000

# Defect rate threshold (e.g., 5%)
threshold = 5.0

# Initialize a variable to count the number of simulations exceeding the threshold
exceed_threshold_count = 0

# Perform Monte Carlo simulations
for _ in range(num_simulations):
    # Generate random samples for the defect rate using a normal distribution
    random_defect_rate = np.random.normal(mean_defect_rate, std_dev_defect_rate, num_production_runs)
    
    # Calculate the percentage of production runs exceeding the threshold
    exceed_threshold_percentage = np.mean(random_defect_rate > threshold)
    
    # Check if the threshold is exceeded and increment the count
    if exceed_threshold_percentage > 0.0:
        exceed_threshold_count += 1

# Calculate the probability of exceeding the threshold
probability_exceed_threshold = exceed_threshold_count / num_simulations

print(f"Estimated Probability of Exceeding {threshold}% Defect Rate: {probability_exceed_threshold:.4f}")

'''
Code Explanation
We specify the historical data for the defect rate, including the average defect rate (mean_defect_rate) and its standard deviation (std_dev_defect_rate).

We define the number of Monte Carlo simulations (num_simulations) to model future defect rates.

For each simulation, we generate random samples for the defect rate using a normal distribution based on historical data.

We calculate the percentage of production runs in each simulation that exceed the specified defect rate threshold (threshold).

We count the number of simulations where the threshold is exceeded and calculate the probability of exceeding the threshold over all simulations.
'''

'''
Suppose you manage a retail store, and you want to assess the risk of running out 
of stock for a particular product during the upcoming holiday season. You have 
historical sales data for this product and would like to estimate the probability 
of stockout (i.e., running out of inventory) during the holiday season.
'''

import numpy as np

# Historical daily sales data for the product (average and standard deviation)
mean_sales = 30  # Average daily sales
std_dev_sales = 10  # Standard deviation of daily sales

# Number of Monte Carlo simulations
num_simulations = 10000

# Number of days in the holiday season
holiday_season_days = 30

# Initialize a variable to count the number of simulations with stockout
stockout_count = 0

# Perform Monte Carlo simulations
for _ in range(num_simulations):
    # Generate random samples for daily sales using a normal distribution
    daily_sales = np.random.normal(mean_sales, std_dev_sales, holiday_season_days)
    
    # Calculate the cumulative sum of daily sales
    cumulative_sales = np.cumsum(daily_sales)
    
    # Check if stockout occurs (inventory drops to zero)
    if np.min(cumulative_sales) <= 0:
        stockout_count += 1

# Calculate the probability of stockout during the holiday season
probability_stockout = stockout_count / num_simulations

print(f"Estimated Probability of Stockout during Holiday Season: {probability_stockout:.4f}")


'''
Code Explanation
We specify the historical daily sales data for the product, including the average daily sales (mean_sales) and the standard deviation of daily sales (std_dev_sales).

We define the number of Monte Carlo simulations (num_simulations) to model future sales.

We specify the number of days in the holiday season (holiday_season_days) for which we want to assess the stockout risk.

For each simulation, we generate random samples for daily sales using a normal distribution based on historical data.

We calculate the cumulative sum of daily sales to simulate inventory levels over the holiday season.

We check if stockout occurs during any simulation (i.e., if the minimum cumulative sales becomes negative) and increment the stockout count accordingly.

Finally, we calculate the probability of stockout during the holiday season based on the count of simulations with stockout.
'''
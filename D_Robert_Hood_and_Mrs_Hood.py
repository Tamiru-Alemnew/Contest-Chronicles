from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

def max_profit_from_trades(data):
    # Group stock prices by stock symbol
    stocks = defaultdict(list)
    
    # Group stock prices by stock symbol and store them with the dates and prices
    for stock, date, price in data:
        stocks[stock].append((date, float(price)))
    
    # Initialize the total profit
    total_profit = 0
    
    # Starting amount
    starting_amount = 1000.0
    
    # Process each stock independently
    for stock, prices in stocks.items():
        # Sort by date to simulate buying/selling on valid dates
        prices.sort()
        
        # Initialize variables to track the minimum price seen so far (buying point)
        min_price = float('inf')
        max_profit = 0  # Track max profit for this stock
        
        for i in range(len(prices)):
            date, price = prices[i]
            
            # Update minimum price if we find a lower price (buying point)
            if price < min_price:
                min_price = price
            else:
                # Calculate potential profit by selling at the current price
                shares_bought = starting_amount / min_price
                profit = shares_bought * (price - min_price)
                max_profit = max(max_profit, profit)
        
        # Add the maximum profit for this stock to the total profit
        total_profit += max_profit
    
    # Round the final profit to the nearest dollar
    return Decimal(total_profit).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

# Example 1
data1 = [
    ("CSCO", "10/18/2024", 41.89),
    ("AMZN", "10/10/2024", 113.67),
    ("AMZN", "10/18/2024", 120.5),
    ("CSCO", "

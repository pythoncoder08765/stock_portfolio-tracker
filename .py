# Hardcoded dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}

portfolio = {}

print("📈 Stock Portfolio Tracker")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found. Please choose from the list above.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number for quantity.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    value = quantity * stock_prices[stock]
    total_value += value
    print(f"{stock}: {quantity} shares → ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optionally save to file
save_choice = input("Do you want to save the result to 'portfolio.txt'? (yes/no): ").lower()
if save_choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("----------------------\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity} shares → ${quantity * stock_prices[stock]}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print("✅ Portfolio saved to 'portfolio.txt'.")

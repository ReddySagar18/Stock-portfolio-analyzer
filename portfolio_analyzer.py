portfolio_analyzer.py
def analyze_portfolio(portfolio):
    for stock in portfolio:
        name = stock["name"]
        buy_price = stock["buy_price"]
        current_price = stock["current_price"]
        quantity = stock["quantity"]

        investment = buy_price * quantity
        current_value = current_price * quantity
        profit_or_loss = current_value - investment

        status = "Profit" if profit_or_loss > 0 else "Loss" if profit_or_loss < 0 else "No Profit No Loss"

        print(f"Stock: {name}")
        print(f"Investment: ₹{investment}")
        print(f"Current Value: ₹{current_value}")
        print(f"{status}: ₹{abs(profit_or_loss)}\n")

portfolio = [
    {"name": "TCS", "buy_price": 3200, "current_price": 3500, "quantity": 10},
    {"name": "INFY", "buy_price": 1400, "current_price": 1300, "quantity": 5},
    {"name": "RELIANCE", "buy_price": 2500, "current_price": 2500, "quantity": 8},
]

analyze_portfolio(portfolio)

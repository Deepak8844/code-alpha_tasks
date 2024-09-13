
stock_prices = {
    'AAPLE': 175.00,  
    'TESLA': 340.00,
    'GOOGLE': 2800.00  
}


portfolio = {
    'AAPLE': 10,  
    'TESLA': 5,   
    'GOOGLE': 2 
}   

def fetch_stock_price(symbol):
    
    
    return stock_prices.get(symbol, 0)

def calculate_portfolio_value(portfolio):
    total_value = 0
    for symbol, quantity in portfolio.items():
        price = fetch_stock_price(symbol)
        total_value += price * quantity
        print(f'{symbol}: {quantity} shares @ ${price} each = ${price * quantity}')
    return total_value

def main():
    print("Stock Portfolio Tracker")
    print("-----------------------")
    total_value = calculate_portfolio_value(portfolio)
    print("-----------------------")
    print(f'Total Portfolio Value: ${total_value:.2f}')

if __name__ == '__main__':
    main()

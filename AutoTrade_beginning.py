import asyncio
import ccxt


async def trade_assets(exchange, symbol, amount, direction):
    # Define the order parameters
    order_type = 'limit'
    price = exchange.fetch_ticker(symbol)['last']
    order = None

    # Execute a buy or sell order
    if direction == 'buy':
        order = exchange.create_order(symbol, order_type, 'buy', amount, price)
    elif direction == 'sell':
        order = exchange.create_order(symbol, order_type, 'sell', amount, price)
    else:
        print(f"Error: Invalid trade direction {direction}")
        return

    # Check the status of the order
    status = exchange.fetch_order(order['id'], symbol)
    print(f"Order status: {status['status']}")


async def main():
    # Initialize the exchange object
    exchange = ccxt.binance()

    # Define the symbol for trading
    symbol = 'BTC/ETH'

    # Define the amount to trade
    amount = 0.1

    # Define the trade direction
    direction = 'buy'

    # Schedule the trade to happen in the future
    await asyncio.sleep(3600)  # wait for one hour
    await trade_assets(exchange, symbol, amount, direction)
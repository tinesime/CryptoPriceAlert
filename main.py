import fire
import ccxt

def fetch_markets(exchange_id):
  exchange = getattr(ccxt, exchange_id)()
  markets = exchange.load_markets()
  return markets

def fetch_eth_price():
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker("ETH/USDT")
    return ticker["last"]

if __name__ == '__main__':
  print(fetch_eth_price())
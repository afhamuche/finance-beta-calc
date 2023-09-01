import yfinance as yf
import time

stock_symbols = ["TTEN3.SA", "ABCB4.SA", "BMOB3.SA", "AGRO3.SA", "ENAT3.SA", "EZTC3.SA", "KEPL3.SA", "LOGG3.SA", "LOGN3.SA", "UNIP3.SA"]

ibovespa_symbol = "^BVSP"

def track_stock_price(stock_symbols):

    stock_list_size = len(stock_symbols)

    while True:
        try:
            volatility = 0.0

            for stock_symbol in stock_symbols:
                stock = yf.Ticker(stock_symbol)
                stock_data = stock.history(period="1d")
                open_price = stock_data["Open"].iloc[-1]
                current_price = stock_data["Close"].iloc[-1]

                variation = (current_price - open_price) / open_price
                volatility += variation

            volatility = volatility / stock_list_size

            print(f'Index volatility = {volatility * 100:.2f}%')

            stock = yf.Ticker(ibovespa_symbol)
            stock_data = stock.history(period="1d")
            open_price = stock_data["Open"].iloc[-1]
            current_price = stock_data["Close"].iloc[-1]

            variation = (current_price - open_price) / open_price
            print(f'IBOV variation = {variation * 100:.2f}%')
            #print(stock_data)

            beta = volatility / variation
            print(f'BETA (Index/IBOV) = {beta:.2f}')

            print ('\n- - - - - - - - - - - - - - - - - - - - \n')


            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    track_stock_price(stock_symbols)


import requests, sys, os, json
from tabulate import tabulate
from fmp_python.fmp import FMP


def main():
    n_stocks = num_of_stocks()
    top_stocks = wsb(n_stocks)
    view_data(top_stocks)
    ...


#get number of stocks user wants to view, return n_stocks int
def num_of_stocks():
    n_stocks = input("How many tickers would you like to view? (1-25): ").strip()
    try:
        n_stocks = int(n_stocks)
        if 1 <= n_stocks <= 25:
            return n_stocks
        else:
            print("Please input an integer, 1-25.")
            return num_of_stocks()
    except ValueError:
        print("Please input an integer, 1-25.")
        return num_of_stocks()
    

#get data from WSB API, make a list out of each of the tickers from that data,
#append those lists to top_stocks list, return top_stocks list
def wsb(n_stocks):
    top_stocks = []
    response = requests.get("https://tradestie.com/api/v1/apps/reddit")
    if response.status_code == 200:
        wsb_data = response.json()
        for i in wsb_data[:n_stocks]:
            top_stocks.append([i['ticker'], i['sentiment'], i['no_of_comments']])
        return top_stocks
    else:
        sys.exit("Error getting WSB API data")


#display the WSB API data in a nice table
def view_data(top_stocks):
    headers = ["Ticker", "Sentiment", "Comments"]
    table = tabulate(top_stocks, headers=headers, tablefmt="fancy_grid")
    print(table)


#get stock prices: current, previousClose, dayLow(?), dayHigh(?)
#get stock prices: yearHigh(?), yearLow(?), priceAvg50, priceAvg200
#get volume, avgVolume
#get name, marketCap
def check_stock():
    ticker = ""
    fmp_key = os.environ.get("FMP_API_KEY")
    fmp = FMP(api_key=fmp_key)
    print(fmp.get_quote(ticker))
    print(fmp.get_quote_short(ticker))
    print(json.dumps(fmp.get_historical_chart("4hour", ticker), indent=2))
    print(json.dumps(fmp.get_historical_price(ticker), indent=2))
    ...


#get news mentioning ticker
def get_news():
    ticker = ""
    marketaux_key = os.environ.get("MARKETAUX_API_KEY")
    url = f"https://api.marketaux.com/v1/news/all?symbols={ticker}&filter_entities=true&api_token={marketaux_key}"
    response = requests.get(url)
    response_json = response.json()
    print(json.dumps(response_json, indent=2))
    ...


if __name__ == "__main__":
    main()
import requests, sys, os, json
from tabulate import tabulate
from fmp_python.fmp import FMP


def main():
    n_stocks = num_of_stocks()
    top_stocks = wsb(n_stocks)
    view_data(update_top_stocks(top_stocks))
    #menu(top_stocks)
    #check_stock()
    #get_news()
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
            top_stocks.append([i['ticker'], i['no_of_comments'], i['sentiment']])
        return top_stocks
    else:
        sys.exit("Error getting WSB API data")


#add price, company name mcap to top_stocks list
def update_top_stocks(top_stocks):
    fmp_key = os.environ.get("FMP_API_KEY")
    fmp = FMP(api_key=fmp_key)
    for index in range(len(top_stocks)):
        info = fmp.get_quote(top_stocks[index][0])
        price = "$" + str(info[0]["price"])
        top_stocks[index].append(price)
    return top_stocks



#display the WSB API data in a nice table
def view_data(top_stocks):
    headers = ["Ticker", "Mentions", "Sentiment", "Price"]
    table = tabulate(top_stocks, headers=headers, tablefmt="fancy_grid")
    print(table)


def menu():
    ticker_input = input("Which ticker would you like more info on?: ")
    print("Would you like:")
    print("1. Company description")
    print("2. Price and Trading Info")
    choice = input(": ")
    ...

#get stock prices: current, previousClose, dayLow(?), dayHigh(?)
#get stock prices: yearHigh(?), yearLow(?), priceAvg50, priceAvg200
#get volume, avgVolume
#get name, marketCap
def check_stock():
    ticker = "NVDA" #placeholder
    fmp_key = os.environ.get("FMP_API_KEY")
    fmp = FMP(api_key=fmp_key)
    print(fmp.get_quote(ticker))
    #print(fmp.get_quote_short(ticker))
    #print(json.dumps(fmp.get_historical_chart("4hour", ticker), indent=2))
    #print(json.dumps(fmp.get_historical_price(ticker), indent=2))
    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={fmp_key}"
    response = requests.get(url)
    response_json = response.json()
    #print(json.dumps(response_json, indent=2))
    print(response_json[0]["description"])
    ...


#get news mentioning ticker
def get_news():
    ticker = "NVDA" #placeholder
    marketaux_key = os.environ.get("MARKETAUX_API_KEY")
    url = f"https://api.marketaux.com/v1/news/all?symbols={ticker}&filter_entities=true&api_token={marketaux_key}"
    response = requests.get(url)
    response_json = response.json()
    print(json.dumps(response_json, indent=2))
    ...


if __name__ == "__main__":
    main()
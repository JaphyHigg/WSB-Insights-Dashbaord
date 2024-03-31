import requests, sys, os, json
from tabulate import tabulate
from fmp_python.fmp import FMP


def main(n_stocks = 1):
    top_stocks = wsb(n_stocks)
    view_data(update_top_stocks(top_stocks))
    menu()
    #get_news()
    ...


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


#add price to top_stocks list
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
    print("Would you like:")
    print("1. More info on a ticker")
    print("2. Increase the number of tickers")
    first_choice = input(":").strip().lower()
    if first_choice[0] == "1" or first_choice[0] == "m":
        ticker_input = input("Which ticker would you like more info on?: ").strip().lower()
        check_stock(ticker_input)
    elif first_choice[0] == "2" or first_choice[0] == "i":
        main(num_of_stocks())
    else:
        print("Invalid choice. Please choose option 1 or 2.")
        menu()


#get more info about company and stock price, as well as a company description
def check_stock(ticker):
    print()
    fmp_key = os.environ.get("FMP_API_KEY")
    fmp = FMP(api_key=fmp_key)
    quote = fmp.get_quote(ticker)
    print(quote)
    ticker_info0 = [[quote[0]["symbol"], quote[0]["name"], ("$" + str(quote[0]["price"])), 
                    ("$" + str("{:,}".format(quote[0]["marketCap"])))]] 
    ticker_info1 = [[("$" + str(quote[0]["open"])), ("$" + str(quote[0]["previousClose"])),
        "{:,}".format(quote[0]["volume"]), "{:,}".format(quote[0]["avgVolume"])]]
    ticker_info2 = [[("$" + str(quote[0]["yearHigh"])), ("$" + str(quote[0]["yearLow"])),
                     ("$" + str(quote[0]["priceAvg50"])), ("$" + str(quote[0]["priceAvg50"]))]] 
    headers0 = ["Ticker", "Name", "Price", "Market Cap"]
    table0 = tabulate(ticker_info0, headers=headers0, tablefmt="fancy_grid")
    print(table0)
    headers1 = ["Open", "Previous Close", "Volume", "Avg Volume"]
    table1 = tabulate(ticker_info1, headers=headers1, tablefmt="fancy_grid")
    print(table1)
    headers2 = ["Year High", "Year Low", "50 Day Avg Price", "200 Day Avg Price"]
    table2 = tabulate(ticker_info2, headers=headers2, tablefmt="fancy_grid")
    print(table2)
    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={fmp_key}"
    response = requests.get(url)
    response_json = response.json()
    print(response_json[0]["description"])
    print()
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


#get number of stocks user wants to view, return n_stocks int
def num_of_stocks():
    n_stocks = input("How many tickers would you like to view? (1-50): ").strip()
    try:
        n_stocks = int(n_stocks)
        if 1 <= n_stocks <= 50:
            return n_stocks
        else:
            print("Please input an integer, 1-50.")
            return num_of_stocks()
    except ValueError:
        print("Please input an integer, 1-50.")
        return num_of_stocks()
    

if __name__ == "__main__":
    main()
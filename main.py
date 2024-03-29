import requests, sys
from tabulate import tabulate


def main():
    n_stocks = num_of_stocks()
    top_stocks = wsb(n_stocks)
    view_data(top_stocks)


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


if __name__ == "__main__":
    main()
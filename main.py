import requests, sys


def main():
    top_20 = wsb()


#get data from WSB API, make a list out of each of the top 20 tickers from that data,
#append those lists to top_20 list, return top_20 list
def wsb():
    top_20 = []
    response = requests.get("https://tradestie.com/api/v1/apps/reddit")
    if response.status_code == 200:
        wsb_data = response.json()
        for i in wsb_data[:20]:
            top_20.append([i['ticker'], i['no_of_comments'], i['sentiment']])
        return top_20
    else:
        sys.exit("Error getting WSB API data")


if __name__ == "__main__":
    main()
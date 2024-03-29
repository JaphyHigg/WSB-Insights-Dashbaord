import requests, json, sys


def main():
    top_20 = wsb()


def wsb():
    top_20 = []
    response = requests.get("https://tradestie.com/api/v1/apps/reddit")
    if response.status_code == 200:
        wsb_data = response.json()
        wsb_data_json = json.dumps(wsb_data, indent=2)
        # print(wsb_data_json)
        for i in wsb_data[:20]:
            top_20.append([i['ticker'], i['no_of_comments'], i['sentiment']])
        # print(top_20)
        # print(top_20[0])
        # print(top_20[0][0])
        return top_20
    else:
        sys.exit("Error getting WSB API data")

if __name__ == "__main__":
    main()
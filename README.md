# Wall Street Bets Insights Dashboard

This program grabs top mentioned tickers from the Wall Street Bets subreddit using an api. It then uses the Financial Modeling Prep API to get more data about the tickers. The use types in which of the tickers they would like to get more info on. The MarketAUX API grabs 3 news stories that mention the selected ticker, and combines it with the FMP data to give the user insight into the ticker being discussed on WSB.  

## Installation  
1. Clone the repository  
2. Get free API keys for [Financial Modeling Prep](https://site.financialmodelingprep.com/) and [MarketAUX](https://www.marketaux.com/register)  
3. Navigate to project directory  
4. Install dependencies (ex: pip install -r requirements.txt)  
5. Either:  
  - A. Put your keys on your local system so they can be accessed by:  
    - fmp_key = os.environ.get("FMP_API_KEY")
    - marketaux_key = os.environ.get("MARKETAUX_API_KEY")  
  - B. Edit main.py and put your keys directly in the code  
6. Run main.py  


## Minimum Viable Product:  
- gets WSB top sentiment API ticker symbols, display number of comments that mention it and if they are bullish/bearish  
- gets current stock price for each ticker (using a TDB stock market API)  
- show ticker market cap, other info about the company (founded date, industry, etc)  
- get top news stories (from a news API) related to each ticker and offers them  


## Additional ideas for this project:   
- - gets stock price for 1 month(and/or week?) ago, gives difference between current and 1 mon(and/or week) ago  
- use openai api to get a short description of the company  
- shows what $n invested one month(and/or week) ago would be worth today  
- show some sort of options interest?  
- show volume  
- GUI (PyQt or PySimpleGUI)  
- charts  


## APIs Being Used    
- Wall Street Bets API  
  * https://tradestie.com/apps/reddit/api/  
- MarketAux API (For news)  
  * https://www.marketaux.com/documentation  
- Financial Modeling Prep (For stock info)  
  * https://site.financialmodelingprep.com/developer/docs  
# Wall Street Bets Insights Dashboard


**Minimum Viable Product:**  
- gets WSB top sentiment API ticker symbols, display number of comments that mention it and if they are bullish/bearish  
- gets current stock price for each ticker (using a TDB stock market API)  
- show ticker market cap, other info about the company (founded date, industry, etc)  
- get top news stories (from a news API) related to each ticker and offers them  


**Additional ideas for this project:**   
- - gets stock price for 1 month(and/or week?) ago, gives difference between current and 1 mon(and/or week) ago  
- use openai api to get a short description of the company  
- shows what $n invested one month(and/or week) ago would be worth today  
- show some sort of options interest?  
- show volume  
- GUI (PyQt or PySimpleGUI)  
- charts  


**APIs Being Used**  
- Wall Street Bets API  
  * https://tradestie.com/apps/reddit/api/  
- MarketAux API (For news)  
  * https://www.marketaux.com/documentation  
- Financial Modeling Prep (For stock info)  
  * https://site.financialmodelingprep.com/developer/docs  
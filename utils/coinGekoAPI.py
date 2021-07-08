import requests
import pandas as pd
from pycoingecko import CoinGeckoAPI

class geckoAPI():
    
    def __init__(self):
        self.cg   = CoinGeckoAPI()
        
    def getTokenDataFromTicker(self,ticker):
        return self.cg.get_price(ids=ticker, vs_currencies='usd',include_market_cap='true')
            

    def getTokenDataFromTickers(self,tickersDict):
    
        result = {key: self.getTokenDataFromTicker(tickersDict[key]["id"]) for key in tickersDict.keys()}
                
        #convert to pandas
        df = pd.DataFrame.from_dict({i: result[i][j] 
                                     for i in result.keys() 
                                     for j in result[i].keys()},
                                    orient='index')

                
        if len(df) != len(tickersDict):
            print("tickers found")
            print(df.to_markdown())
            raise NotImplementedError('Some tickers were not found, please check if id were properly incorporated as tickers')
            
        return df

    def getTokenIDFromTicker(self,ticker):
        #Helper function to find ids using ticker
        url  = 'https://api.coingecko.com/api/v3/coins/list?include_platform=true'
        coinList = requests.get(url).json()
        #Convert to df
        df          = pd.DataFrame(coinList)
        df          = df[df.symbol.str.contains(ticker)]
        df["cap"]   = df["id"].apply(self.getTokenDataFromTicker)
        df["price"] = df.apply(lambda x: x["cap"][x["id"]]["usd"],axis=1)
        df["cap"]   = df.apply(lambda x: x["cap"][x["id"]]["usd_market_cap"],axis=1)
        df          = df[['id','symbol','name',"cap","price"]]
        print(df.to_markdown(index=False))
                
#%%
if __name__ == '__main__':
    gecko = geckoAPI()
    self = gecko

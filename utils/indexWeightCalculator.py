import pandas as pd
from utils.coinGekoAPI import geckoAPI

class calculator(geckoAPI):
    
    def __init__(self):
        super().__init__()
    
    def compute(self,tickersDict):

        dfCap = self.getTokenDataFromTickers(tickersDict)
        
        dfTickers = pd.DataFrame.from_dict({i: tickersDict[i] 
                                            for i in tickersDict.keys()
                                            },
                                           orient='index')
        
        df = pd.concat([dfCap,dfTickers],
                       ignore_index=True,
                       axis=1)
        df.columns = ['price','cap','name','concentration']
        
        df["value"] = df["concentration"] * 1000
        df["units"] = df["value"] / df["price"]
        
        df.to_csv(r'output\output.csv')
                
#%%
if __name__ == '__main__':
    calc = calculator()
    self = calc

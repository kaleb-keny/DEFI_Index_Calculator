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
        
        df["units"] = df["concentration"] * 1000 / df["price"]
                
        df.to_csv(r'output\output.csv')
            
        
    def getDefiIndexPrice(self):
        df = pd.read_html('https://www.synthetix-monitoring.com/')[0]
        df = df.query('Synth == "sDEFI"').copy()
        return df.Price.values[0]
        
                
#%%
if __name__ == '__main__':
    calc = calculator()
    self = calc

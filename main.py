from utils.utility import parse_config
from utils.indexWeightCalculator import calculator
tickersDict = parse_config(r"config/tickers.yaml")

#%%Arg Parse
if __name__ == '__main__':
    calc = calculator()
    calc.compute(tickersDict)
    print("Output saved successfully in output folder")

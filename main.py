from utils.utility import parse_config
from utils.indexWeightCalculator import calculator
import argparse
tickersDict = parse_config(r"config/tickers.yaml")


#%%Arg Parse
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Computes the weights of defi/cefi index')

    parser.add_argument("-r",
                        type=str,
                        required=True,
                        choices=["weights","ticker"],
                        help=''''Please choose between:
                                    - 'weights', to compute the weights
                                    - 'ticker', to retrieve ticker related information which needs to be incorporated under tickers.yaml as `id`''')
                        
    parser.add_argument("--t",
                        type=str,
                        required=False,
                        help=''''Please enter the ticker''')
                        
    
    args = parser.parse_args()
    calc = calculator()

    if args.r == 'weights':

        calc.compute(tickersDict)
        print("Output saved successfully in output folder")

    elif args.r =='ticker':
        if not args.t:
            parser.error('''Need to specify the ticker''')
        
        calc.getTokenIDFromTicker(args.t)
        
    else:
        print("invalid arg")

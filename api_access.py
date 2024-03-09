#Project imports

import requests


## Main

# Check if given ticker symbol points to a real stock 
def check_stock(ticker):
    return

def get_data_from_api(time_series, ticker):

    #time_series must be one of these four:
    # - TIME_SERIES_INTRA
    # - TIME_SERIES_DAILY
    # - TIME_SERIES_WEEKLY
    # - TIME_SERIES_MONTHLY  

    url = 'https://www.alphavantage.co/query?function=' + time_series + '&symbol=' + ticker + '&interval=60min0&apikey=JLFXYX4J4I20CF8E'
    r = requests.get(url)
    data = r.json()

    print(data)
    
    # #Proof of concept 

    # url = ""

    # # Make API request 
    # response = requests.get()

get_data_from_api()
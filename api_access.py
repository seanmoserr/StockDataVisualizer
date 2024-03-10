#Project imports
import requests


## Main

# Check if given ticker symbol points to a real stock 
def check_stock(ticker):

    response = requests.get(url='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=5min&apikey=JLFXYX4J4I20CF8E')
    data = response.json()

    if 'Error Message' in data:
        print("It does not seem that this ticker symbol points to an existing stock. Please try again")
    else: 
        print('The ticker symbol ' + ticker + ' is valid')
        print(data)
        return ticker


def get_data_from_api(time_series, ticker):

    #time_series must be one of these four:
    # - TIME_SERIES_INTRADAY
    # - TIME_SERIES_DAILY
    # - TIME_SERIES_WEEKLY
    # - TIME_SERIES_MONTHLY  

    url = 'https://www.alphavantage.co/query?function=' + time_series + '&symbol=' + ticker + '&interval=5min&apikey=JLFXYX4J4I20CF8E'

    r = requests.get(url)
    data = r.json()

    print(data)


# get_data_from_api('TIME_SERIES_INTRADAY', 'IB')
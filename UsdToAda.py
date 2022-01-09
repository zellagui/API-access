from requests import Request, Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start':'1',
    'limit':'10',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '52da5bee-2bbc-49e0-b837-9544f2cacc60',
}

delevery_cost = 20 #delevery cost

session = Session()
session.headers.update(headers)

def get_price_ADA_USD(delevery_cost):
    #Get method to access Data
    response = session.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)
    crypto = data["data"]
    #Looping through all crypto to extract ADA Then the price in quote/usd
    for x in crypto:
        if x['symbol'] == 'ADA':
            price = x['quote']['USD']['price']
    return round(delevery_cost / price, 2)

print(get_price_ADA_USD(delevery_cost), 'ADA')

    

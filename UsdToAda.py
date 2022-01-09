from requests import Request, Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'

parameters = {
    'amount':1,
    'id':'2010'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '52da5bee-2bbc-49e0-b837-9544f2cacc60',
}

session = Session()
session.headers.update(headers)

delivery_cost = 15 #delevery cost


#Get delivery cost in USD as parameter and return delivery const in ADA
def get_ADA_conv(delivery_cost):
    response = session.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)
    crypto = data["data"]['quote']['USD']['price']
    cost_in_ADA =  round(delivery_cost / crypto, 2)
    return cost_in_ADA

try:
    #Printing the the result
    print(get_ADA_conv(delivery_cost), 'ADA')

except requests.exceptions.Timeout:
    print('An error occurred')
except requests.exceptions.TooManyRedirects:
    print('An error occurred')
except requests.exceptions.RequestException as e:
    raise SystemExit(e)




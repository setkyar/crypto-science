# Getting crypto currency price from Coingecko
# https://www.coingecko.com/en/api

# Todo:: Improve by asking ids and currency via command

import requests
import json

data = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=USD", headers={"accept":"application/json"})
price = data.json()['bitcoin']['usd']

print("The price of Bitcoin is currently {} USD!".format(price))
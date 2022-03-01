import requests
from datetime import datetime, timedelta

#========================== INITIALIZE VARIABLE ==========================#
etherscan_priceETH = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def request_json(url):
    return (requests.get(url).json())

def get_yesterday_date():
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, '%Y-%m-%d')

def get_price_eth():
    rsp = float(request_json(etherscan_priceETH)['result']['ethusd'])
    return (rsp)

def get_localtime():
    current_time = datetime.now()
    return (current_time)

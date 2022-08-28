import re
import requests
from datetime import datetime, timedelta

#========================== INITIALIZE VARIABLE ==========================#
etherscan_priceETH = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def request_json(url):
    try:
        rsp = requests.get(url)
        return(rsp.json())
    except requests.exceptions.ConnectionError:
        return (None)

def get_yesterday_date():
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, '%Y-%m-%d')

def get_price_eth() -> float:
    rsp = request_json(etherscan_priceETH)
    if (rsp != None and rsp['status'] != '0'):
        return ((float)(rsp['result']['ethusd']))
    else:
        return (0)

def get_localtime():
    current_time = datetime.now()
    return (current_time)

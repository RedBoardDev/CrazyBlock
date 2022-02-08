import requests
from datetime import datetime, timedelta

def get_mhs_hiveos(url1, hiveToken):
    mhs_hiveos = 0
    reponse = requests.get(url1, headers={'Authorization': 'Bearer ' + hiveToken}, params="period=1d").json()['data'][-1]['hashrates']
    for i in range(len(reponse)):
        if(reponse[i]['algo'] == "ethash"):
            rsp3 = reponse[i]['values']
            for i in range(len(rsp3)):
                mhs_hiveos = mhs_hiveos + rsp3[i]/1000000
    return round(mhs_hiveos, 2)

def get_yesterday_date():
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, '%Y-%m-%d')

def get_last_gain_crazy(get_yesterday_date, crazy_request): # A REFAIRE
    for i in range(len(crazy_request['paymentCharts'])):
        if(crazy_request['paymentCharts'][i]['timeFormat'] == get_yesterday_date):
            return crazy_request['paymentCharts'][i]['amount']/1000000000
    else:
        return crazy_request['paymentCharts'][-2]['amount']/1000000000

def get_balance(crazy_request):
    reponse = crazy_request['stats']['balance']
    return(reponse / 1000000000)

def get_status_rig(url2, hiveToken):
    reponse = requests.get(url2, headers={'Authorization': 'Bearer ' + hiveToken}, params="period=1d").json()['data'][-1]['stats']
    online:bool = reponse['online']
    gpus_offline:int = reponse['gpus_offline']
    if (online == False):
        return (-1)
    elif (gpus_offline > 0):
        return(gpus_offline)
    else:
        return (0)

def get_status_temp(url1, hiveToken, tempLimit):
    reponse = requests.get(url1, headers={'Authorization': 'Bearer ' + hiveToken}, params="period=1d").json()['data'][-1]['temp']
    for i in range(len(reponse)):
        if (reponse[i] > tempLimit): return (i)
    return (-1)

def get_price_eth(etherscan_priceETH):
    rsp = float(requests.get(etherscan_priceETH).json()['result']['ethusd'])
    return (rsp)

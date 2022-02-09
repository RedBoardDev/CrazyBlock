import requests

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

import requests
import time
from datetime import datetime, timedelta
from datetime import date
from requests.api import request
from requests.models import Response
from get_info import *

#========================== INITIALIZE VARIABLE ==========================#
url0 = 'https://eth.crazypool.org/api/accounts/0xb35ff0343da28525fCE4BD49308920f2B8f7bEd4'
url1 = 'https://api2.hiveos.farm/api/v2/farms/776169/workers/1669282/metrics'
url2 = 'https://api2.hiveos.farm/api/v2/farms/776169/workers'
hiveToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkiLCJpYXQiOjE2Mjg3OTQ3NjksImV4cCI6MTk0NDE1NDc2OSwibmJmIjoxNjI4Nzk0NzY5LCJqdGkiOjM5Njc1MDc0LCJzdWIiOjM5Njc1MDc0fQ.QwcvWJdodnvt9ZD9NkwPpFTiF7Yo_WFd2BUyZA-4R0Y"
tempLimit = 48

#========================== FUNCTION ==========================#

# balance = get_balance(url0)
# gain_yesterday = get_last_gain_crazy(get_yesterday_date(), url0)
#calcul moyenne total
# status_rig = get_status_rig(url2, hiveToken)
# status_temp = get_status_temp(url1, hiveToken, tempLimit)

def get_localtime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return (current_time)

def send_info():
    crazy_request = requests.get(url0).json()
    balance = get_balance(crazy_request)
    gain_yesterday = get_last_gain_crazy(get_yesterday_date(), crazy_request)
    # add to the list in data.py -> rewards
    # calcul moyenne total with data.py -> rewards

#========================== MAIN ==========================#

while (True):
    if (get_localtime() >= '00:30'):
        send_info()
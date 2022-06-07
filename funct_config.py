import json
import orjson

def f_set_height(height:int):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    data['last_height'] = height
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_get_height() -> int:
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['last_height'])

def f_set_tx(tx_code:str):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    data['last_tx'] = tx_code
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_get_tx() -> str:
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['last_tx'])

def f_get_account():
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['account'])

def f_add_account(wallet:str, channel, role_id):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    node = {}
    node['channel'] = channel
    node['role_id'] = role_id
    node['wallet'] = wallet
    node['currency'] = 'USD'
    node['settings'] = {"blocks": True, "payments": True}
    data['account'].append(node)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_remove_account(wallet:str):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    for i, node in enumerate(data["account"]):
        if wallet == node["wallet"]:
            del data["account"][i]
            break
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_find_index_account(wallet:str) -> int:
    with open('data.json', 'r') as file:
        data1 = orjson.loads(file.read())
        data = data1['account']
    for x in range(len(data)):
        if (data[x]['wallet'] == wallet):
            return (x)
    return (None)

def f_modify_account(wallet:str, channel, role_id):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    node = f_find_account(wallet)
    node['channel'] = channel
    node['role_id'] = role_id
    node['wallet'] = wallet
    data['account'][f_find_index_account(wallet)] = node
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_find_account(wallet:str):
    with open('data.json', 'r') as file:
        data1 = orjson.loads(file.read())
        data = data1['account']
    if (len(data) == 0):
        return (None)
    for x in range(len(data)):
        if (data[x]['wallet'] == wallet):
            return (data[x])
    return (None)

def f_set_flags_settings(wallet:str, param:str, flags:bool):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    settings = f_find_account(wallet)['settings']
    for x in settings:
        if (x == param):
            settings[param] = flags
    data['account'][f_find_index_account(wallet)]['settings'] = settings
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_set_currency(wallet:str, currency:str) -> int:
    if (currency == 'USD' or currency == 'EUR'):
        with open('data.json', 'r') as file:
            data = orjson.loads(file.read())
        data['account'][f_find_index_account(wallet)]['currency'] = currency
        with open('data.json', 'w') as file:
            json.dump(data, file, indent = 4)
        return (1)
    return (0)

def f_get_currency(wallet:str) -> str:
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    currency = data['account'][f_find_index_account(wallet)]['currency']
    return (currency)

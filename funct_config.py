import json
import orjson

def f_set_height(height):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    data['last_height'] = height
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_get_height():
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['last_height'])

def f_set_tx(height):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    data['last_tx'] = height
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_get_tx():
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['last_tx'])

def f_get_tempLimit():
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['tempLimit'])

def f_get_account():
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['account'])

def f_add_account(wallet, round_share, channel, role_id):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    node = {}
    node['channel'] = channel
    node['role_id'] = role_id
    node['round_share'] = round_share
    node['wallet'] = wallet
    node['settings'] = {"blocks": True, "payments": True}
    data['account'].append(node)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_find_index_account(wallet):
    with open('data.json', 'r') as file:
        data1 = orjson.loads(file.read())
        data = data1['account']
    for x in range(len(data)):
        if (data[x]['wallet'] == wallet):
            return (x)
    return (None)

def f_modify_account(wallet, round_share, channel, role_id):
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    node = f_find_account(wallet)
    node['channel'] = channel
    node['role_id'] = role_id
    node['round_share'] = round_share
    node['wallet'] = wallet
    data['account'][f_find_index_account(wallet)] = node
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_find_account(wallet):
    with open('data.json', 'r') as file:
        data1 = orjson.loads(file.read())
        data = data1['account']
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

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

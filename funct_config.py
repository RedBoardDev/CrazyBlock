import yaml

def f_set_height(height):
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)
    data['last_height'] = height
    with open('config.yml', 'w') as file:
        yaml.dump(data, file)

def f_get_height():
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)
    return(data['last_height'])

def f_get_tempLimit():
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)
    return(data['tempLimit'])

def f_get_account():
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)
    return(data['account'])

def f_add_account(wallet, round_share, channel, role_id):
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)
    nb_account = len(data['account'])

    node = {}
    node['channel'] = channel
    node['role_id'] = role_id
    node['round_share'] = round_share
    node['wallet'] = wallet

    data['account'][nb_account] = node
    with open('config.yml', 'w') as file:
        yaml.dump(data, file)

def f_find_index_account(wallet):
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)['account']
    for x in range(len(data)):
        if (data[x]['wallet'] == wallet):
            return (x)
    return (None)

def f_modify_account(wallet, round_share, channel, role_id):
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)
    node = f_find_account(wallet)
    node['channel'] = channel
    node['role_id'] = role_id
    node['round_share'] = round_share
    node['wallet'] = wallet
    data['account'][f_find_index_account(wallet)] = node
    with open('config.yml', 'w') as file:
        yaml.dump(data, file)

def f_find_account(wallet):
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)['account']
    for x in range(len(data)):
        if (data[x]['wallet'] == wallet):
            return (data[x])
    return (None)

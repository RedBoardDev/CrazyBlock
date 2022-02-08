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

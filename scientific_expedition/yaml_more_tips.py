import re

def yaml(a):
    yaml_dict = {}
    for el in a.split('\n'):
        if el != '':
            key, value = el.split(':')
            value = value.lstrip(' ')
            if (value == '') or (value == None) or (value == 'null'):
                yaml_dict[key] = None
            elif (value.lower() in ['true', 'false']):
                yaml_dict[key] = True if value.lower() == 'true' else False
            elif (re.search(r'[a-zA-Z]+', value)):
                value = re.sub(r'\\"', r'"', value)
                try:                    
                    value = re.search(r'\"([\w\W]*)\"', value).group(1)
                    yaml_dict[key] = value
                except AttributeError:
                    yaml_dict[key] = value
            else:
                yaml_dict[key] = int(value)
    return yaml_dict
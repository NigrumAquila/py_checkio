def Capital(name):
    if not hasattr(Capital,'name'):
        Capital.name=lambda:name
    return Capital
def turn90(key):
    return [''.join([line[::-1][i] for line in key])for i in range(len(key[0]))]if key else[]

def trim(key):
    for n in range(4):
        while key and not '#' in key[0]: key = key[1:]
        key = turn90(key)
    return key
    
def keys_and_locks(lock, key):
    lock, key = trim(lock.split()), trim(key.split())
    for n in range(4):
        if lock == key: break
        key = turn90(key)
    return lock == key
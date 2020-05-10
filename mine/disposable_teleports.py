def checkio(teleports_string):
    ports = [set(port) for port in teleports_string.split(',')]
    
    def find(stat, route, ports):
        if set(route) == set('12345678') and stat == '1': return route + '1'
        avail = [port for port in ports if stat in port]
        if not avail: return False
        for port in  avail:
            dest = (port - {stat}).pop()
            togo = find(dest, route + stat, [p for p in ports if p != port])
            if togo: return togo
        return False
    
    avail = [port for port in ports if '1' in port]
    for port in  avail:
         dest = (port - {'1'}).pop()
         route = find(dest, '1', [p for p in ports if p != port])
         if route: return route
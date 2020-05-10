from collections import deque

def disconnected_users(net, users, source, crushes):
    net = [set(connection) for connection in net]
    result = set.union(*net)
    seen = set()
    q = deque([source])
    # BFS
    while q:
        node = q.popleft()
        if node in seen: continue
        seen.add(node)
        if node not in crushes:
            result -= {node}
            q.extend([(r - {node}).pop() for r in net if node in r])
    return sum(users[node] for node in result)
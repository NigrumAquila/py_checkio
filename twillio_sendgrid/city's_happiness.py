def most_crucial(net, users):
    def DFS_visit(G, u):
        visited.add(u)
        sub_net.add(u)
        for v in G[u]:
            if v not in visited:
                DFS_visit(G, v)
    
    G = {u:set() for u in users}
    for u, v in net:
        G[u].add(v)
        G[v].add(u)
    happiness = dict(users)
    for u in users:
        visited = {u}
        for v in users:
            if v not in visited:
                sub_net = set()
                DFS_visit(G, v)
                happiness[u] += sum(users[w] for w in sub_net) ** 2
    min_happiness = min(happiness.values())
    return [u for u in users if happiness[u] == min_happiness]
from typing import Set, Tuple, List, Dict
from heapq import heappop,heappush

def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    plants=tuple(sorted(ranges,reverse=True))
    
    nodes=set()
    for link in network:
        nodes.update(set(link))
    
    dist={(i,j):0 if i==j else float("inf") for i in nodes for j in nodes}
    for s,e in network:
        dist[(s,e)]=1
        dist[(e,s)]=1
        
    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[(i,j)]=min(dist[(i,j)],dist[(i,k)]+dist[(k,j)])
    
    first=(left,used,cities,plants)=(len(nodes),(),tuple(nodes),plants)
    que=[first]
    while que:
        left,used,cities,plants=heappop(que)
        if plants==() and cities!=():
            continue
        if not cities:
            return {k:v for k,v in used}
            
        for node_s in nodes-{x[0] for x in used}:
            next_used=used+((node_s,plants[0]),)
            next_cities=set(cities)
            for node_t in cities:
                if dist[(node_s,node_t)]<=plants[0]:
                    next_cities.remove(node_t)
            next_cities=tuple(next_cities)
            heappush(que,(len(next_cities),next_used,next_cities,plants[1:]))
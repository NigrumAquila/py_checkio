def hypercube(grid):
    h,w,code=len(grid),len(grid[0]),"hypercube"    
    res,paths=[],[]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x].lower() in code:
                res.append([y,x,grid[y][x].lower()])    
    for j in range(len(code)):        
        for elem in res:
            work=paths[:]
            if elem[2]==code[j]:
                if j==0:
                    paths+=[[[elem[0],elem[1],elem[2]]]]                    
                    continue
                else:
                    for path in work:
                        if path[-1][2]==code[j-1] and (abs(path[-1][0]-elem[0]) + abs(path[-1][1]-elem[1]))==1:                            
                            path.append(elem)                            
                            paths.append(path)
    return False if all([len(path)!=len(code) for path in paths]) else True
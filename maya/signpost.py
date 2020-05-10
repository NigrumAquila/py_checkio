vectors = { 'NW': (-1, -1), 'N': (-1, 0), 'NE': (-1, 1),
            'W' : ( 0, -1), '' : ( 0, 0), 'E' : ( 0, 1),
            'SW': ( 1, -1), 'S': ( 1, 0), 'SE': ( 1, 1),
          }
          
class Board:
    
    def __init__(self,grid,directions):
        self._nb_row,self._nb_col=(len(grid),len(grid[0]))
        self._size=max(self._nb_row,self._nb_col)
        self._final=self._nb_row*self._nb_col
        self._successors=dict()
        self._predecessors=dict()
        self._values=dict()
        self._positions=dict()

        positions=[(x,y) for x in range(self._nb_row) for y in range(self._nb_col)]                
        self._next={pos:None for pos in positions}
        self._before={pos:None for pos in positions}
        self._possible_next={pos:[] for pos in positions}
        self._possible_before={pos:[] for pos in positions}
        self._positions={val:None for val in range(1,self._final)}
        self._values={pos:0 for pos in positions}
        
        for x, row in enumerate(grid):
            for y,val in enumerate(row):
                M=(x,y)
                if val!=0:
                    self._positions[val]=M
                    self._values[M]=val
                if val==1:
                    self._start=M
                if val==self._final:
                    self._end=M
   
        for x in range(self._nb_row):
            for y in range(self._nb_col):
                dx,dy=vectors[directions[x][y]]
                for n in range(1,self._size):
                    if 0<=x+n*dx<self._nb_row and 0<=y+n*dy<self._nb_col:
                        if (x+n*dx,y+n*dy)!=self._start and (x,y)!=self._end:
                            self._possible_next[(x,y)].append((x+n*dx,y+n*dy))
                            self._possible_before[(x+n*dx,y+n*dy)].append((x,y))

    def _link(self,B,C):

        # Actually Link B to C
        self._next[B]=C
        self._before[C]=B
        # Remove B and C as options for other links
        for A in self._possible_next[B]:
            self._possible_before[A].remove(B)
        self._possible_next[B]=[]

        for A in self._possible_before[C]:
            self._possible_next[A].remove(C)
        self._possible_before[C]=[]
        
        # Let see if we learned some values
        if self._values[B] and not self._values[C]:
            val=self._values[B]
            prev_pos=B
            while self._next[B] and not self._values[self._next[B]]:
                val+=1
                next_pos=self._next[B]
                self._values[next_pos]=val
                self._positions[val]=next_pos
                prev_pos=next_pos
            # Check if we know where val+1 is
            if self._positions[val+1]:
                self._link(next_pos,self._positions[val+1])

        elif self._values[C] and not self._values[B]:
            val=self._values[C]
            next_pos=C
            while self._before[C] and not self._values[self._before[C]]:
                val-=1
                prev_pos=self._before[C]
                self._values[prev_pos]=val
                self._positions[val]=prev_pos
                next_pos=prev_pos
            # Check if we know where val-1 is
            if self._positions[val-1]:
                self._link(self._positions[val-1],next_pos)

    def _paths(self,start,stop):
        A,B=self._positions[start],self._positions[stop]
        paths=[[A]] # All paths start at A
        length=stop-start
        current_pos=A
        for _ in range(length-1):
            # We want to stop just before last step (as we will control that all positions in path are empty
            next_paths=[]
            for path in paths:
                last_pos=path[-1]
                next_pos=self._next[last_pos]
                if next_pos:
                    if not self._values[next_pos] and next_pos not in path:
                        # If next_pos already has a value, it can not be a valid path
                        # loops are not possible too
                        next_paths.append(path+[next_pos])
                else:
                    for next_pos in self._possible_next[last_pos]:
                        if not self._values[next_pos] and not next_pos in path:
                            # If next_pos already has a value, it can not be a valid path
                            # loops are not possible too
                            next_paths.append(path+[next_pos])
            paths=next_paths
        # We reach the end, time to remove any path that won't terminate in B
        next_paths=[]
        for path in paths:
            last_pos=path[-1]
            next_pos=self._next[last_pos]
            if B==next_pos or B in self._possible_next[last_pos]:
                # This terminate in B
                next_paths.append(path+[B])
        # We are done
        paths=next_paths
        if len(paths)>1:
            return []
        else:
            return paths[0]
        
    def solve(self):
        # Linking pairs of numbers first
        numbers=[n for n,v in self._positions.items() if v]
        pairs=[(n-1,n) for n in numbers if n-1 in numbers]
        for p,n in pairs:
            self._link(self._positions[p],self._positions[n])

        # Start a loop until all positions have a defined value   
        while not all(self._positions.values()):
            for pos,successor in [(pos,possible_next[0])
                                  for pos,possible_next in self._possible_next.items()
                                  if possible_next and len(possible_next)==1]:
                # Only one successor
                self._link(pos,successor)

            for pos,predecessor in [(pos,possible_before[0])
                                    for pos,possible_before in self._possible_before.items()
                                    if possible_before and len(possible_before)==1]:
                # Only one predecessor
                self._link(predecessor,pos)

            # Let's search for paths between numbers with smallest gap
            numbers=[n for n,v in self._positions.items() if v]
            gaps=[(numbers[i-1],n) for i,n in enumerate(numbers) if i>0 and n-numbers[i-1]>1]
            distances=sorted([stop-start for start,stop in gaps])
            for limit in distances:
                paths=[path for path in [self._paths(start,stop) for start,stop in gaps if stop-start==limit] if path]
                if paths:
                    # At Least one valid path, time to stop, else continue with longer paths
                    break

            # We have a valid path
            for path in paths:
                for prev_pos,next_pos in zip(path[:-1],path[1:]):
                    val=self._values[prev_pos]+1
                    self._values[next_pos]=val
                    self._positions[val]=next_pos
                    self._link(prev_pos,next_pos)

        # End of while loop, hopefully we are done
        return [[self._values[(x,y)] if (x,y) in self._values else 0 for y in range(self._nb_col)] for x in range(self._nb_row)]

def signpost(grid, directions):
    return Board(grid,directions).solve()
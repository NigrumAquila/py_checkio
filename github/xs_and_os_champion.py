import copy

class Board:
    def __init__(self,initial_grid,next_to_move,depth):
        self.grid = initial_grid
        self.next_to_move = next_to_move
        self.depth = depth
        strength_cur = self.find_strength()
        if strength_cur != 0 or depth >= 3:
            self.bestMove,self.strength = None,strength_cur
        else:
            childrenDict = self.create_children()
            if len(childrenDict) == 0:
                self.bestMove,self.strength = None,0
            elif next_to_move == "X":  # If X's turn then the aim is to max
                self.bestMove = max(childrenDict,key=lambda x:childrenDict[x].strength)
                self.strength = childrenDict[self.bestMove].strength
            else:
                self.bestMove = min(childrenDict,key=lambda x:childrenDict[x].strength)
                global Y; Y  = childrenDict
                self.strength = childrenDict[self.bestMove].strength

                
    def find_strength(self) -> int:
        A,has_winning_line = self.grid,{"X":False,"O":False}
        for c in ["X","O"]:
            if any(all(A[R][C] == c for R in range(3)) for C in range(3)): has_winning_line[c] = True
            if any(all(A[R][C] == c for C in range(3)) for R in range(3)): has_winning_line[c] = True
            if all(A[R][R] == c for R in range(3)): has_winning_line[c] = True
            if all(A[R][2-R] == c for R in range(3)): has_winning_line[c] = True
        if   has_winning_line["X"] and not has_winning_line["O"]: return  1
        elif has_winning_line["O"] and not has_winning_line["X"]: return -1
        else:                                                     return  0

    def create_children(self) -> dict:
        childrenDict = {}
        for R,C in [(R,C) for R in range(3) for C in range(3)]:
            if self.grid[R][C] != ".": continue
            grid_new = copy.deepcopy(self.grid)
            grid_new[R][C] = self.next_to_move
            next_to_move_new = "XO"[self.next_to_move == "X"]
            depth_new = self.depth + 1
            board_new = Board(grid_new,next_to_move_new,depth_new)
            childrenDict[(R,C)] = board_new
        return childrenDict


x_and_o=lambda grid,mark:Board([list(row) for row in grid],mark,0).bestMove
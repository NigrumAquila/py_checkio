from collections import namedtuple

def checkio(house, stephan, ghost):
    if stephan == 1:
        return 'N' # that was easy
   
    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    def possible_moves(pos):
        return {direction: pos + DIRS[direction]
                for direction in DIRS if not(
                direction == 'N' and pos in (1, 2, 3, 4) or
                direction == 'S' and pos in (13, 14, 15, 16) or
                direction == 'E' and pos in (4, 8, 12, 16) or
                direction == 'W' and pos in (1, 5, 9, 13) or
                direction in house[pos - 1])}

    def ghost_moves(stephan_pos, ghost_pos):
        all_moves = possible_moves(ghost_pos)
        if len(all_moves) > 1:
            sx, sy = (stephan_pos - 1) % 4, (stephan_pos - 1) // 4
            min_moves, min_dist = {}, 1000
            for g_dir, g_pos in all_moves.items():
                gx, gy = (g_pos - 1) % 4, (g_pos - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if min_dist > dist:
                    min_moves, min_dist = [g_pos], dist
                elif min_dist == dist:
                    min_moves += [g_pos]
            return min_moves
        return all_moves.values()

    # state = 'W'/'L'/'U'/'E'

    class Ghost(object):
        __slots__ = ('pos', 'stephans')
        
        def __init__(self, pos, stephans):
            self.pos = pos
            self.stephans = stephans

    class Stephan(object):
        __slots__ = ('direction', 'pos', '_state', 'ghosts')
        
        def __init__(self, direction, pos, ghost_pos=None):
            self.direction = direction
            self.pos = pos
            if ghost_pos is None:
                self.ghosts = None
                self.state = None
            else:
                self._fill(ghost_pos)

        @property
        def state(self):
            return self._state
        
        @state.setter
        def state(self, value):
            self._state = value
            if value is not None and value in 'WL':
                self.ghosts = None

        def add_step(self):
            if self.state == 'U':
                new_moves = possible_moves(self.pos)
                for ghost in self.ghosts:
                    ghost.stephans = [Stephan(new_dir, new_pos, ghost.pos)
                                      for new_dir, new_pos in new_moves.items()]

        def _fill(self, ghost_pos):
            self.ghosts = [Ghost(move, None) for move in ghost_moves(self.pos, ghost_pos)]
            if self.pos == self.ghosts[0].pos:
                self.state = 'L'
            elif self.pos == 1:
                self.state = 'W'
            else:
                self.state = 'U'

        def expand(self):
            if self.state == 'U':
                if any(ghost.stephans is None for ghost in self.ghosts):
                    self.add_step()
                else:
                    for ghost in self.ghosts:
                        for stephan in ghost.stephans:
                            stephan.expand()
                all_win = True
                has_all_loose = False
                for ghost in self.ghosts:
                    has_win = False
                    if all(stephan.state == 'L' for stephan in ghost.stephans):
                        has_all_loose = True
                    if any(stephan.state == 'W' for stephan in ghost.stephans):
                        has_win = True
                    if not has_win:
                        all_win = False
                if has_all_loose:
                    self.state = 'L'
                elif all_win:
                    self.state = 'W'

    first_moves = [Stephan(direction, pos, ghost) for direction, pos in possible_moves(stephan).items()]
    while True:
        stephan = first_moves.pop()
        if not first_moves or stephan.state == 'W':
            return stephan.direction
        if stephan.state != 'L':
            stephan.expand()
            first_moves.insert(0, stephan)
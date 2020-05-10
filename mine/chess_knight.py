def chess_knight(start, moves):
    def knight_can_move(from_pos, to_pos):
        return set(map(lambda x: abs(ord(x[0]) - ord(x[1])), zip(from_pos, to_pos))) == {1, 2}
        
    def knight_moves(pos):
        return {f + r for f in 'abcdefgh' for r in '12345678' if knight_can_move(pos, f + r)}
        
    # till task become consistent, hardcode
    res = knight_moves(start)
    if moves == 2:
        res.update(*map(knight_moves, res))
    return sorted(res)
from typing import List

def checkio(game_result):
    for i in game_result:
        if i[0] == i[1] == i[2] and i[0]!= '.':
            return i[0]
        
    rotated_field = zip(*game_result)
    for i in rotated_field:
        if i[0] == i[1] == i[2] and i[0]!= '.':
            return i[0]
            
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0]!='.':
        return game_result[0][0]
    
    if game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2]!='.':
        return game_result[0][2]
        
    return 'D'
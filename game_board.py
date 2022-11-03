
#create an empty board
game_board = {'1': ' ' , '2': ' ' , '3': ' ' ,           
              '4': ' ' , '5': ' ' , '6': ' ' ,
              '7': ' ' , '8': ' ' , '9': ' ' }

#saving dictionary keys into the list form and printing
board_keys = []

for key in game_board:
    
    board_keys.append(key)
print(board_keys)

def display_board():
    '''
Defined game board using dictionary with keys as numbers ranging from 1 to 9 represented by blank spaces.
Print the game board 
    '''
    print(game_board['1'] + '|'+ game_board['2'] + '|' + game_board['3'])
    print('-+-+-')
    print(game_board['4'] + '|' + game_board['5'] + '|' + game_board['6'])
    print('-+-+-')
    print(game_board['7'] + '|' + game_board['8'] + '|' + game_board['9'])


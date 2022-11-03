
#importing the game board conveniently as gb
import game_board as gb


def handle_turn(turns):
    '''
Handle turn function used to handle the turns.
Take input from the user.
Print errors if the input value is not in the defined range.  
    '''

    #taking input from user
    position = input("choose a position from the list of numbers:")

    #using error handling to figure out errors
    try:
        #checking whether given input lies between (0,10) 
        0<int(position)<=9

        #checking whether the place is filled by X or O
        if gb.game_board[position] == ' ':

            #if turns is even then it prints X
            if turns%2==0:
                gb.game_board[position] = "X"

            #if turns is odd then it prints O
            else:
                gb.game_board[position] = "O"
            gb.display_board()
        
        #if the same input is given,ask to give another input which is not filled   
        else:
            print("number is already repeated please choose another number")
            handle_turn(turns)
        
    #if given input is out of range    
    except:
        print("an error has occured choose a number between 1 and 9")
        handle_turn(turns)




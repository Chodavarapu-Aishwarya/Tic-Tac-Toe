                #title : tic - tac - toe game
                #the overall code is written by all the team members equally

print("start the game")

#importing handle_turn function
import handle_turn as ht

#importing game_board function
import game_board as gb

#importing date and time
import datetime

#time stores the date and time when they are playing
time_and_date = datetime.datetime.now()



#initial number of games is one
no_of_games=1



#defining a function to initialize the game
def play_game(no_of_games):        
    '''
Play game function used to play the entire game.
Take the winning conditions through all possible ways (across the horizonatl, vertical and diagonal).
Print the winner'''
    
    # to display the empty board
    gb.display_board()
    turns=0

    #using while loop to iterate the turns
    while turns<9:
        ht.handle_turn(turns)
        
        #iteration condition
        turns+=1

        #checking winning condition from the 5th move since wiining condition is not possible for less than 5 moves
        if turns >= 5:
            
            if gb.game_board['1'] == gb.game_board['2'] == gb.game_board['3'] != ' ': # across the top 
                gb.display_board()                                                    #displaying the board after every move
                print("Game Over.")                                               #printing game over if winning condition is met
                print("*", gb.game_board['1'], "won", "*")
                
                #breaking the loop if winning condition is met    
                break
            
            elif gb.game_board['4'] == gb.game_board['5'] == gb.game_board['6'] != ' ': # across the middle
                gb.display_board()
                print(" Game Over. ")                
                print("*", gb.game_board['4'], "won", "*")
               
                break
            
            elif gb.game_board['7'] == gb.game_board['8'] == gb.game_board['9'] != ' ': # across the bottom
                gb.display_board()
                print(" Game Over. ")                
                print("*", gb.game_board['7'], "won", "*")

            
                break
            
            elif gb.game_board['1'] == gb.game_board['5'] == gb.game_board['9'] != ' ': # across the diagonal
                gb.display_board()
                print(" Game Over. ")                
                print("*", gb.game_board['1'], "won", "*")
                
                break
            
            elif gb.game_board['1'] == gb.game_board['4'] == gb.game_board['7'] != ' ': # down the left side
                gb.display_board()
                print(" Game Over. ")                
                print("*", gb.game_board['1'], "won", "*")
                
                break
            
            elif gb.game_board['2'] == gb.game_board['5'] == gb.game_board['8'] != ' ': # down the middle
                gb.display_board()
                print(" Game Over. ")                
                print("*", gb.game_board['2'], "won", "*")
                
                break
            
            elif gb.game_board['3'] == gb.game_board['6'] == gb.game_board['9'] != ' ': # down the right side
                gb.display_board()
                print(" Game Over. ")                
                print("*", gb.game_board['3'], "won", "*")
                
                break
            
            elif gb.game_board['3'] == gb.game_board['5'] == gb.game_board['7'] != ' ': # across the diagonal
                gb.display_board()
                print(" Game Over. ")                
                print("*", gb.game_board['3'], "won", "*")
               
                break
            
            # if all the spaces got filled and none of the winning conditions are satisfied , then the game is over and decided as tie
        if turns == 9: 
            print(" Game over. ")
            print("It's a tie")
            
    



  
#using the play_game function defined above
play_game(no_of_games)

#using while loop whether to restart the game or not after the previous game ends
while True:
    restart = (input("do you want to restart the game(yes/no)?:"))
    if restart == "yes" or restart == "Yes":
        no_of_games=1+no_of_games
        for key in gb.game_board:
            gb.game_board[key] = " "
        play_game(no_of_games)
    elif restart == "no" or restart == "No":
        print("thank you for playing")
        break
    else:
        print("please enter yes or no")
       
#creating a tic-tac-toe.txt to store the number of games played
file=open("tic-tac-toe.txt",mode="a")

#defining the line 1 
line1=("total games played = ",str(no_of_games),",played at ",str(time_and_date),"\n")

#writing the first line in the tic-tac-toe.txt
file.writelines(line1)


#opening the tic-tac-toe.txt file to read
file=open("tic-tac-toe.txt","r")

#printing the text in tic-tac-toe.txt 
read_line=(file.readlines())

length=len(read_line)


print(read_line[length-1])
#clsoing the file
file.close


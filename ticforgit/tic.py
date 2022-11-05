def display_board(board):
    
    print(board[7]+' '+'|'+' '+board[8]+' '+'|'+board[9])
    print('--------')
    print(board[4]+' '+'|'+' '+board[5]+' '+'|'+board[6])
    print('--------')
    print(board[1]+' '+'|'+' '+board[2]+' '+'|'+board[3])
    
def player_input():
    maker=''
    while maker!='X' and maker!='O':
        maker=input('player1 choose x or o:').upper()
    if maker=='x':
        return ('x','o')
    else:
        return ('o','x')

def place_marker(board,marker,position):
    board[position]=marker
    
def win_check(board,mark):
    
    return((board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==board[5]==board[6]==mark) or  
    (board[7]==board[8]==board[9]==mark) or
    (board[1]==board[4]==board[7]==mark) or
    (board[2]==board[5]==board[8]==mark) or
    (board[3]==board[6]==board[9]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[3]==board[5]==board[7]==mark))


import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose a position 1 to 9:"))
    return position

def replay():
    choice=input('play again? enter yes or no:')
    return choice=='yes'


#while loop to keep running the game
print("WELCOME TO TIC TAC TOE")
while True:
    #play the game here
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn +' will go first')
    play_game=input('ready to play? y on n')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
        
    while game_on:
        if turn=='player1':
            #show the board
            display_board(the_board)
            #choose a position
            position=player_choice(the_board)
            #place the number on the position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on==False
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game")
                    break
                else:
                    turn='player2'
                    
            #or check if there is a tie
            #no tie and no win? next players turn
            # player1 turn
        else:
            
             #show the board
            display_board(the_board)
            #choose a position
            position=player_choice(the_board)
            #place the number on the position
            place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on==False
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game")
                    break
                else:
                    turn='player1'
                    
            #or check if there is a tie
            #no tie and no win? next players turn
            #player2 turn
            
            


    if not replay():
        break
#break out of while loop on replay()
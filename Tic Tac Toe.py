#board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

game_still_going = True
winner = None
current_player = "X"


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")
    
    
def play_game():

    # display inital board
    display_board()
    
    #while the game is still going 
    while game_still_going:
        
       # handle a single turn of arbitrary player 
        handle_turn(current_player)
        
       #check if the game has ended 
        check_if_game_over()

        #flip to the other player
        flip_player()
        
    
    
    # the game has ended
    if winner == "X" or winner =="O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
    
  
def handle_turn(player):
    
    print(player + "'s turn.")
    position = input("choose a position from 1-9")

    #find valid input
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("choose a position from 1-9: ")
        
        #align board
        position = int(position) - 1
    
    #available
        if board[position] == "-":
            valid = True
        else:
            print("you cant go there")
    #put game piece 
    board[position] = player
    #show
    display_board()
    
    
def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    #set up global variables
    global winner
    
    #check rows
    row_winner = check_rows()
    
    #check columns
    column_winner = check_columns()
        
    # check diagnols
    diagnols_winner = check_diagnols()
    
    #get winner
    if row_winner:
        winner = row_winner     
    elif column_winner:
        winner = column_winner
    elif diagnols_winner:
        winner = diagnols_winner

    else:
    #there was no win
        winner = None
    return


def check_rows():
    #set up global variables
    global game_still_going
    #check rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if match
    if row_1 or row_2 or row_3:
        game_still_going = False
    #find winner X/O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    #set up global variables
    global game_still_going
    #check rows
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[6] == board[7] == board[8] != "-"
    #if match
    if column_1 or column_2 or column_3:
        game_still_going = False
    #find winner X/O
    if  column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagnols():
    #set up global variables
    global game_still_going
    #check rows
    diagnol_1 = board[0] == board[4] == board[8] != "-"
    diagnol_2 = board[6] == board[4] == board[2] != "-"
    #if match
    if diagnol_1 or diagnol_2:
        game_still_going = False
    #find winner X/O
    if diagnol_1:
        return board[0]
    elif diagnol_2:
        return board[6]
    else:
        return None


def check_for_tie():
    global game_still_going
    
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
   
 
#PLEASE
play_game()

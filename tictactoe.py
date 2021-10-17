"""
    Author: Jareth Dodson
    Filename: tictactoe.py
    Last Updated: 10/10/2021
    Description: Text based version of tictactoe that
                 can have 2 players or 1 player vs. an AI

    Possible addons: Minimax AI Algorithm,
                     Show a demo board,
                     Difficulty levels,
                     GUI(may involve revamp),
                     Make main less messy(make more functions)

    Problems:   When playing against AI, when player1
                    goes to an occupied spot, the AI will still play
                
                Inputing anything else besides a 1-9 breaks program
                Inputing 0 skips player 1 move


"""
import random as rand
#Global Variables
x = 'X'
o = 'O'
player1 = x
player2 = o
cur_player = player1
board = [' ', ' ' ,' ', ' ' ,' ' ,' ' ,' ' ,' ' ,' ']
possible_moves = [1,2,3,4,5,6,7,8,9]
    
"""
    DrawBoard()
    Description: Draws a text based board for a game
    Precondition: None
    Postcondition: None
    Return: None
"""
def DrawBoard():
    count = 0
    for val1 in range(3):
        print(board[count] + '|' + board[count + 1] + '|' + board[count + 2])
        if val1 != 2:
            print('-----')
        count += 3
    print('------------')

"""
    PlayPiece(char piece, int position)
    Description: Adds piece to board
    Precondition: position must be a valid interger
    Postcondition: piece gets added to board
    Return: None
"""
def PlayPiece(piece, position):
    if position < 10 and position > 0:
        board[position - 1] = piece

"""
    CheckWin()
    Description: Check board for a win
    Postcondition: None
    Precondition: None
    Return: 1 if game has winner
            2 if game is a cats game
            0 if game is still going
"""
def CheckWin():
    if(board[0] == board[1] == board[2] and board[0] != ' ') or(board[3] == board[4] == board[5] and board[3] != ' ') or(board[6] == board[7] == board[8] and board[6] != ' ') or(board[0] == board[4] == board[8] and board[0] != ' ') or(board[2] == board[4] == board[6] and board[2] != ' ') or(board[0] == board[3] == board[6] and board[0] != ' ') or(board[1] == board[4] == board[7] and board[1] != ' ') or(board[2] == board[5] == board[8] and board[2] != ' ') :
        return 1
    elif board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ':
         return 2
    else:
        return 0

"""
    ResetBoard()
    Description: Resets board to default board
    Precondition: None
    Postcondition: Board spots are set back to ' '
    Return: None
"""
def ResetBoard():
    for i in range(9):
        board[i] = ' '

"""
    AIMove()
    Description: Plays a move based on best possible decision for Ai
    Precondition: Game must have 1 player
    Postcondition: Plays best move onto board
"""
def AIMove():
    print('AI Move')
    random_number_bool = True
    choice = 0
    while(random_number_bool):
        choice = rand.choice(possible_moves)
        if(board[choice-1] != ' '):
            possible_moves.remove(choice)
        else:
            random_number_bool = False

    PlayPiece(cur_player, choice)
    DrawBoard()

"""
    GetPlayerCount()
    Description: Get the number of players for the game
    Precondition: None
    Postcondition: None
    Return: number of players for the game
"""
def GetPlayerCount():
    num_of_players = 2
    NumOfPlayers = ' '
    while(NumOfPlayers != '1' and NumOfPlayers != '2'):
        NumOfPlayers = input('How many players? ')
        if(NumOfPlayers == '1'):
            num_of_players = 1
        elif(NumOfPlayers != '2' and NumOfPlayers != '1'):
            print('Enter valid number of players')
        
    return num_of_players
    
"""
    GetPosition()
    Description: Get position from user to players piece
    Precondition: None
    Postcondition: None
    Return: Position player chose, if position is 1-9 and an integer
            0 if player chosen position is invalid
"""
def GetPosition():
    user_input = input('Enter spot: ')
    position = 0
    if user_input.isdigit():
        position = int(user_input)
    return position

#Main for tictactoe game
def main():
    has_won = 0
    global cur_player
    cur_player = player1
    player_count = 2
    play_game = True
    spot = 0
    #ask for number of players
    player_count = GetPlayerCount()
    while(play_game == True):
        DrawBoard()
        #start of game
        while(has_won == 0):
            spot = 0
            while(spot == 0):
                spot = GetPosition()
            
            if(board[spot - 1] == ' '):
                PlayPiece(cur_player, spot)
                DrawBoard()
                has_won = CheckWin() 
                if(has_won == 1) or (has_won == 2):
                    break    
                else:
                    if cur_player == player1:
                        cur_player = player2
                    else:
                        cur_player = player1

            else:
                print('Spot is occupied, retry.')

            if(player_count == 1 and cur_player == player2): #player_count equals 1
                AIMove()
                cur_player = player1
                has_won = CheckWin()
                if(has_won == 1) or (has_won == 2):
                    break    
                 
        if(has_won == 1):
            print(cur_player + ' has won!')
        else:
            print('cats game')
        
        play_again = input('Do you want to play again? (y/n)')
        if(play_again != 'y'):
            play_game = False
        else:
            has_won = 0
            play_game = True
            ResetBoard()

if __name__ == '__main__':
    main()
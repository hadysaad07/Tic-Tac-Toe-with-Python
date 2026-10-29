import os

def displaygame(board):
  os.system('cls')
  print('Welcome to Tic-Tac-Toe game!\n')
  print(f'{ board[1]} | {board[2]} | {board[3]} ')
  print('--------')
  print(f'{ board[4]} | {board[5]} | {board[6]} ')
  print('--------')
  print(f'{ board[7]} | {board[8]} | {board[9]} ')
  print('--------')

def Player_choice():

    choice = ''
    while choice not in ('X','O'):
        choice = input("\nPlease choose player1 will choose 'X' or 'O' : ").upper()
        if choice not in ('X','O'):
            print('Invalid Input!\n')
    return choice

def Player (player):
    if player == 'X':
        player1 = player
        player2 = 'O'
    else:
        player2 = 'X'
        player1 = player
    return (player1,player2)


def user_choice(board):
    
    while True:
        choice = input('Please choose a position from 1 : 9 ->   ')

        if not choice.isdigit():
            print('Invalid Input!')
            continue
        else:
           choice = int(choice)
        if choice not in range (1,10):
            print('Invalid Input!')
            continue
        if board[choice] != ' ':
             print('This place is already occupied! \n')
             continue

        return choice

def replace_choice(choice,board,player):

    board[choice] = player 


def Winner(board):
    combinations = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]
    for a,b,c in combinations:
        if board[a]==board[b]==board[c] and board[a] != ' ':
            return board[a]
    return None

def game():
    board = [' ']*10
    board[0]='T'
    displaygame(board)
    player1,player2 = Player(Player_choice())
    current_player = player1
    while True:
        print(f'Current Player -> {current_player} : ')
        choice = user_choice(board)
        replace_choice(choice,board,current_player)
        displaygame(board)
        winner = Winner(board)
       
        if winner:
             displaygame(board)
             print(f'The winner is {winner}\n')
             break
        if all(board[i] != ' 'for i in range(1,10)):
             displaygame(board)
             print('\nIt is a draw\n')
             break
        if current_player == player1:
            current_player = player2
        else:
             current_player = player1

def game_on():
    while True:
        game()

        while True:
            gameon = input(
                'Do you want to play again? (y/n): '
        ).strip().lower()

            if gameon == 'y':
                break
            elif gameon == 'n':
                print('Thanks for playing!')
                return
        


game_on()
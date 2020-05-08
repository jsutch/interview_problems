# coding: utf-8
import os, random

def draw(board):
    """
    Draw a board from a board array
    """
    os.system('clear')
    print('   |   |')
    print((' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print((' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print((' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]))
    print('   |   |')
    
def newboard():
    return [' ' for x in range(10)]
    
def setmark():
    print('Do you want to be X or O?')
    print('default is X')
    letter = input("Type X, O or press enter: ").upper()
    if letter == 'O':
        return ['O', 'X']
    return ['X', 'O']

def firstmove(name='Nimrod'):
    if random.randint(0,1) == 0:
        return 'computer'
    return 'player'
    
def replay():
    """
    Need a way to loop back to start
    """
    print('Great game! Want to play again? (y/n)')
    if input().lower().startswith('y/n or q'):
        return "Need to build the loop for restarting"
    return "Thanks for playing!"
    
def winner(b, l):
    """
    winning moves:
    top row, middle row bottom row
    left column, middle column, right column
    top diagonal, bottom diagonal
    """
    return ((b[7] == b[8] == b[9] == l) or #horz
    (b[4] == b[5] ==  b[6] == l) or #horz
    (b[1] == b[2] ==  b[3] == l) or #horz
    (b[1] == b[5] == b[9] == l) or #diag
    (b[7] == b[5] == b[3] == l) or #diag
    (b[7] == b[4] == b[1] == l) or #vert
    (b[8] == b[5] == b[2] == l) or #vert
    (b[9] == b[6] == b[3] == l)) #vert
    
def boardcopy(board):
    return board.copy()
    
def spacefree(board, move):
    return board[move] == ' '

def getplayermove(board):
    intarr=[1,2,3,4,5,6,7,8,9]
    move = input("What's your next move? 1-9, q: ")
    if move == 'q':
        return
    if move.isdigit() and int(move) in intarr:
        return int(move)
    else:
        print('input not valid')
        getplayermove(board)

def randommove(board, moveslist):
    possiblemove = []
    for i in moveslist:
        if spacefree(board, i):
            possiblemove.append(i)
            
def boardfull(board):
    return False if ' ' in board[1:] else True
    
def movesleft(board):
    """
    returns an array of move numbers
    """
    moves = []
    for i in range(1, 10):
        if ' ' in board[i]:
            moves.append(i)
    return moves
    
def getcomputermove(board):
    """
    returns a random choice as integer
    """
    if not boardfull(board):
         return random.choice(movesleft(board))
    
        
def computermove(board):
    makemove(board, getcomputermove(board), computertoken)        
    
def playermove(board):
    makemove(board, getplayermove(), playertoken)

def makemove(board, move, token):
    if spacefree(board, move):
        board[move] = token
    else:
        return 'Space taken'
    return draw(board)

def otherguy():
    if turn == 'player':
        return 'computer'
    return 'player'

def changeturn():
    if turn == 'player':
        return 'computer'
    return 'player'

def outcome(board, player):
    """
    a dict called belligerants has to be created to map the player to the token
    belligerants = {'player': 'X','computer':'O'}. Need to write a mapping step.
    this will take belligerants[turn] to for the winner/tie/scoring phase
    """
    #pass
    if winner(board, belligerants[player]):
        draw(board)
        print(f"{player} has won the game")
        inplay = False
        replay()
    elif boardfull(board):
        draw(board)
        print("game is a tie!")
        inplay = False
        replay()
    else:
        turn = otherguy()

# main game loop
playertoken, computertoken = setmark()
belligerants = {'player': playertoken,'computer':computertoken}
turn = firstmove()
board2 = newboard()
inplay = True
while inplay:
    if turn == 'player':
        draw(board2)
        move = getplayermove(board2)
        makemove(board2, move, belligerants[turn])
        if winner(board2, belligerants[turn]):
            draw(board2)
            print(f"{turn} has won the game")
            inplay = False
            replay()
        elif boardfull(board2):
            draw(board2)
            print("game is a tie!")
            inplay = False
            replay()
        else:
            # turn = 'computer'
            turn = otherguy()
    elif turn == 'computer':
        computermove(board2)
        if winner(board2, belligerants[turn]):
            draw(board2)
            print(f"{turn} has won the game")
            inplay = False
            replay()
        elif boardfull(board2):
            draw(board2)
            print("game is a tie!")
            inplay = False
            replay()
        else:
            # turn = 'player'
            turn = otherguy()



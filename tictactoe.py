# -*- coding: utf-8 -*-
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
    """
    return a new board as a list
    """
    return [' ' for x in range(10)]
    

def setmark():
    """
    Who takes X or O?
    """
    print('Do you want to be X or O?')
    print('default is X')
    letter = input("Type X, O or press enter: ").upper()
    if letter == 'O':
        return ['O', 'X']
    return ['X', 'O']


def firstmove(name='Nimrod'):
    """
    Randomize who goes first
    """
    if random.randint(0,1) == 0:
    # if random.randint(0,10) < 9: # computer probably goes first
        return 'computer'
    return 'player'
    

def replay():
    """
    restart game
    """
    # print('Inplay is set to: ',inplay) # debugger
    if input('Great game! Want to play again? (y/n q)').lower().startswith('y'):
        newgamevars()
        return

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
    """
    utility for testing array overwrites
    """
    return board.copy()
    
def spacefree(board, move):
    """
    Check for free space on board
    """
    if isinstance(move, int):
        return board[move] == ' '
    else:
        return "Need a number between 1-9"


def randommove(board, moveslist):
    """
    random move for computer
    """
    possiblemove = []
    for i in moveslist:
        if spacefree(board, i):
            possiblemove.append(i)
            
def boardfull(board):
    """
    returns True or False if there are no spaces on board
    """
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
    """
    make the computer's move
    """
    makemove(board, getcomputermove(board), computertoken) 

def getplayermove(board):
    """
    get the player's move - integer 1-9
    """
    intarr=[1,2,3,4,5,6,7,8,9]
    move = input("What's your next move? 1-9, q: ")
    if move.isdigit() and int(move) in intarr:
        return int(move)
    elif move == 'q':
        print('Quitting')
        os._exit(0)
    else:
        print('Need a number between 1-9')
        getplayermove(board)

def playermove(board):
    """
    make the player's move
    """
    makemove(board, getplayermove(), playertoken)

def makemove(board, move, token):
    """
    Helper to make moves
    """
    if inplay == False or isinstance(move, int) == False:
        print('Something went wrong')
        os._exit(666)
    elif isinstance(move, int) and spacefree(board, move):
        board[move] = token
        return draw(board)
    #return makemove(board, move, token)
    return draw(board)

def otherguy():
    """
    Helper to change players during turns
    """
    if turn == 'player':
        return 'computer'
    return 'player'


def outcome(board, player):
    """
    a dict called belligerants has to be created to map the player to the token
    belligerants = {'player': 'X','computer':'O'}. 
    this will take belligerants[turn] to for the winner/tie/scoring phase
    """
    global turn
    global inplay
    if winner(board, belligerants[player]):
        draw(board)
        print(f"{player} has won the game")
        inplay = False
        replay()
    elif boardfull(board):
        draw(board)
        print("game is a tie!")
        inplay  = False
        replay()
    else:
        turn = otherguy()



def newgamevars():
    global playertoken, computertoken, belligerants, turn, mainboard, inplay
    playertoken, computertoken = setmark()
    belligerants = {'player': playertoken,'computer':computertoken}
    turn = firstmove()
    mainboard = newboard()
    inplay = True


def main():
    global turn
    global mainboard
    global inplay
    while inplay:
        if turn == 'player':
            draw(mainboard)
            move = getplayermove(mainboard)
            makemove(mainboard, move, playertoken)
            outcome(mainboard, turn)
        elif turn == 'computer':
            computermove(mainboard)
            outcome(mainboard, turn)

if __name__ == "__main__":
    print("Ok - let's play a new game")
    newgamevars()
    while True:
        if inplay == True:
            main()
        else:
            print('Game Over')
            break
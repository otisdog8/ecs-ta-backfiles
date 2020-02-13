import sys

def intput(text):
    isint = False
    
    while not isint:
        try:
            result = int(input(text))
            isint = True
        except ValueError:
            pass

    return result

def displayboard(board):
    print("\n\n")
    for r in board:
        print("\t",end='')
        for c in r:
            print(c, end='')
            print('\t', end='')
        print('\n\n')

config = intput("Do you want:\n1) standard tictactoe\n2) advanced tictactoe\n")

if config == 1:
    size = 3
    players = 2
    turns = ["X", "O"]
    filler = "E"
    streak = 3
elif config == 2:
    size = intput("Enter the size of your tic-tac-toe board:    ")
    players = intput("Enter the number of players:    ")

    turns = []

    for i in range(players):
        turns.append(input("Enter the symbol for the player:   "))

    filler = input("Enter a character used to designate empty space:   ")
    streak = intput("Enter the number of symbols in a row to win (doesn't affect diagonals):    ")
else:
    sys.exit()


tictacarray = []

for i in range(size):
    tictacarray.append([])
    for j in range(size):
        tictacarray[i].append(filler)

displayboard(tictacarray)

won = False

turnptr = 0

rscore = []
cscore = []

for i in range(players):
    rscore.append([])
    cscore.append([])
    for j in range(size):
        rscore[i].append(0)
        cscore[i].append(0)

while turnptr < size*size and not won:
    player = turnptr % players
    displayboard(tictacarray)
    print("Player " + turns[player] + " playing")
    xpt = intput("Enter the x coordinate of your selection: ")
    ypt = intput("Enter the y coordinate of your selection: ")

    if not tictacarray[ypt][xpt] in turns:
        tictacarray[ypt][xpt] = turns[player]


    for i in range(size):
        rscore[player][i] = 0
        cscore[player][i] = 0
    
    diagonal = True

    for i in range(size):
        if tictacarray[i][i] == turns[player]:
            pass
        else:
            diagonal = False

        if tictacarray[size-i-1][size-i-1] == turns[player]:
            pass
        else:
            diagonal = False


    for i in range(size):
        for j in range(size):
            if tictacarray[i][j] == turns[player]:
                rscore[player][i] += 1
            if tictacarray[j][i] == turns[player]:
                cscore[player][i] += 1

    print(rscore)
    print(cscore)
    print(diagonal)

    if streak in rscore[player] or streak in cscore[player] or diagonal:
        won = True

    turnptr += 1

displayboard(tictacarray)

if won:
    print("Player " + turns[player] + " won")
else:
    print("Stalemate!")
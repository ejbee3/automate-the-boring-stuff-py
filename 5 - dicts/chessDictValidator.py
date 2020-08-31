import sys

# TODO: make this program accept dictionary inputs
startingBoard = {'a1': 'wrook', 'a2': 'wpawn', 'a7': 'bpawn', 'a8': 'brook',
                 'b1': 'wknight', 'b2': 'wpawn', 'b7': 'bpawn', 'b8': 'bknight',
                 'c1': 'wbishop', 'c2': 'wpawn', 'c7': 'bpawn', 'c8': 'bbishop',
                 'd1': 'wqueen', 'd2': 'wpawn', 'd7': 'bpawn', 'd8': 'bqueen',
                 'e1': 'wking', 'e2': 'wpawn', 'e7': 'bpawn', 'e8': 'bking',
                 'f1': 'wbishop', 'f2': 'wpawn', 'f7': 'bpawn', 'f8': 'bbishop',
                 'g1': 'wknight', 'g2': 'wpawn', 'g7': 'bpawn', 'g8': 'bknight',
                 'h1': 'wrook', 'h2': 'wpawn', 'h7': 'bpawn', 'z8': 'brook', }


# program output
print('Is your chess board valid?')

if ((pieceTotal(startingBoard, 'pawn') <= 16) and (pieceTotal(startingBoard, 'rook') <= 4)
    and (pieceTotal(startingBoard, 'bishop') <= 4) and (pieceTotal(startingBoard, 'queen') <= 2)
    and (pieceTotal(startingBoard, 'knight') <= 4) and (pieceTotal(startingBoard, 'king') == 2)
        and isColorValid(startingBoard) and isValidSquare(startingBoard)):
    print('Yes, your chess board is valid.')
else:
    print('No, your chess board is not valid... \nwould you like more information? ' +
          '(y)es or (n)o')
    userInput = input().lower()
    if (userInput == 'y'):
        print('You have ' + str(pieceTotal(startingBoard, 'pawn')) + ' pawns.')
        print('You have ' + str(pieceTotal(startingBoard, 'rook')) + ' rooks.')
        print('You have ' + str(pieceTotal(startingBoard, 'bishop')) + ' bishops.')
        print('You have ' + str(pieceTotal(startingBoard, 'knight')) + ' knights.')
        print('You have ' + str(pieceTotal(startingBoard, 'queen')) + ' queens.')
        print('You have ' + str(pieceTotal(startingBoard, 'king')) + ' kings.')
        if (isColorValid(startingBoard)):
            print('Your colors: (w)hite and (b)lack are valid')
        else:
            print('You do not have all (w)hite and (b)lack pieces.')
        if (isValidSquare(startingBoard)):
            print('Your pieces are on valid squares.')
        else:
            print('One or more of your pieces is on an invalid square.')
    elif (userInput == 'n'):
        sys.exit()


# functions for program
def pieceTotal(board, piece):
    numPieces = 0
    for v in board.values():
        if (v[1:len(v)] == piece):
            numPieces += 1
    return numPieces


def isValidSquare(board):
    isValidChar = True
    isValidNum = True
    for k in board.keys():
        for char in char_range('i', 'z'):
            if (k[0].lower() == char):
                isValidChar = False

        if (int(k[1]) == 0 or int(k[1:len(k)]) >= 9):
            isValidNum = False

    if (isValidNum and isValidChar):
        return True
    else:
        return False


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def isColorValid(board):
    for v in board.values():
        for char in char_range('c', 'v'):
            if (v[0].lower() == char or v[0].lower() == 'a' or
                    v[0].lower() == 'x' or v[0].lower() == 'y' or v[0].lower() == 'z'):
                return False

    return True

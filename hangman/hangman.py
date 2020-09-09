import random
import sys

randomWordList = ['Hua Mulan', 'Stitch', 'Aladdin', 'Princess Jasmine', 'Pinocchio', 'Phineas Flynn', 'Pocahontas',
                  'Rapunzel', 'Cheshire Cat', 'Cinderella', 'Hercules', 'Duchess', 'Figaro the cat',
                  'Ichabod Crane', 'Jack Skellington', 'Jiminy Cricket', 'Kuzco', 'Kronk', 'Maleficent', 'Mad Hatter',
                  'Mary Poppins', 'Mufasa', 'Pegasus', 'Piglet', 'Prince Charming',
                  'Pumbaa', 'Quasimodo', 'Ron Stoppable', 'Snow White', 'Tinker Bell',
                  'Ursula', 'Violet Parr', 'Wendy Darling', 'Wreck it Ralph']
# all taken from the Disney animated characters Wikipedia page


def fillBoard(word):
    for letter in randomWord:
        if letter != ' ':
            word.append('_')
        else:
            word.append(' ')


randomWord = list(randomWordList[random.randint(
    0, len(randomWordList) - 1)].lower())
numOfGuessesLeft = 6
graveyard = []
board = []

print('Welcome to Hang that Disney Character! \nGuess the name in 6 guesses and you win!')

fillBoard(board)

print(f"Here's your mystery Disney character: {''.join(board)}")

while True:
    if board == randomWord:
        print('\nYou won! That Disney character is dead b/c of you.')
        break
    elif numOfGuessesLeft < 0:
        print('You lost! That Disney Character will live on in infamy!')
        break

    else:
        print('Enter your guess: (any letter from A-Z)')
        playerGuess = input().lower()
        if playerGuess in randomWord:
            idx = [i for i, x in enumerate(randomWord) if x == playerGuess]
            for indice in idx:
                board[indice] = playerGuess
            print(
                f"\nYou guessed right! \nHere's your board: {''.join(board)}")
        else:
            graveyard.append(playerGuess)
            numOfGuessesLeft -= 1
            print(
                f"""\nYou guessed wrong! You have {numOfGuessesLeft} guesses left.
Here's your board: {''.join(board)} 
Here's your graveyard: {' '.join(graveyard)}\n""")

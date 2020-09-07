import random

randomWordList = ['Hua Mulan', 'Stitch', 'Aladdin', 'Princess Jasmine', 'Pinocchio', 'Phineas Flynn', 'Pocahontas',
                  'Rapunzel', 'Cheshire Cat', 'Cinderella', 'Hercules', 'Duchess', 'Figaro the cat',
                  'Ichabod Crane', 'Jack Skellington', 'Jiminy Cricket', 'Kuzco', 'Kronk', 'Maleficent', 'Mad Hatter',
                  'Mary Poppins', 'Mufasa', 'Pegasus', 'Piglet', 'Prince Charming',
                  'Pumbaa', 'Quasimodo', 'Ron Stoppable', 'Snow White', 'Tinker Bell',
                  'Ursula', 'Violet Parr', 'Wendy Darling', 'Wreck it Ralph']
# all taken from the Disney animated characters Wikipedia page


def fillWord(wordList):
    for letter in randomName:
        wordList.append('_')


def splitWord(word):
    return list(word)


randomName = splitWord(randomWordList[random.randint(
    0, len(randomWordList) - 1)])
numOfGuesses = 0
wins = 0
losses = 0
wrongGuesses = []

print('Welcome to Hangman! \nGuess the name in 6 tries and you win!')

while True:
    print('%s Guesses, %s Wins, %s Losses' % (numOfGuesses, wins, losses))
    print('Enter your guess: (any letter from A-Z)')
    playerGuess = input().lower()
    correctGuesses = fillWord([])
    for idx, letter in enumerate(randomName):
        if playerGuess[0] == letter.lower():
            correctGuesses[idx] == randomName[idx]
            print(
                f"""You guessed correct! \nYour word now looks
                like {' '.join(correctGuesses)}""")
        elif playerGuess != letter.lower():
            wrongGuesses.append(playerGuess)
            numOfGuesses += 1

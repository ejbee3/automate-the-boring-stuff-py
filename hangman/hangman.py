import random

randomWordList = ['Hua Mulan', 'Stitch', 'Aladdin', 'Princess Jasmine', 'Pinocchio', 'Phineas Flynn', 'Pocahontas',
                  'Rapunzel', 'Cheshire Cat', 'Cinderella', 'Hercules', 'Duchess', 'Figaro the cat',
                  'Ichabod Crane', 'Jack Skellington', 'Jiminy Cricket', 'Kuzco', 'Kronk', 'Maleficent', 'Mad Hatter',
                  'Mary Poppins', 'Mufasa', 'Pegasus', 'Piglet', 'Prince Charming',
                  'Pumbaa', 'Quasimodo', 'Ron Stoppable', 'Snow White', 'Tinker Bell',
                  'Ursula', 'Violet Parr', 'Wendy Darling', 'Wreck it Ralph']
# all taken from the Disney animated characters Wikipedia page


def fillWord(wordList):
    for letter in chosenWord:
        wordList.append('_')


# randomName = splitWord(randomWordList[random.randint(
#     0, len(randomWordList) - 1)])
chosenWord = list(randomWordList[12])
numOfGuesses = 0
wins = 0
losses = 0
graveyard = []
wordDict = {}

print('Welcome to Hangman! \nGuess the name in 6 tries and you win!')

while True:
    print('%s Guesses, %s Wins, %s Losses' % (numOfGuesses, wins, losses))
    print('Enter your guess: (any letter from A-Z)')
    board = fillWord([])
    playerGuess = input().lower()
    for letter in chosenWord:
      # make the dictionary for the word
        if letter == ' ':
            wordDict.setdefault('space', 0)
            wordDict['space'] += 1
        else:
            wordDict.setdefault(letter.lower(), 0)
            wordDict[letter.lower()] += 1

        if playerGuess == letter:
            print('You guessed correctly! \nGuess again.')
    print(wordDict)

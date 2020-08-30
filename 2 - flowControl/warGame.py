import random
import sys

print('WAR - the card game')
print('O==|======>  <++++++|==&')
wins = 0
losses = 0
suits = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
faceCards = ['JACK', 'QUEEN', 'KING', 'ACE']

while True:
    print('%s Wins, %s Losses' % (wins, losses))
    while True:
        print('(D)raw a card or (q)uit the game')
        playerInput = input().lower()
        if playerInput == 'q':
            sys.exit()
        if playerInput == 'd':
            break
        print('Type either d or q.')

    # player draw
    randomCard = random.randint(2, 14)
    randomSuit = random.randint(0,  3)
    if randomCard >= 2 and randomCard <= 10:
        print('You drew the %s of %s' %
              (randomCard, suits[randomSuit]))
    elif randomCard == 11:
        print('You drew the %s of %s' %
              (faceCards[0], suits[randomSuit]))
    elif randomCard == 12:
        print('You drew the %s of %s' %
              (faceCards[1], suits[randomSuit]))
    elif randomCard == 13:
        print('You drew the %s of %s' %
              (faceCards[2], suits[randomSuit]))
    elif randomCard == 14:
        print('You drew the %s of %s' %
              (faceCards[3], suits[randomSuit]))

    print('O==|======>')

    # computer draw
    computerCard = random.randint(2, 14)
    computerSuit = random.randint(0, 3)
    print('The computer draws...')
    if computerCard >= 2 and computerCard <= 10:
        print('the %s of %s' %
              (computerCard, suits[computerSuit]))
    elif computerCard == 11:
        print('the %s of %s' %
              (faceCards[0], suits[computerSuit]))
    elif computerCard == 12:
        print('the %s of %s' %
              (faceCards[1], suits[computerSuit]))
    elif computerCard == 13:
        print('the %s of %s' %
              (faceCards[2], suits[computerSuit]))
    elif computerCard == 14:
        print('the %s of %s' %
              (faceCards[3], suits[computerSuit]))

    print('<++++++|==&')
    # determine who wins
    if computerCard == randomCard:
        playerDice = random.randint(1, 6)
        computerDice = random.randint(1, 6)
        if playerDice > computerDice:
            print('It\'s a tie! But you won the dice roll %s to %s!' %
                  (playerDice, computerDice))
            wins = wins + 1
        elif computerDice > playerDice:
            print('It\'s a tie! But you lost the dice roll :( %s to %s' %
                  (computerDice, playerDice))
    elif randomCard > computerCard:
        print('You won!')
        wins = wins + 1
    elif computerCard > randomCard:
        print('You lost :(')
        losses = losses + 1

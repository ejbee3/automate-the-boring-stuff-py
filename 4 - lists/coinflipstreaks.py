import random

numOfStreaks = 0

for experimentNum in range(10000):
    # code that creates a list of 100 'heads' or 'tails' values

    listOf100Flips = []
    for flip in range(100):
        coinflip = random.randint(0, 1)
        if (coinflip == 0):
            listOf100Flips.append('heads')
        else:
            listOf100Flips.append('tails')


# code that checks if there is a streak of 6 heads or tails in a row
    for idx, flip in enumerate(listOf100Flips):
        if (listOf100Flips[idx:idx + 6] == ['heads', 'heads', 'heads', 'heads', 'heads', 'heads'] or
                listOf100Flips[idx:idx + 6] == ['tails', 'tails', 'tails', 'tails', 'tails', 'tails']):
            numOfStreaks += 1
print('Chance of streak: %s%%' % (numOfStreaks / 10000))

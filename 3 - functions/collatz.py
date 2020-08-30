import sys


def collatz(num):
    while num >= 2:
        if num % 2 == 0:
            num = num // 2
            print(str(num))
        else:
            num = 3 * num + 1
            print(str(num))


print('Enter number:')

while True:
    try:
        userInput = int(input())
        collatz(userInput)
        sys.exit()

    except ValueError:
        print('You must enter a number!')

import copy
from collections.abc import Iterable


def commacode(argList):

    if not argList:
        print('You gave an empty list, program will exit now.')

    flattenedArgList = list(flatten(argList))

    for itemInArgList in flattenedArgList:

        if (flattenedArgList[-1] == itemInArgList and len(flattenedArgList) > 1):
            print('and ', end='')
            print(itemInArgList)
        else:
            print(itemInArgList, end='')
            print(', ', end='')


def flatten(x):
    for el in x:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


commacode([2, 3, 4, ['grass', 'cow'], 'apple', 'dog'])

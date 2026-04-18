import random
import sys
import os


def addNumber(fNumb: int, lNumb: int) -> int:
    """
    this is a fn Descriptor string
    :param fNumb:
    :param lNumb:
    :return:
    """
    sumNumb = fNumb + lNumb
    return sumNumb

string = addNumber(1, 2)
print(string)

# print(sumNumb) # will error, vars are function scope

# system fn() calls
print('What is your name?')
name = sys.stdin.readline()
print('Hello', name)
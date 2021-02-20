#import numpy as np
import math

def show(state):
    baseStr = list("........")
    for row in state:
        str = baseStr.copy()
        if row > -1:
            str[row] = 'X'
        print(str)

def isThreaten(curr, test):
    if curr[0] == test[0]:
        return True
    if curr[1] == test[1]:
        return True
    if abs(curr[0] - test[0]) == abs(curr[1] - test[1]):
        return True
    return False


def isOK(r, c, state):
    for i in range(r):
        if isThreaten((r, c), (i, state[i])):
            return False
    return True

queens = [-1, -1, -1, -1, -1, -1, -1, -1]

for r in range(8):
    r_ok = False
    for c in range(queens[r] + 1, 8):
        if isOK(r, c, queens):
            print(r, c)
            queens[r] = c
            r_ok = True
            break
   # if  not r_ok:



show(queens)

#import numpy as np
import math

def show(state, n, k):

    baseStr = ['.'] * k
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


def giveParams():
    print("Give the number of the rows: ")
    n = int(input())
    print("Give the number of the columns: ")
    k = int(input())
    print("The size of the board:", n, " × ", k)
    return n, k


def numOfQueens(n, k):
    if n >= k:
        q = k
    else:
        q = n
    return q


# Find solutions

solutions = []

n, k = giveParams()

q = numOfQueens(n, k)
queens = [-1]*q

print(queens)
r = 0
c = 0

if k >= n:
    while r < k and r > -1:
        r_ok = False
        for c in range(queens[r] + 1, k):
            if isOK(r, c, queens):
                queens[r] = c
                r_ok = True
                break

        if not r_ok:
            queens[r] = -1
            r = r - 1
        else:
            r = r + 1

        if r == n:
                solutions.append(queens.copy())
                r = r - 1

# Test solutions
errors = []

# Test1 - testing every raw in all solutions
for i, solution in enumerate(solutions):
    for r, c in enumerate(solutions[i]):
        if c < 0 or c > k - 1:
            errors.append((1, i, r))

# Test2 - testing every queen in all solutions
if len(errors) == 0:
    for i, solution in enumerate(solutions):
        for R, C in enumerate(solutions[i]):
            for r, c in enumerate(solutions[i]):
                if R == r:
                    continue
                if C == c:
                    errors.append((2, i, r))
                if abs(C - c) == abs(R - r):
                    errors.append((2, i, r))

# Show solution
if len(errors) == 0:
    num_of_solutions = len(solutions)
    for i, solution in enumerate(solutions):
        print("{}/{}".format((i + 1), num_of_solutions))
        show(solution, n, k)
else:
    print("Something went wrong!")
    print("(Test case, solution, row of solution)")
    for i, error in enumerate(errors):
        print(error)

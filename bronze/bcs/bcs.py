import sys
from copy import deepcopy


def count(figure):
    return sum([line.count('#') for line in figure])


def check(figure, p1, p2, n, cf, c1, c2):
    if c1 + c2 != cf:
        return False
    for i1 in range(1-n, n-1):
        for j1 in range(1-n, n-1):
            for i2 in range(1-n, n-1):
                for j2 in range(1-n, n-1):
                    valid = True
                    for i in range(n):
                        for j in range(n):
                            value = '.'
                            if 0 <= i-i1 < n and 0 <= j-j1 < n:
                                value = p1[i-i1][j-j1]
                            if 0 <= i-i2 < n and 0 <= j-j2 < n:
                                if p2[i-i2][j-j2] == '#':
                                    if value == '#':
                                        valid = False
                                        break
                                    else:
                                        value = p2[i-i2][j-j2]
                            if value != figure[i][j]:
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        return True
    return False


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, k = [int(i) for i in input().split()]
    figure = []
    pieces = []
    for i in range(n):
        figure.append(list(input()))
    cf = count(figure)

    for i in range(k):
        p = []
        for j in range(n):
            p.append(input())
        pieces.append(p)
    cp = [count(p) for p in pieces]

    for i in range(k):
        for j in range(i+1, k):
            if check(figure, pieces[i], pieces[j], n, cf, cp[i], cp[j]):
                print(min(i, j)+1, max(i, j)+1)
                return


if __name__ == "__main__":
    main('bcs')

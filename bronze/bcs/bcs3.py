import sys
from copy import deepcopy


def remove_dots(piece, n):
    np = []
    first = n
    last = 0
    for line in piece:
        if '#' not in line:
            continue
        else:
            np.append(line)
            first = min(line.index('#'), first)
            last = max(n - line[::-1].index('#'), last)
    np = [line[first:last] for line in np]
    return np


def count(figure):
    return sum([line.count('#') for line in figure])


def print_figure(figure):
    for i in range(len(figure)):
        print(''.join(figure[i]))


def same(f1, f2):
    if len(f1) != len(f2):
        return False
    for i in range(len(f1)):
        if f1[i] != f2[i]:
            return False
    return True


def check(figure, p1, p2, n, cf, c1, c2, figure_only):
    # shift p1 up and right
    if c1 + c2 != cf:
        return False
    si = []
    for i in range(n * 3):
        si.append(['.'] * (n * 3))
    # Put p1 in the middle
    for i in range(n):
        for j in range(n):
            si[n+i][n+j] = p1[i][j]
    for i in range(0, n*2+1):
        for j in range(0, n*2+1):
            si_copy = deepcopy(si)
            valid = True
            for k in range(n):
                for l in range(n):
                    if p2[k][l] == '#' and si_copy[i+k][j+l] == '#':
                        valid = False
                        break
                    if p2[k][l] == '#':
                        si_copy[i+k][j+l] = p2[k][l]
                if not valid:
                    break
            if valid:
                si_copy = remove_dots(si_copy, 3*n)
                if same(si_copy, figure_only):
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
    figure_only = remove_dots(figure, n)
    for i in range(k):
        for j in range(i+1, k):
            if check(figure, pieces[i], pieces[j], n, cf, cp[i], cp[j], figure_only):
                print(min(i, j)+1, max(i, j)+1)
                return


if __name__ == "__main__":
    main('bcs')

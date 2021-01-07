import sys
from copy import deepcopy


def remove_dots(piece, n):
    first = n
    last = 0
    first_line = -1
    last_line = -1
    for j in range(len(piece)):
        line = piece[j]
        line_first = -1
        line_last = -1
        for i in range(n):
            if line[i] == '#':
                if line_first == -1:
                    line_first = i
                line_last = i
        if line_first == -1:
            continue
        if first_line == -1:
            first_line = j
        last_line = j
        first = min(line_first, first)
        last = max(line_last, last)
    return [piece[j][first:last+1] for j in range(first_line, last_line+1)]


def count(figure):
    return sum([line.count('#') for line in figure])


def print_figure(figure):
    for i in range(len(figure)):
        print(''.join(figure[i]))


def check(figure, p1, p2, cf, c1, c2):
    # shift p1 up and right
    if c1 + c2 != cf:
        return False
    si = []
    w1 = len(p1[0])
    w2 = len(p2[0])
    h1 = len(p1)
    h2 = len(p2)
    w = w1 + w2 * 2
    h = h1 + h2 * 2
    for i in range(h):
        si.append(['.'] * w)
    # Put p1 in the middle
    for i in range(h1):
        for j in range(w1):
            si[h2+i][w2+j] = p1[i][j]
    for i in range(0, h1+h2+1):
        for j in range(0, w1+w2+1):
            si_copy = deepcopy(si)
            valid = True
            for k in range(h2):
                for l in range(w2):
                    if p2[k][l] == '#':
                        if si_copy[i+k][j+l] == '#':
                            valid = False
                            break
                        si_copy[i+k][j+l] = p2[k][l]
                if not valid:
                    break
            if valid:
                si_copy = remove_dots(si_copy, w)
                if len(si_copy) == len(figure) and len(si_copy[0]) == len(figure[0]):
                    if si_copy == figure:
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
    figure = remove_dots(figure, n)
    cf = count(figure)

    for i in range(k):
        p = []
        for j in range(n):
            p.append(input())
        pieces.append(remove_dots(p, n))
    cp = [count(p) for p in pieces]
    for i in range(k):
        for j in range(i+1, k):
            if check(figure, pieces[i], pieces[j], cf, cp[i], cp[j]):
                print(min(i, j)+1, max(i, j)+1)
                return


if __name__ == "__main__":
    main('bcs')

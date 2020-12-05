import sys


def find(color, b, i, j, r, c, total):
    if i == r-1 and j == c-1:
        return total + 1
    elif i == r-1 or j == c-1:
        return total
    else:
        for x in range(i+1, r):         #  R R R R
            for y in range(j+1, c):     #  R B R R
                if b[x][y] != color:    #  R B R R
                    total = find(b[x][y], b, x, y, r, c, total)
        return total


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    r, c = [int(i) for i in input().split()]
    b = []
    for i in range(r):
        b.append(list(input()))

    l = (0, 0)
    color = b[0][0]
    total = find(color, b, 0, 0, r, c, 0)
    print(total)


if __name__ == "__main__":
    main('hopscotch')

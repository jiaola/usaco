import sys


def find(field):
    n = len(field)
    max_dist = -1
    cell = (-1, -1)
    for i in range(0, n):
        for j in range(0, n):
            if field[i][j] == 1 and i + j > max_dist:
                max_dist = i + j
                cell = (i, j)
    return cell


def flip(field, cell):
    x, y = cell
    for i in range(0, x+1):
        for j in range(0, y+1):
            field[i][j] = 1 - field[i][j]
    return field


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    field = []
    for i in range(n):
        field.append([int(j) for j in list(input())])
    cell = find(field)
    n = 0
    while cell != (-1, -1):
        n += 1
        field = flip(field, cell)
        cell = find(field)
    print(n)


if __name__ == "__main__":
    main('cowtip')

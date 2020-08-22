import sys


def main(pname):
    sys.stdin = open(pname + 'in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    for i in range(10):
        line = input()
        if 'B' in line:
            b = (i, line.index('B'))
        if 'R' in line:
            r = (i, line.index('R'))
        if 'L' in line:
            l = (i, line.index('L'))
    d = 0
    if b[0] == r[0] == l[0] and (b[1] < r[1] < l[1] or b[1] > r[1] > l[1]):
        d = abs(l[1] - b[1]) + 1
    elif b[1] == r[1] == l[1] and (b[0] < r[0] < l[0] or b[0] > r[0] > l[0]):
        d = abs(l[0] - b[0]) + 1
    else:
        d = abs(l[0] - b[0]) + abs(l[1] - b[1]) - 1
    print(str(d))


if __name__ == "__main__":
    main('buckets')

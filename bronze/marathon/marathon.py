import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    t = 0
    d = 0
    for i in range(n):
        p = [int(i) for i in input().split()]
        if i == 1:
            d1 = abs(p[0] - p1[0]) + abs(p[1] - p1[1])
        if i > 1:
            d2 = d1
            d1 = abs(p[0] - p1[0]) + abs(p[1] - p1[1])
            d3 = abs(p[0]-p2[0]) + abs(p[1]-p2[1])
            diff = d1 + d2 - d3
            d = max(d, diff)
            if i == 2:
                t += d2
            t += d1
        if i > 0:
            p2 = p1
        p1 = p
    print(t - d)


if __name__ == "__main__":
    main('marathon')

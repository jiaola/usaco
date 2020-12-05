import sys


def solve(k, x):
    s = 0
    d = 0
    c = 0
    while d < k:
        s += 1
        if s < x:
            d += s
            c += 1
        else:
            d += 2 * s
            c += 2
    if d - k >= s:
        c -= 1
    return c


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    k, n = [int(i) for i in input().split()]
    for i in range(n):
        x = int(input())
        print(solve(k, x))


if __name__ == "__main__":
    main('race')

import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    r1 = [int(i) for i in input().split()]
    r2 = [int(i) for i in input().split()]

    x = [r1[0], r1[2], r2[0], r2[2]]
    y = [r1[1], r1[3], r2[1], r2[3]]

    s = max(max(x) - min(x), max(y) - min(y))
    print(s*s)


if __name__ == "__main__":
    main('square')

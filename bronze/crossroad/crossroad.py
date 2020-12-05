import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    cows = {}
    c = 0
    for i in range(n):
        id, s = [int(i) for i in input().split()]
        if id in cows:
            if cows[id] != s:
                c += 1
        cows[id] = s
    print(c)


if __name__ == "__main__":
    main('crossroad')

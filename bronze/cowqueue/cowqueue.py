import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    q = []
    for i in range(n):
        x, y = [int(i) for i in input().split()]
        q.append((x, y))
    q.sort()

    t = 0
    for i in q:
        t = max(t, i[0]) + i[1]
    print(t)


if __name__ == "__main__":
    main('cowqueue')

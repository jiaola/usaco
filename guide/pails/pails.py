import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    x, y, m = [int(i) for i in input().split()]
    i = j = 0
    s = 0
    for i in range(int(m/x)+1):
        for j in range(int(m/y)+1):
            n = x * i + y * j
            if n <= m:
                s = max(s, n)
            else:
                break
    print(s)


if __name__ == "__main__":
    main('pails')

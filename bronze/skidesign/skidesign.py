import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))

    k = 17
    t = sys.maxsize
    for i in range(min(l), max(l)):
        s = 0
        for j in l:
            if j < i:
                s += (i - j) ** 2
            elif j > i + 17:
                s += (j - (i + 17)) ** 2
        t = min(t, s)
    print(t)


if __name__ == "__main__":
    main('skidesign')

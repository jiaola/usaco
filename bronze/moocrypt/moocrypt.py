import sys


def count(t, m, o):
    if m == o or m == 'M' or o == 'O':
        return 0
    moo = m + o + o
    oom = o + o + m
    c = 0
    for i in t:
        c += i.count(moo)
        c += i.count(oom)

    nrow = len(t)
    ncol = len(t[0])

    for i in range(ncol):
        s = ''
        for j in t:
            s += j[i]
        c += s.count(moo)
        c += s.count(oom)

    # diagnols
    for i in range(nrow + ncol - 1):
        s = ''
        for j in range(nrow):
            if i >= j and i - j < ncol:
                s += t[j][i-j]
        c += s.count(moo)
        c += s.count(oom)

    for i in range(1-nrow, ncol):
        s = ''
        for j in range(nrow):
            if 0 <= i+j < ncol:
                s += t[j][i+j]
        c += s.count(moo)
        c += s.count(oom)

    return c


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, m = [int(i) for i in input().split()]

    t = []
    for i in range(n):
        t.append(input())

    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c = 0
    for i in l:
        for j in l:
            c = max(c, count(t, i, j))
    print(c)


if __name__ == "__main__":
    main('moocrypt')

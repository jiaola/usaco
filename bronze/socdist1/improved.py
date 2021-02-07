import sys
from math import ceil, floor


def count(lst, i, j):
    if lst[i] == 1 or lst[j] == 1:
        return -1
    lst_cp = lst.copy()
    lst_cp[i] = 1
    lst_cp[j] = 1
    mn = len(lst_cp)
    first = True
    cnt = 0
    for i in range(len(lst_cp)):
        if lst_cp[i] == 1:
            if first:
                first = False
            else:
                mn = min(cnt, mn)
            cnt = 0
        else:
            cnt += 1
    return mn


def d(g):
    return g[1] - g[0]


def mid(g):
    return (g[1] + g[0]) // 2


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    g1 = [-1, -1]
    g2 = [-1, -1]

    n = int(input())
    lst = [int(i) for i in input()]

    gap = [-1, -1]
    if lst[0] == 0:
        gap[0] = 0

    for i in range(1, n):
        j = lst[i]
        if j == 0:
            if gap[0] == -1:  # new gap
                gap[0] = i
        else:
            if lst[i-1] == 0:
                gap[1] = i
                if d(gap) > d(g1):
                    g2 = g1
                    g1 = gap
                elif d(gap) > d(g2):
                    g2 = gap
            gap = [-1, -1]
    if lst[-1] == 0:
        gap[1] = n

    if g1 == [-1, -1]:
        g1 = [0, n]

    m = 0
    # 1st, last
    m = max(m, count(lst, 0, n-1))
    m = max(m, count(lst, 0, mid(g1)))
    m = max(m, count(lst, n-1, mid(g1)))
    m = max(m, count(lst, mid(g1), mid(g2)))
    m = max(m, count(lst, floor(g1[0] + (g1[1] - g1[0]) / 3), floor(g1[0] + (g1[1] - g1[0]) / 3 * 2)))
    print(m+1)


if __name__ == "__main__":
    main('socdist1')

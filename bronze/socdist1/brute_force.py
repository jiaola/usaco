import sys


def count(lst, i, j):
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


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')
    n = int(input())
    lst = [int(i) for i in input()]
    mx = 0
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == 0 and lst[j] == 0:
                mx = max(count(lst, i, j), mx)
    print(mx+1)


if __name__ == '__main__':
    main('socdist1')

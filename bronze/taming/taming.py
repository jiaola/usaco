import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    lst = [int(i) for i in input().split()]

    for i in range(n-2, -1, -1):
        if lst[i] == -1 and lst[i+1] > 0:
            lst[i] = lst[i+1] - 1

    if lst[0] == 0:
        for i in range(n-1):
            if lst[i+1] - lst[i] != 1 and lst[i+1] > 0:
                print(-1)
                return

    m = 0
    M = 0

    for i in range(n):
        if lst[i] == -1 or lst[i] == 0:
            M += 1
        if i == 0 and lst[i] == -1:
            m += 1
        if lst[i] == 0:
            m += 1

    print(m, M)


if __name__ == "__main__":
    main('taming')

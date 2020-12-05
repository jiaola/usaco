import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    a = [int(i) for i in input().split()]
    cows = input().split()

    for i in range(3):
        c = [''] * n
        for j in range(n):
            c[j] = cows[a[j]-1]
        cows = c
    print('\n'.join(cows))


if __name__ == "__main__":
    main('shuffle')

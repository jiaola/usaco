import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    m, n, k = [int(i) for i in input().split()]
    for i in range(m):
        line = ''
        for j in input():
            line += j * k
        for j in range(k):
            print(line)


if __name__ == "__main__":
    main('cowsignal')

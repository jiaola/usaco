import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    a, b = [int(i) for i in input().split()]
    c, d = [int(i) for i in input().split()]

    t = 0
    for i in range(101):
        if a <= i < b or c <= i < d:
            t += 1
    print(t)


if __name__ == '__main__':
    main('paint')

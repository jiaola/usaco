import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    p = [int(i) for i in input().split()]
    p.sort()

    if p[1] - p[0] == 1 and p[2] - p[1] == 1:
        print(0)
    elif p[1] - p[0] == 2 or p[2] - p[1] == 2:
        print(1)
    else:
        print(2)
    print(max(p[1]-p[0], p[2]-p[1]) - 1)


if __name__ == "__main__":
    main('herding')

import sys


def overlap(r1, r2):
    if r1[0] > r2[2] or r1[2] < r2[0] or r1[1] > r2[3] or r1[3] < r2[1]:
        return 0
    else:
        x = [r1[0], r1[2], r2[0], r2[2]]
        y = [r1[1], r1[3], r2[1], r2[3]]
        x.sort()
        y.sort()
        return (x[2]-x[1]) * (y[2]-y[1])


def area(r):
    return abs((r[2]-r[0]) * (r[3]-r[1]))


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    r1 = [int(i) for i in input().split()]
    r2 = [int(i) for i in input().split()]
    r3 = [int(i) for i in input().split()]

    print(area(r1) + area(r2) - overlap(r1, r3) - overlap(r2, r3))


if __name__ == "__main__":
    main('billboard')

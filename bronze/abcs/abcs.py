import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')

    lst = sorted([int(i) for i in input().split()])
    a = lst[0]
    b = lst[1]
    ab = a + b
    if lst.index(ab) == 2:
        c = lst[3]
    else:
        c = lst[2]

    print(a, b, c)


if __name__ == '__main__':
    main('abcs')
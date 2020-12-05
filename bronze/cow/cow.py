import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    s = input()
    cow = 0
    ow = 0
    w = 0

    for i in range(len(s)-1, -1, -1):
        if s[i] == 'C':
            cow += ow
        elif s[i] == 'O':
            ow += w
        elif s[i] == 'W':
            w += 1

    print(cow)


if __name__ == "__main__":
    main('cow')

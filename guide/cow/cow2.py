import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    s = input()
    c = 0
    co = 0
    cow = 0

    for i in range(len(s)):
        if s[i] == 'C':
            c += 1
        elif s[i] == 'O':
            co += c
        elif s[i] == 'W':
            cow += co

    print(cow)


if __name__ == "__main__":
    main('cow')

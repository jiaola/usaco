import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    words = []
    f = [0] * 26
    for i in range(n):
        f1 = [0] * 26
        f2 = [0] * 26
        w1, w2 = input().split()
        for c in w1:
            ind = ord(c) - ord('a')
            f1[ind] += 1
        for c in w2:
            ind = ord(c) - ord('a')
            f2[ind] += 1
        for j in range(26):
            f[j] += max(f1[j], f2[j])
    for i in f:
        print(i)


if __name__ == "__main__":
    main('blocks')

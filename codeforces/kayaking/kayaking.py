import sys


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    # sys.stdout = open(pname + '.out', 'w')
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort()
    m = 100000
    for i in range(2*n):
        for j in range(i):
            d = l[:j] + l[j+1:i] + l[i+1:]
            s = 0
            for k in range(0, len(d)-1, 2):
                s += d[k+1] - d[k]
            m = min(m, s)
    print(m)


if __name__ == "__main__":
    main('')

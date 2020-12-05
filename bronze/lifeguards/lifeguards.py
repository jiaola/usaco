import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    lg = []
    for i in range(n):
        lg.append([int(j) for j in input().split()])
    m = 0
    for i in range(n):
        mi = 0
        for j in range(1001):
            j_in = False
            for k in range(n):
                if k == i:
                    continue
                if lg[k][0] < j <= lg[k][1]:
                    j_in = True
                    break
            if j_in:
                mi += 1
        m = max(m, mi)
    print(m)


if __name__ == "__main__":
    main('lifeguards')

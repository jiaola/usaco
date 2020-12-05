import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, m = [int(i) for i in input().split()]
    s = []
    p = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        p.append(input())

    t = 0
    for i in range(m):
        s_set = set()
        p_set = set()
        for j in range(n):
            s_set.add(s[j][i])
            p_set.add(p[j][i])
        if s_set.isdisjoint(p_set):
            t += 1
    print(t)


if __name__ == "__main__":
    main('cownomics')

import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    f = []
    for i in range(2001):
        f.append([-1]*2001)
    x, y = 1000, 1000
    f[x][y] = 0
    n = int(input())
    t = 0
    m = 2000
    for i in range(n):
        d, s = input().split()
        s = int(s)
        for j in range(s):
            t += 1
            if d == 'N':
                y += 1
            elif d == 'E':
                x += 1
            elif d == 'W':
                x -= 1
            else:
                y -= 1
            if f[x][y] >= 0:
                m = min(m, t-f[x][y])
            f[x][y] = t
    if m == 2000:
        m = -1
    print(m)



if __name__ == "__main__":
    main('mowing')

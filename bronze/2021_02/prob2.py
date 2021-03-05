import sys


def main(pname):
    s = 1001
    d = []
    c = []
    for i in range(s):
        d.append([0] * s)
        c.append([0] * s)

    N = int(input())
    total = 0
    for i in range(N):
        x, y = [int(j) for j in input().split()]
        d[x][y] += 1
        pairs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for pair in pairs:
            a, b = pair
            if 0 <= a < s and 0 <= b < s:
                if c[a][b] == 2:
                    total += 1 * d[a][b]
                elif c[a][b] == 3:
                    total -= 1 * d[a][b]
                c[a][b] += 1
        print(total)


if __name__ == "__main__":
    main('prob2')

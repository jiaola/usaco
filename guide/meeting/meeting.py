import sys


def travel(g, current, paths, target, dist):
    if current != target:
        for j in g[current]:
            paths = travel(g, j, paths, target, dist + g[current][j])
    else:
        paths.append(dist)
    return paths


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, m = [int(i) for i in input().split()]
    g1 = []
    g2 = []
    for i in range(n):
        g1.append({})
        g2.append({})
    for i in range(m):
        a, b, c, d = [int(j) for j in input().split()]
        g1[a-1][b-1] = c
        g2[a-1][b-1] = d

    p1 = travel(g1, 0, [], n-1, 0)
    p2 = travel(g2, 0, [], n-1, 0)
    p1.sort()
    p2.sort()
    i1 = 0
    i2 = 0
    while i1 < len(p1) and i2 < len(p2):
        if p1[i1] > p2[i2]:
            i2 += 1
        elif p1[i1] < p2[i2]:
            i1 += 1
        else:
            break
    if i1 < len(p1) and i2 < len(p2):
        print(p1[i1])
    else:
        print('IMPOSSIBLE')


if __name__ == "__main__":
    main('meeting')

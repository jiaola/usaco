import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    lst = [int(i) for i in input().split()]
    lst.sort()

    g = [-1] * n
    for i in range(n):
        if i == 0:
            g[i] = 1
        elif i == n - 1:
            g[i] = n-2
        else:
            if (lst[i] - lst[i-1]) > (lst[i+1] - lst[i]):
                g[i] = i+1
            else:
                g[i] = i-1
    in_degree = [0] * n
    out_degree = [0] * n
    for i in range(n):
        in_degree[g[i]] += 1
        if g[i] != -1:
            out_degree[i] += 1
    a = in_degree.count(0)
    b = 0
    for i in range(n):
        if in_degree[i] == 1 and out_degree[i] == 1:
            target = g[i]
            if in_degree[target] == 1 and g[target] == i:
                b += 1

    print(a + int(b / 2))


if __name__ == "__main__":
    main('hoofball')

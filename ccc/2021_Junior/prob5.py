import sys

# a O(k) algorithm
def main(pname):
    m = int(input())
    n = int(input())

    r = [0] * m
    c = [0] * n

    ans = 0
    k = int(input())
    for i in range(k):
        d, p = input().split()
        p = int(p)
        if d == 'R':
            r[p-1] += 1
        else:
            c[p-1] += 1
    nr = 0
    nc = 0
    for i in range(m):
        if r[i] % 2 == 1:
            nr += 1
    for i in range(n):
        if c[i] % 2 == 1:
            nc += 1

    print(nr * n + nc * m - 2 * nc * nr)


if __name__ == '__main__':
    main('prob4')

import sys
import math

sys.setrecursionlimit(10000)

M = 0
N = 0
visited = []
b = []


def dfs(i, j):
    global M, N, visited, b
    if i > M or j > N:
        return False
    elif i == M and j == N:
        return True
    else:
        if not visited[i-1][j-1]:
            v = b[i-1][j-1]
            visited[i-1][j-1] = True
            for k in range(1, math.floor(v ** 0.5) + 1):
                if v % k == 0:
                    l = v // k
                    if dfs(l, k) or dfs(k, l):
                        return True
    return False


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')
    global b, visited, M, N

    M = int(input())
    N = int(input())

    for i in range(M):
        b.append([int(j) for j in input().split()])
        visited.append([False] * N)

    if dfs(1, 1):
        print('yes')
    else:
        print('no')


if __name__ == "__main__":
    main('prob5')

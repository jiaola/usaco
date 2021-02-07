import sys
import math

sys.setrecursionlimit(10000)

M = 0
N = 0
visited = []
b = []
s = []


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')
    global b, visited, M, N

    M = int(input())
    N = int(input())

    for i in range(M):
        b.append([int(j) for j in input().split()])
        visited.append([False] * N)
        for j in range(N):
            s.append((b[i][j], i, j))
    s.sort()
    print(s)


    current = (M, N)



if __name__ == "__main__":
    main('prob5_1')

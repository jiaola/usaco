# Brute force. Only passes 5 tests. The rest time out.

import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    N = int(input())
    cows = []
    for i in range(N):
        cows.append([int(i) for i in input().split()])
    cows.sort()
    t = 0
    for i in range(N):
        speed_i = cows[i][1]
        free = True
        for j in range(i+1, N):
            if cows[j][1] < speed_i:
                free = False
                break
        if free:
            t += 1
    print(t)


if __name__ == "__main__":
    main('cowjog')

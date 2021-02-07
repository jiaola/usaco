import sys
import math


def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    # sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    d = [0] * n

    for i in range(1, n):
        a, b = [int(j) for j in input().split()]
        d[a-1] += 1
        d[b-1] += 1

    ans = 0
    for i in range(n):
        if i == 0:
            ans += math.ceil(math.log2(d[i] + 1)) + d[i]
        elif d[i] > 1:
            ans += math.ceil(math.log2(d[i])) + d[i] - 1

    print(ans)


if __name__ == "__main__":
    main('prob1')

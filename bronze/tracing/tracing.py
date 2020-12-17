import sys


def check(n, i, k, shakes):
    cows = [-1] * n
    cows[i] = 0
    for shake in shakes:
        if (cows[shake[1]] == -1 or cows[shake[1]] >= k) and (cows[shake[2]] == -1 or cows[shake[2]] >= k):
            continue
        else:
            cows[shake[1]] += 1
            cows[shake[2]] += 1
    result = [0] * n
    for i in range(n):
        if cows[i] >= 0:
            result[i] = 1
    return result


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, t = [int(i) for i in input().split()]
    sick = [int(i) for i in list(input())]
    shakes = []
    for i in range(t):
        x, y, z = [int(j) for j in input().split()]
        shakes.append([x, y-1, z-1])
    shakes.sort()

    min_k = n
    max_k = 0
    start = []
    for i in range(n):
        if sick[i] == 1:
            possible = False
            for k in range(t):
                result = check(n, i, k, shakes)
                if result == sick:
                    possible = True
                    break
            min_k = min(min_k, k)
            for k in range(t+1, -1, -1):
                result = check(n, i, k, shakes)
                if result == sick:
                    break
            max_k = max(max_k, k)
            if possible:
                start.append(i)
    if max_k == t+1:
        max_k = 'Infinity'

    print(len(start), min_k, max_k)


if __name__ == "__main__":
    main('tracing')

import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    cows = []
    for i in range(n):
        j, k = [int(i) for i in input().split()]
        cows.append((j, k))
    cows.sort()

    min_dist = 10**6
    for i in range(n):
        if cows[i][1] == 0:
            if i > 0 and cows[i-1][1] == 1:
                min_dist = min(min_dist, cows[i][0] - cows[i-1][0])
            elif i < n-1 and cows[i+1][1] == 1:
                min_dist = min(min_dist, cows[i+1][0] - cows[i][0])
    count = 0

    last_x = -1
    for i in range(n):
        if cows[i][1] == 1:
            if last_x == -1:
                count += 1
            else:
                if cows[i][0] - last_x >= min_dist:
                    count += 1
            last_x = cows[i][0]

    print(count)


if __name__ == "__main__":
    main('socdist2')
